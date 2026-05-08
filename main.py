
from runtime.conversation_runtime import ConversationRuntime
from rich import print

runtime = ConversationRuntime(model="qwen3:14b")

print("\n[bold green]Mini Claw Runtime v5[/bold green]")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You> ") # for e.g. inspect repository

    if user_input.strip().lower() in [
        "exit",
        "quit"
    ]:
        break

    runtime.add_user_message(user_input)

    runtime.run(max_steps=10)

print("\n===== EVENT REPLAY =====")
runtime.replay()