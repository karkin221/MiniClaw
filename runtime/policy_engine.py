
class PolicyEngine:

    ALLOWED_TOOLS = [
        "list_files"
    ]

    @classmethod
    def validate(cls, response):

        if response["type"] == "tool_call":

            if response["tool"] not in cls.ALLOWED_TOOLS:

                return False, "Blocked tool"

        return True, None
