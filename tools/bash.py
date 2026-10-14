"""Run a shell command and return stdout+stderr."""
import subprocess


def _handler(command: str, timeout: int = 30) -> str:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        out = result.stdout
        err = result.stderr
        parts = []
        if out:
            parts.append(f"stdout:\n{out}")
        if err:
            parts.append(f"stderr:\n{err}")
        parts.append(f"exit_code: {result.returncode}")
        return "\n".join(parts)
    except subprocess.TimeoutExpired:
        return f"Error: command timed out after {timeout}s"


BASH = {
    "name": "bash",
    "description": "Run a shell command. Returns stdout, stderr, and exit code. Timeout 30s.",
    "input_schema": {
        "type": "object",
        "properties": {
            "command": {"type": "string"},
            "timeout": {"type": "integer", "default": 30},
        },
        "required": ["command"],
    },
    "handler": _handler,
}
