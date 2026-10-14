"""Fetch a URL and return the text content."""
import urllib.request
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            text = data.strip()
            if text:
                self.parts.append(text)


def _handler(url: str, max_chars: int = 10000) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "SqueakAgent/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    parser = _TextExtractor()
    parser.feed(html)
    text = "\n".join(parser.parts)
    return text[:max_chars] + ("..." if len(text) > max_chars else "")


FETCH_URL = {
    "name": "fetch_url",
    "description": "Fetch a URL and return the plain-text content. Use this to read web pages.",
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "The URL to fetch."},
            "max_chars": {"type": "integer", "description": "Max characters to return.", "default": 10000},
        },
        "required": ["url"],
    },
    "handler": _handler,
}
