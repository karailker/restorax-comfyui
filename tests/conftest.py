"""Expose the repository root as the importable package ``comfyui_nodes``.

The repo directory is named ``restorax-comfyui`` (not a valid module name) and
ComfyUI itself loads the root ``__init__.py`` directly, so tests load it under a
stable alias instead of requiring any particular checkout directory name.
"""

import importlib.util
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

if "comfyui_nodes" not in sys.modules:
    spec = importlib.util.spec_from_file_location(
        "comfyui_nodes", ROOT / "__init__.py", submodule_search_locations=[str(ROOT)]
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["comfyui_nodes"] = module
    spec.loader.exec_module(module)


def pytest_collection_modifyitems(config, items):
    skip = pytest.mark.skip(reason="needs $COMFYUI_PATH set to a real ComfyUI checkout")
    if os.environ.get("COMFYUI_PATH"):
        return
    for item in items:
        if "requires_comfyui" in item.keywords:
            item.add_marker(skip)
