"""
Example 2: Scrape a page, detect change since last run, notify.

Change detection: hash of extracted text. State stored in state.json.
Notification: prints to stdout (replace with email/Slack/Discord in prod).

Usage: python examples/scrape_and_notify.py https://example.com "price selector or free text"
"""
import sys
import json
import hashlib
import os
sys.path.insert(0, ".")

from agent import Agent
from tools import FETCH_URL

STATE_FILE = "state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def main():
    if len(sys.argv) < 3:
        print("Usage: python examples/scrape_and_notify.py <URL> <what-to-watch>")
        sys.exit(1)
    url = sys.argv[1]
    watch = sys.argv[2]

    agent = Agent(
        system="You extract specific information from web pages. Return only the requested data, nothing else.",
        tools=[FETCH_URL],
    )
    result = agent.run(f"Fetch {url} and tell me the current value of: {watch}")

    state = load_state()
    key = hashlib.md5(f"{url}|{watch}".encode()).hexdigest()
    prev = state.get(key)
    state[key] = {"url": url, "watch": watch, "value": result}
    save_state(state)

    if prev is None:
        print(f"[FIRST RUN] {watch} = {result}")
    elif prev["value"] != result:
        print(f"[CHANGED] {watch}")
        print(f"  before: {prev['value']}")
        print(f"  after:  {result}")
    else:
        print(f"[NO CHANGE] {watch} = {result}")


if __name__ == "__main__":
    main()
