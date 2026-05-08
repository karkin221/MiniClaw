class ContextBuilder:

    SYSTEM_PROMPT = '''
You are a coding agent.

Use tools aggressively:
- list_files
- read_file
- search_codebase
- inspect_architecture
- grep_text
- write_file
- run_python

Workflow:
1. inspect repo
2. read docs
3. inspect architecture
4. explain findings
'''

    @classmethod
    def build(cls, messages, retrieved=""):

        system = cls.SYSTEM_PROMPT

        if retrieved:
            system += "\n\nRetrieved:\n" + retrieved

        return [
            {
                "role": "system",
                "content": system
            }
        ] + messages[-15:]
