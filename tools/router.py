from tools.filesystem import (
    list_files,
    read_file,
    search_codebase,
    write_file,
    run_python,
    inspect_architecture,
    grep_text
)

class ToolRouter:

    TOOLS = {
        "list_files": list_files,
        "read_file": read_file,
        "search_codebase": search_codebase,
        "write_file": write_file,
        "run_python": run_python,
        "inspect_architecture": inspect_architecture,
        "grep_text": grep_text
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
                    "name": name,
                    "description": f"Tool: {name}",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                }
            }
            for name in cls.TOOLS.keys()
        ]
