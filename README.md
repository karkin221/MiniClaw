
# Mini Claw Runtime

Interactive real-time local agent runtime inspired by:
- Claw
- Cursor
- Claude Code
- OpenHands

## Features

- Interactive shell
- Streaming responses
- Native tool calling
- Session IDs
- SQLite event replay
- Retrieval engine
- Background task queue
- Structured actions
- Multi-step runtime loop

## Install

```bash
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com

Pull model:

```bash
ollama pull qwen3:14b
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

## Example Prompts

- inspect repository architecture
- read the README and summarize
- search the codebase for runtime logic
- create a notes file
- run a python calculation
