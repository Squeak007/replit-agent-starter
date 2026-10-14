"""
Dual-provider LLM wrapper. Switch between OpenAI and Anthropic
with a single env var: LLM_PROVIDER=openai|anthropic (default: anthropic).

Both providers expose the same interface:
    client = get_provider()
    response = client.chat(messages, tools=None, system=None)

Response is normalized to:
    {
        "text": str,                  # final assistant text
        "tool_calls": [                # if any tools were called
            {"name": str, "input": dict, "id": str}
        ],
        "stop_reason": str,            # "end_turn" | "tool_use" | "max_tokens"
        "raw": object,                 # raw provider response
    }
"""
import os
from typing import Optional


class _AnthropicProvider:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        from anthropic import Anthropic
        self.client = Anthropic()
        self.model = model

    def chat(self, messages, tools=None, system=None, max_tokens=4096):
        kwargs = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": messages,
        }
        if system:
            kwargs["system"] = system
        if tools:
            kwargs["tools"] = tools
        resp = self.client.messages.create(**kwargs)

        text_parts = []
        tool_calls = []
        for block in resp.content:
            if block.type == "text":
                text_parts.append(block.text)
            elif block.type == "tool_use":
                tool_calls.append({
                    "name": block.name,
                    "input": block.input,
                    "id": block.id,
                })
        return {
            "text": "".join(text_parts),
            "tool_calls": tool_calls,
            "stop_reason": resp.stop_reason,
            "raw": resp,
        }


class _OpenAIProvider:
    def __init__(self, model: str = "gpt-4o"):
        from openai import OpenAI
        self.client = OpenAI()
        self.model = model

    def chat(self, messages, tools=None, system=None, max_tokens=4096):
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.extend(messages)

        kwargs = {
            "model": self.model,
            "messages": msgs,
            "max_tokens": max_tokens,
        }
        if tools:
            # Convert Anthropic-style tool defs to OpenAI style
            kwargs["tools"] = [
                {
                    "type": "function",
                    "function": {
                        "name": t["name"],
                        "description": t.get("description", ""),
                        "parameters": t.get("input_schema", {}),
                    },
                }
                for t in tools
            ]
        resp = self.client.chat.completions.create(**kwargs)
        msg = resp.choices[0].message
        tool_calls = []
        if msg.tool_calls:
            import json
            for tc in msg.tool_calls:
                tool_calls.append({
                    "name": tc.function.name,
                    "input": json.loads(tc.function.arguments),
                    "id": tc.id,
                })
        return {
            "text": msg.content or "",
            "tool_calls": tool_calls,
            "stop_reason": resp.choices[0].finish_reason,
            "raw": resp,
        }


def get_provider(provider: Optional[str] = None):
    """Return a provider based on env var or explicit arg."""
    name = (provider or os.getenv("LLM_PROVIDER", "anthropic")).lower()
    if name == "openai":
        return _OpenAIProvider()
    return _AnthropicProvider()
