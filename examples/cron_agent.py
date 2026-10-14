"""
Example 4: Run an agent on a schedule (via Replit Scheduled Deployments).

This script is designed to be invoked once per schedule tick (e.g., every hour).
Replit will handle the scheduling via `.replit`'s deployment config.

Set TASK env var to control what the agent does. Example:
    TASK="Check https://news.ycombinator.com and summarize the top 3 stories"
"""
import os
import sys
import datetime
sys.path.insert(0, ".")

from agent import Agent
from tools import FETCH_URL, SUMMARIZE_URL, WRITE_FILE


def main():
    task = os.getenv("TASK", "Summarize https://news.ycombinator.com into 5 bullet points.")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    agent = Agent(
        system="You are a scheduled agent. Do the task, write the output to a timestamped file, and report what you did.",
        tools=[FETCH_URL, SUMMARIZE_URL, WRITE_FILE],
    )
    result = agent.run(f"{task} Save the output to runs/{stamp}.md and tell me the filename.")
    print(f"[{stamp}] {result}")


if __name__ == "__main__":
    main()
