"""Ready-to-use tools for the agent. Import and pass to Agent(tools=[...])."""
from .fetch_url import FETCH_URL
from .files import READ_FILE, WRITE_FILE
from .bash import BASH
from .summarize import SUMMARIZE_URL

ALL_TOOLS = [FETCH_URL, READ_FILE, WRITE_FILE, BASH, SUMMARIZE_URL]
