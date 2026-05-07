
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
