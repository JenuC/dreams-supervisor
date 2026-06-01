from fastmcp import FastMCP

from src.local_tools import analyze_latest_image as analyze_latest_image_local
from src.local_tools import snap_image as snap_image_local


mcp = FastMCP("dreams-microscopy")


@mcp.tool
def snap_image() -> dict:
    """Acquire a fake microscope image and save it locally."""
    return snap_image_local()


@mcp.tool
def analyze_latest_image(image_path: str = "latest_image.npy") -> dict:
    """Analyze the latest fake microscope image."""
    return analyze_latest_image_local(image_path)


if __name__ == "__main__":
    mcp.run()
