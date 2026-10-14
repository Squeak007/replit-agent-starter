"""
Example 5: Minimal terminal chat UI with tool access.
Usage: python examples/chat_cli.py
"""
import sys
sys.path.insert(0, ".")

from agent import Agent
from tools import ALL_TOOLS


def main():
    print("Squeak Agent — chat mode. Type 'exit' to quit.\n")
    agent = Agent(
        system=(
            "You are a helpful assistant with filesystem, web, and shell access. "
            "Use tools when needed. Be concise."
        ),
        tools=ALL_TOOLS,
    )
    while True:
        try:
            user = input("you > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user.lower() in ("exit", "quit"):
            break
        if not user:
            continue
        try:
            response = agent.run(user)
            print(f"agent > {response}\n")
        except Exception as e:
            print(f"error: {e}\n")


if __name__ == "__main__":
    main()
