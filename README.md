# RestoraX for ComfyUI

ComfyUI custom nodes for [RestoraX](https://github.com/karailker/restorax), an open-source AI video and audio restoration toolkit. Every RestoraX restorer is exposed as a node: super-resolution, face restoration, colorization, frame interpolation, deinterlacing, scratch removal, HDR conversion, stabilization and audio restoration.

> **Model status:** not every restorer ships working weights yet. See the
> [model status table](https://github.com/karailker/restorax#model-status) in the RestoraX README. Restorers that cannot load raise an explicit error instead of silently passing frames through.

## Install

Into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/karailker/restorax-comfyui
pip install -r restorax-comfyui/requirements.txt
```

Restart ComfyUI. The nodes appear under the **RestoraX** category. Once published, the pack is also installable from the [ComfyUI Registry](https://registry.comfy.org) / ComfyUI Manager.

## Optional: DLSS 5 Neural Rendering node

The *RestoraX DLSS 5 Neural Rendering (external)* node drives an externally installed [Visual Enhancer](https://github.com/Merserk/dlss5-visual-enhancer) (`VE_CLI.exe`). Nothing from Visual Enhancer or NVIDIA is bundled; you install it yourself under its own license and set `RESTORAX_VE_CLI`. It runs natively on Windows 11 with an NVIDIA RTX GPU; on Linux it is experimental and goes through Wine/Proton (`RESTORAX_VE_LAUNCHER`). See the RestoraX README for details.

## Development

```bash
pip install -r requirements.txt pytest ruff
python -m pytest tests
ruff check . && ruff format --check .
```

`tests/test_comfyui_load.py` loads the pack inside a real ComfyUI checkout and is skipped unless `COMFYUI_PATH` is set.

## History

These nodes previously lived in the `comfyui_nodes/` directory of the main RestoraX repository ([restorax#24](https://github.com/karailker/restorax/issues/24)).

## License

MIT, see [LICENSE](LICENSE).
