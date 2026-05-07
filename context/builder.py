
class ContextBuilder:

    SYSTEM_PROMPT = '''
You are a local coding agent.

You have tools available.

Use tools whenever useful.

After receiving tool results:
- explain findings
- summarize clearly
'''

    @classmethod
    def build(cls, messages, retrieved_context=""):

        system = cls.SYSTEM_PROMPT

        if retrieved_context:
            system += f"\n\nRetrieved Context:\n{retrieved_context}"

        return [
            {
                "role": "system",
                "content": system
            }
        ] + messages[-12:]
