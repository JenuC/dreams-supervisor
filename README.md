# DREAMS Agent Skeleton

Minimal local/non-local multi-agent skeleton for DREAMS-style microscopy automation.

It has two runnable paths:

- `src/main.py`: LangGraph supervisor using local Python functions directly.
- `src/mcp_main.py`: LangGraph supervisor whose agents call FastMCP tools.

## Run

```powershell
uv sync
uv run dreams-local
uv run dreams-mcp
```

The fake acquisition step writes `latest_image.npy` in the project root.

## MCP server

The MCP server is in `src/mcp_server.py`.

By default, `dreams-mcp` uses FastMCP's in-memory client transport so it stays simple and does not need a second process. To exercise stdio process transport instead:

```powershell
$env:DREAMS_MCP_TRANSPORT = "stdio"
uv run dreams-mcp
```

You can also run the server directly:

```powershell
uv run python -m src.mcp_server
```
