from pathlib import Path
from typing import Any

import numpy as np


IMAGE_PATH = Path("latest_image.npy")


def snap_image(path: str | Path = IMAGE_PATH) -> dict[str, Any]:
    """Create a fake microscope image and save it as a NumPy array."""
    output_path = Path(path)
    image = np.random.default_rng().poisson(lam=12, size=(64, 64)).astype(np.uint16)
    np.save(output_path, image)
    return {
        "image_path": str(output_path),
        "shape": list(image.shape),
        "dtype": str(image.dtype),
    }


def analyze_latest_image(path: str | Path = IMAGE_PATH) -> dict[str, float | int | str]:
    """Load the latest fake microscope image and return simple statistics."""
    image_path = Path(path)
    if not image_path.exists():
        raise FileNotFoundError(f"No image found at {image_path}. Run snap_image first.")

    image = np.load(image_path)
    return {
        "image_path": str(image_path),
        "mean": float(image.mean()),
        "std": float(image.std()),
        "max": int(image.max()),
    }
