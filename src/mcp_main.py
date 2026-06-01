import asyncio

from langgraph.graph import END, StateGraph

from src.mcp_agents import McpState, acquisition_agent, analysis_agent, report_agent


def build_graph():
    graph = StateGraph(McpState)
    graph.add_node("acquire", acquisition_agent)
    graph.add_node("analyze", analysis_agent)
    graph.add_node("report", report_agent)

    graph.set_entry_point("acquire")
    graph.add_edge("acquire", "analyze")
    graph.add_edge("analyze", "report")
    graph.add_edge("report", END)
    return graph.compile()


async def main() -> None:
    app = build_graph()
    final_state = await app.ainvoke({"user_request": "Acquire one image and summarize it."})
    print(final_state["report"])


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
