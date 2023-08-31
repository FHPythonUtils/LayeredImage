# Common

[Layeredimage Index](../../README.md#layeredimage-index) /
[Layeredimage](../index.md#layeredimage) /
[Io](./index.md#io) /
Common

> Auto-generated documentation for [layeredimage.io.common](../../../../layeredimage/io/common.py) module.

- [Common](#common)
  - [blendModeLookup](#blendmodelookup)
  - [expandLayersToCanvas](#expandlayerstocanvas)

## blendModeLookup

[Show source in common.py:13](../../../../layeredimage/io/common.py#L13)

Get the blendmode from a lookup table.

#### Signature

```python
def blendModeLookup(
    blendmode: Any, blendLookup: dict[Any, Any], default: Any = BlendType.NORMAL
) -> BlendType:
    ...
```



## expandLayersToCanvas

[Show source in common.py:23](../../../../layeredimage/io/common.py#L23)

Return layers and throw a warning if the image has groups.

#### Signature

```python
def expandLayersToCanvas(layeredImage: LayeredImage, imageFormat: str) -> list[Image]:
    ...
```