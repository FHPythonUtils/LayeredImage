# Common

> Auto-generated documentation for [layeredimage.io.common](../../../../layeredimage/io/common.py) module.

Do file io - Common Operations for file readers/writers.

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../MODULES.md#layeredimage-modules) / [Layeredimage](../index.md#layeredimage) / [Io](index.md#io) / Common
    - [blendModeLookup](#blendmodelookup)
    - [expandLayersToCanvas](#expandlayerstocanvas)

## blendModeLookup

[[find in source code]](../../../../layeredimage/io/common.py#L13)

```python
def blendModeLookup(
    blendmode: Any,
    blendLookup: dict[Any, Any],
    default: Any = BlendType.NORMAL,
) -> BlendType:
```

Get the blendmode from a lookup table.

## expandLayersToCanvas

[[find in source code]](../../../../layeredimage/io/common.py#L23)

```python
def expandLayersToCanvas(
    layeredImage: LayeredImage,
    imageFormat: str,
) -> list[Image]:
```

Return layers and throw a warning if the image has groups.
