
# Mini Claw Runtime

A more realistic local-first agent runtime inspired by:
- Claw
- Cursor
- Claude Code
- OpenHands

## New Features

- Native tool calling
- SQLite event persistence
- Streaming responses
- Simple retrieval layer
- Structured runtime architecture
- Local open-source models

## Recommended Model

Install Ollama:

https://ollama.com

Pull model:

```bash
ollama pull qwen3:14b
```

## Install

```bash
pip install -r requirements.txt
```

## Run

Terminal 1:

```bash
ollama serve
```

Terminal 2:

```bash
python main.py
```

## Sample Output

```bash
Tool Result
['tools', 'context', 'memory', 'requirements.txt', 'runtime', 'models', 'README.md', '.git', 'main.py', 'events.db']
Here's the file listing and architecture explanation:

**Files in the project:**
- `tools/` - Contains function definitions for tool calling
- `context/` - Manages conversation context/state
- `memory/` - Handles persistent memory storage
- `requirements.txt` - Python dependencies
- `runtime/` - Core runtime implementation
- `models/` - Local model files (uses Ollama)
- `README.md` - Project documentation
- `.git/` - Version control
- `main.py` - Entry point
- `events.db` - SQLite event persistence database

**Architecture Overview:**
1. **Runtime Layer** - Core agent logic in `runtime/` with structured architecture
2. **Persistence** - Uses SQLite in `events.db` for event tracking
3. **Models** - Local open-source models via Ollama (Qwen3:14b recommended)
4. **Tools** - Native tool calling system in `tools/`
5. **Memory** - State management in `memory/`
6. **Context** - Conversation context handling in `context/`
7. **Streaming** - Implemented through the runtime architecture
8. **Retrieval** - Simple retrieval layer integrated

The system follows a modular design with clear separation of concerns between runtime, persistence, models, and tools.

===== REPLAY =====


(1778141153.2655191, 'UserMessage', '{"role": "user", "content": "list files and explain the architecture"}')


(1778141166.972126, 'LLMOutput', '{"type": "tool_call", "tool": "list_files", "args": {}}')


(1778141166.973354, 'ToolRequested', '{"type": "tool_call", "tool": "list_files", "args": {}}')


(1778141166.9742389, 'ToolCompleted', '["tools", "context", "memory", "requirements.txt", "runtime", "models", "README.md", ".git", "main.py", "events.db"]')


(
    1778141205.507819,
    'LLMOutput',
    '{"type": "assistant_message", "content": "Here\'s the file listing and architecture explanation:\\n\\n**Files in the project:**\\n- `tools/` - Contains function definitions for tool calling\\n- `context/` - 
Manages conversation context/state\\n- `memory/` - Handles persistent memory storage\\n- `requirements.txt` - Python dependencies\\n- `runtime/` - Core runtime implementation\\n- `models/` - Local model files 
(uses Ollama)\\n- `README.md` - Project documentation\\n- `.git/` - Version control\\n- `main.py` - Entry point\\n- `events.db` - SQLite event persistence database\\n\\n**Architecture Overview:**\\n1. **Runtime 
Layer** - Core agent logic in `runtime/` with structured architecture\\n2. **Persistence** - Uses SQLite in `events.db` for event tracking\\n3. **Models** - Local open-source models via Ollama (Qwen3:14b 
recommended)\\n4. **Tools** - Native tool calling system in `tools/`\\n5. **Memory** - State management in `memory/`\\n6. **Context** - Conversation context handling in `context/`\\n7. **Streaming** - Implemented 
through the runtime architecture\\n8. **Retrieval** - Simple retrieval layer integrated\\n\\nThe system follows a modular design with clear separation of concerns between runtime, persistence, models, and 
tools."}'
)
```