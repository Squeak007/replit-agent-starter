"""Fetch a URL and ask the LLM to summarize it in one call."""
from providers import get_provider
from .fetch_url import _handler as _fetch


def _handler(url: str, style: str = "bullet points") -> str:
    content = _fetch(url, max_chars=12000)
    provider = get_provider()
    resp = provider.chat(
        messages=[{"role": "user", "content": f"Summarize the following in {style}:\n\n{content}"}],
        system="You are a concise, high-signal summarizer.",
        max_tokens=1024,
    )
    return resp["text"]


SUMMARIZE_URL = {
    "name": "summarize_url",
    "description": "Fetch a URL and return an LLM-generated summary. Style can be 'bullet points', 'paragraph', 'tweet thread', etc.",
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {"type": "string"},
            "style": {"type": "string", "default": "bullet points"},
        },
        "required": ["url"],
    },
    "handler": _handler,
}
