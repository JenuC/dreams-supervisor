import os
from pathlib import Path
from typing import Any, TypedDict

from fastmcp import Client

from src.mcp_server import mcp


class McpState(TypedDict, total=False):
    user_request: str
    image_path: str
    analysis: dict[str, Any]
    report: str


def make_client() -> Client:
    transport = os.getenv("DREAMS_MCP_TRANSPORT", "memory").lower()
    if transport == "stdio":
        server_path = Path(__file__).with_name("mcp_server.py")
        return Client(str(server_path))
    return Client(mcp)


async def acquisition_agent(state: McpState) -> McpState:
    async with make_client() as client:
        result = await client.call_tool("snap_image", {})
    return {"image_path": result.data["image_path"]}


async def analysis_agent(state: McpState) -> McpState:
    async with make_client() as client:
        result = await client.call_tool(
            "analyze_latest_image",
            {"image_path": state["image_path"]},
        )
    return {"analysis": result.data}


async def report_agent(state: McpState) -> McpState:
    analysis = state["analysis"]
    report = (
        "DREAMS MCP microscopy run complete.\n"
        f"- Request: {state['user_request']}\n"
        f"- Image: {analysis['image_path']}\n"
        f"- Mean intensity: {analysis['mean']:.2f}\n"
        f"- Std intensity: {analysis['std']:.2f}\n"
        f"- Max intensity: {analysis['max']}"
    )
    return {"report": report}
