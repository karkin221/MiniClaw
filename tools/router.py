
from tools.filesystem import list_files


class ToolRouter:

    TOOLS = {
        "list_files": list_files
    }

    @classmethod
    def execute(cls, tool_name, args):

        return cls.TOOLS[tool_name](**args)

    @classmethod
    def tool_schemas(cls):

        return [
            {
                "type": "function",
                "function": {
                    "name": "list_files",
                    "description": "List files in current directory",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                }
            }
        ]
