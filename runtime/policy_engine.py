
class PolicyEngine:

    ALLOWED_TOOLS = [
        "list_files",
        "read_file",
        "search_codebase",
        "write_file",
        "run_python",
        "inspect_architecture",
        "grep_text"
    ]

    @classmethod
    def validate(cls, response):

        if response["type"] == "tool_call":

            tool = response["tool"]

            if tool not in cls.ALLOWED_TOOLS:

                return False, f"Blocked tool: {tool}"

        return True, None
