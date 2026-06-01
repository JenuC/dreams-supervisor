from typing import Any, TypedDict

from src.local_tools import analyze_latest_image, snap_image


class State(TypedDict, total=False):
    user_request: str
    image_path: str
    analysis: dict[str, Any]
    report: str


def acquisition_agent(state: State) -> State:
    result = snap_image()
    return {"image_path": result["image_path"]}


def analysis_agent(state: State) -> State:
    analysis = analyze_latest_image(state["image_path"])
    return {"analysis": analysis}


def report_agent(state: State) -> State:
    analysis = state["analysis"]
    report = (
        "DREAMS microscopy run complete.\n"
        f"- Request: {state['user_request']}\n"
        f"- Image: {analysis['image_path']}\n"
        f"- Mean intensity: {analysis['mean']:.2f}\n"
        f"- Std intensity: {analysis['std']:.2f}\n"
        f"- Max intensity: {analysis['max']}"
    )
    return {"report": report}
