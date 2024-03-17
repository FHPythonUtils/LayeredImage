# Common

[Layeredimage Index](../../README.md#layeredimage-index) / [Layeredimage](../index.md#layeredimage) / [Io](./index.md#io) / Common

> Auto-generated documentation for [layeredimage.io.common](../../../../layeredimage/io/common.py) module.

- [Common](#common)
  - [blendModeLookup](#blendmodelookup)
  - [expandLayer](#expandlayer)
  - [expandLayersToCanvas](#expandlayerstocanvas)

## blendModeLookup

[Show source in common.py:15](../../../../layeredimage/io/common.py#L15)

Get the blendmode from a lookup table.

#### Signature

```python
def blendModeLookup(
    blendmode: Any,
    blendLookup: dict[Any, Any],
    default: BlendType | tuple[str, ...] = BlendType.NORMAL,
) -> BlendType: ...
```



## expandLayer

[Show source in common.py:45](../../../../layeredimage/io/common.py#L45)

#### Arguments

----
 foreground (np.ndarray | Image.Image): The foreground layer (must be the same size as the background).
 - `opacity` *float, optional* - The opacity of the foreground image. Defaults to 1.0.
 offsets (Tuple[int, int], optional): Offsets for the foreground layer. Defaults to (0, 0).

#### Returns

-------
 - `Image.Image` - The image.

#### Signature

```python
def expandLayer(
    dimensions: tuple[int, int],
    foreground: np.ndarray | Image.Image,
    opacity: float = 1.0,
    offsets: tuple[int, int] = (0, 0),
) -> Image.Image: ...
```



## expandLayersToCanvas

[Show source in common.py:27](../../../../layeredimage/io/common.py#L27)

Return layers and throw a warning if the image has groups.

#### Signature

```python
def expandLayersToCanvas(
    layeredImage: LayeredImage, imageFormat: str
) -> list[Image.Image]: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)