"""
Example 3: Polish a draft while preserving your voice.
Usage: python examples/writing_assistant.py draft.txt
"""
import sys
sys.path.insert(0, ".")

from agent import Agent
from tools import READ_FILE, WRITE_FILE

WRITER_PROMPT = """You are a writing assistant that preserves the user's voice. Rules:
- Never use "delve", "furthermore", "moreover", "in conclusion", or em-dashes.
- Match sentence rhythm: alternate short and long. No two paragraphs same length.
- Use concrete nouns. Replace "things" with the actual thing.
- Edit, don't rewrite. Keep 80%+ of the user's words when revising.
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python examples/writing_assistant.py <draft.txt>")
        sys.exit(1)
    path = sys.argv[1]

    agent = Agent(system=WRITER_PROMPT, tools=[READ_FILE, WRITE_FILE])
    result = agent.run(
        f"Read {path}, polish it per your rules, and write the revised version to {path}.polished.md. "
        f"Keep the author's voice. Only edit, don't rewrite."
    )
    print(result)


if __name__ == "__main__":
    main()
