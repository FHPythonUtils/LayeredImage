# common

> Auto-generated documentation for [layeredimage.io.common](../../../layeredimage/io/common.py) module.

Do file io - Common Operations for file readers/writers.

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../README.md#layeredimage-modules) / [layeredimage](../index.md#layeredimage) / [io](index.md#io) / common
    - [blendModeLookup](#blendmodelookup)
    - [expandLayersToCanvas](#expandlayerstocanvas)

## blendModeLookup

[[find in source code]](../../../layeredimage/io/common.py#L14)

```python
def blendModeLookup(
    blendmode: Any,
    blendLookup: dict[(Any, Any)],
    default: Any = BlendType.NORMAL,
) -> BlendType:
```

Get the blendmode from a lookup table.

## expandLayersToCanvas

[[find in source code]](../../../layeredimage/io/common.py#L26)

```python
def expandLayersToCanvas(
    layeredImage: LayeredImage,
    imageFormat: str,
) -> list[Image]:
```

Return layers and throw a warning if the image has groups.
