
from rich import print

from context.builder import ContextBuilder
from memory.retrieval import RetrievalEngine
from models.ollama_client import OllamaClient
from runtime.event_store import EventStore
from runtime.policy_engine import PolicyEngine
from tools.router import ToolRouter


class ConversationRuntime:

    def __init__(self, model="qwen3:14b"):

        self.messages = []

        self.model_client = OllamaClient(
            model=model
        )

        EventStore.init()

    def add_user_message(self, text):

        msg = {
            "role": "user",
            "content": text
        }

        self.messages.append(msg)

        EventStore.emit(
            "UserMessage",
            msg
        )

    def step(self):

        retrieved = RetrievalEngine.retrieve(
            self.messages[-1]["content"]
        )

        messages = ContextBuilder.build(
            self.messages,
            retrieved
        )

        tools = ToolRouter.tool_schemas()

        response = self.model_client.generate(
            messages,
            tools
        )

        EventStore.emit(
            "LLMOutput",
            response
        )

        ok, error = PolicyEngine.validate(
            response
        )

        if not ok:

            print(error)
            return True

        if response["type"] == "tool_call":

            tool_name = response["tool"]

            EventStore.emit(
                "ToolRequested",
                response
            )

            result = ToolRouter.execute(
                tool_name,
                {}
            )

            EventStore.emit(
                "ToolCompleted",
                result
            )

            print("\n[bold yellow]Tool Result[/bold yellow]")
            print(result)

            self.messages.append({
                "role": "tool",
                "content": str(result)
            })

            return False

        if response["type"] == "assistant_message":

            self.messages.append({
                "role": "assistant",
                "content": response["content"]
            })

            return True

        return True

    def run(self, max_steps=5):

        done = False
        steps = 0

        while not done and steps < max_steps:

            done = self.step()

            steps += 1

    def replay(self):

        for row in EventStore.replay():

            print("\n", row)
