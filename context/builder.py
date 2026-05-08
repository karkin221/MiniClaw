
class ContextBuilder:

    SYSTEM_PROMPT = '''
You are a local coding agent.

Use tools aggressively.

Suggested workflow:
1. inspect repository
2. list files
3. read important files
4. inspect architecture
5. summarize findings

Available tools:
- list_files
- read_file
- search_codebase
- inspect_architecture
- grep_text
- write_file
- run_python

Be concise and technical.
'''

    @classmethod
    def build(cls, messages, retrieved=""):

        system = cls.SYSTEM_PROMPT

        if retrieved:
            system += "\n\nRetrieved Context:\n" + retrieved

        return [
            {
                "role": "system",
                "content": system
            }
        ] + messages[-20:]
