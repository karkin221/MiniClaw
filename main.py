from runtime.conversation_runtime import ConversationRuntime

runtime = ConversationRuntime(model="qwen3:14b")

runtime.add_user_message(
    "Inspect this repository. Explain the architecture."
)

runtime.run(max_steps=10)

print("\n===== EVENT REPLAY =====")
runtime.replay()
