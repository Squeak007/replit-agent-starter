"""Read and write files on the local filesystem."""
import os


def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _write(path: str, content: str) -> str:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote {len(content)} chars to {path}"


READ_FILE = {
    "name": "read_file",
    "description": "Read a file from the local filesystem and return its contents.",
    "input_schema": {
        "type": "object",
        "properties": {"path": {"type": "string"}},
        "required": ["path"],
    },
    "handler": _read,
}

WRITE_FILE = {
    "name": "write_file",
    "description": "Write content to a file. Creates parent directories as needed.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string"},
            "content": {"type": "string"},
        },
        "required": ["path", "content"],
    },
    "handler": _write,
}
