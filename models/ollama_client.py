from openai import OpenAI

class OllamaClient:

    def __init__(self, model="qwen3:14b"):

        self.model = model

        self.client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )

    def generate(self, messages, tools):

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools,
            stream=True,
            temperature=0
        )

        final_text = ""
        final_tool_calls = []

        for chunk in stream:

            delta = chunk.choices[0].delta

            if delta.content:
                print(delta.content, end="", flush=True)
                final_text += delta.content

            if delta.tool_calls:
                final_tool_calls.extend(delta.tool_calls)

        print()

        if final_tool_calls:

            tool = final_tool_calls[0]

            return {
                "type": "tool_call",
                "tool": tool.function.name,
                "args": {}
            }

        return {
            "type": "assistant_message",
            "content": final_text
        }
