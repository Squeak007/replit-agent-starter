"""
Example 1: Summarize a URL from the command line.
Usage: python examples/summarize_url.py https://example.com
"""
import sys
sys.path.insert(0, ".")

from agent import Agent
from tools import SUMMARIZE_URL


def main():
    if len(sys.argv) < 2:
        print("Usage: python examples/summarize_url.py <URL> [style]")
        sys.exit(1)
    url = sys.argv[1]
    style = sys.argv[2] if len(sys.argv) > 2 else "bullet points"

    agent = Agent(
        system="You are a helpful research assistant. Use the summarize_url tool to summarize URLs the user gives you.",
        tools=[SUMMARIZE_URL],
    )
    result = agent.run(f"Summarize this URL in {style}: {url}")
    print(result)


if __name__ == "__main__":
    main()
