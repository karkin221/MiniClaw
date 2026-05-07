
from runtime.conversation_runtime import ConversationRuntime

runtime = ConversationRuntime(
    model="qwen3:14b"
)

runtime.add_user_message(
    "list files and explain the architecture"
)

runtime.run()

print("\n===== REPLAY =====")
runtime.replay()
