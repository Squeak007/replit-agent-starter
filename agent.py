"""
Core agent loop with tool-calling.

Usage:
    from agent import Agent
    from tools import FETCH_URL, WRITE_FILE

    agent = Agent(
        system="You are a helpful research assistant.",
        tools=[FETCH_URL, WRITE_FILE],
    )
    result = agent.run("Summarize https://example.com and save to summary.md")
    print(result)
"""
from providers import get_provider


class Agent:
    def __init__(self, system: str = "", tools: list = None, max_steps: int = 10):
        self.provider = get_provider()
        self.system = system
        self.tools = tools or []
        self.max_steps = max_steps
        self.tool_map = {t["name"]: t["handler"] for t in self.tools}
        self.tool_defs = [
            {"name": t["name"], "description": t["description"], "input_schema": t["input_schema"]}
            for t in self.tools
        ]

    def run(self, user_message: str) -> str:
        messages = [{"role": "user", "content": user_message}]

        for step in range(self.max_steps):
            response = self.provider.chat(
                messages=messages,
                system=self.system,
                tools=self.tool_defs if self.tool_defs else None,
            )

            # No tool calls → we're done
            if not response["tool_calls"]:
                return response["text"]

            # Add the assistant's response to history
            messages.append({"role": "assistant", "content": response["raw"].content if hasattr(response["raw"], "content") else response["text"]})

            # Execute each tool call
            tool_results = []
            for call in response["tool_calls"]:
                handler = self.tool_map.get(call["name"])
                if not handler:
                    result = f"Error: unknown tool {call['name']}"
                else:
                    try:
                        result = handler(**call["input"])
                    except Exception as e:
                        result = f"Error: {e}"
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": call["id"],
                    "content": str(result),
                })

            messages.append({"role": "user", "content": tool_results})

        return "Agent hit max steps without finishing."
