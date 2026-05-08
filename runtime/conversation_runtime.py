
import uuid

from rich import print

from context.builder import ContextBuilder
from memory.retrieval import RetrievalEngine
from models.ollama_client import OllamaClient
from runtime.event_store import EventStore
from runtime.policy_engine import PolicyEngine
from tasks.task_queue import TaskQueue
from tools.router import ToolRouter


class ConversationRuntime:

    def __init__(self, model="qwen3:14b"):

        self.session_id = str(uuid.uuid4())

        self.messages = []

        self.task_queue = TaskQueue()

        self.model_client = OllamaClient(model=model)

        EventStore.init()

        print(f"[bold blue]Session:[/bold blue] {self.session_id}")

    def add_user_message(self, text):

        msg = {
            "role": "user",
            "content": text
        }

        self.messages.append(msg)

        EventStore.emit(
            self.session_id,
            "UserMessage",
            msg
        )

    def step(self):

        self.task_queue.process_tasks()

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
            self.session_id,
            "LLMOutput",
            response
        )

        ok, error = PolicyEngine.validate(response)

        if not ok:

            print(error)

            return True

        if response["type"] == "tool_call":

            tool_name = response["tool"]

            print(f"\n[bold cyan]Calling Tool:[/bold cyan] {tool_name}")

            EventStore.emit(
                self.session_id,
                "ToolRequested",
                response
            )

            result = ToolRouter.execute(
                tool_name,
                {}
            )

            EventStore.emit(
                self.session_id,
                "ToolCompleted",
                {
                    "tool": tool_name,
                    "result": str(result)[:1000]
                }
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

    def run(self, max_steps=10):

        done = False

        steps = 0

        while not done and steps < max_steps:

            print(f"\n[bold green]===== STEP {steps+1} =====[/bold green]")

            done = self.step()

            steps += 1

    def replay(self):

        rows = EventStore.replay(self.session_id)

        for row in rows:

            print("\n", row)
