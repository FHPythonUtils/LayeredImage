# layeredimage

> Auto-generated documentation for [layeredimage.layeredimage](../../layeredimage/layeredimage.py) module.

LayeredImage class

- [Layeredimage](../README.md#layeredimage-index) / [Modules](../README.md#layeredimage-modules) / [layeredimage](index.md#layeredimage) / layeredimage
    - [LayeredImage](#layeredimage)
        - [LayeredImage().addLayerOrGroup](#layeredimageaddlayerorgroup)
        - [LayeredImage().addLayerRaster](#layeredimageaddlayerraster)
        - [LayeredImage().extractGroups](#layeredimageextractgroups)
        - [LayeredImage().extractLayers](#layeredimageextractlayers)
        - [LayeredImage().flattenLayers](#layeredimageflattenlayers)
        - [LayeredImage().flattenTwoLayers](#layeredimageflattentwolayers)
        - [LayeredImage().getFlattenLayers](#layeredimagegetflattenlayers)
        - [LayeredImage().getFlattenTwoLayers](#layeredimagegetflattentwolayers)
        - [LayeredImage().getLayerOrGroup](#layeredimagegetlayerorgroup)
        - [LayeredImage().insertLayerOrGroup](#layeredimageinsertlayerorgroup)
        - [LayeredImage().insertLayerRaster](#layeredimageinsertlayerraster)
        - [LayeredImage().json](#layeredimagejson)
        - [LayeredImage().removeLayerOrGroup](#layeredimageremovelayerorgroup)
        - [LayeredImage().updateGroups](#layeredimageupdategroups)
        - [LayeredImage().updateLayers](#layeredimageupdatelayers)
    - [flattenAll](#flattenall)
    - [flattenLayerOrGroup](#flattenlayerorgroup)
    - [rasterImageOA](#rasterimageoa)
    - [rasterImageOffset](#rasterimageoffset)

## LayeredImage

[[find in source code]](../../layeredimage/layeredimage.py#L8)

```python
class LayeredImage():
    def __init__(
        layersAndGroups: list[Union[(Layer, Group)]],
        dimensions: Optional[tuple[(int, int)]] = None,
        **kwargs: Any,
    ):
```

A representation of a layered image such as an ora

### LayeredImage().addLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L41)

```python
def addLayerOrGroup(layerOrGroup: Union[(Layer, Group)]):
```

Add a LayerOrGroup

### LayeredImage().addLayerRaster

[[find in source code]](../../layeredimage/layeredimage.py#L54)

```python
def addLayerRaster(image: Image.Image, name: str):
```

Raster an image and add as a layer

### LayeredImage().extractGroups

[[find in source code]](../../layeredimage/layeredimage.py#L117)

```python
def extractGroups():
```

Extract the groups from the image

### LayeredImage().extractLayers

[[find in source code]](../../layeredimage/layeredimage.py#L95)

```python
def extractLayers():
```

Extract the layers from the image

### LayeredImage().flattenLayers

[[find in source code]](../../layeredimage/layeredimage.py#L85)

```python
def flattenLayers(ignoreHidden: bool = True):
```

Flatten all layers

### LayeredImage().flattenTwoLayers

[[find in source code]](../../layeredimage/layeredimage.py#L78)

```python
def flattenTwoLayers(
    background: int,
    foreground: int,
    ignoreHidden: bool = True,
):
```

Flatten two layers

### LayeredImage().getFlattenLayers

[[find in source code]](../../layeredimage/layeredimage.py#L66)

```python
def getFlattenLayers(ignoreHidden: bool = True) -> Image.Image:
```

Return an image for all flattened layers

### LayeredImage().getFlattenTwoLayers

[[find in source code]](../../layeredimage/layeredimage.py#L70)

```python
def getFlattenTwoLayers(
    background: int,
    foreground: int,
    ignoreHidden: bool = True,
) -> Image.Image:
```

Return an image for two flattened layers

### LayeredImage().getLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L37)

```python
def getLayerOrGroup(index: int):
```

Get a LayerOrGroup

### LayeredImage().insertLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L45)

```python
def insertLayerOrGroup(layerOrGroup: Union[(Layer, Group)], index: int):
```

Insert a LayerOrGroup at a specific index

### LayeredImage().insertLayerRaster

[[find in source code]](../../layeredimage/layeredimage.py#L59)

```python
def insertLayerRaster(image: Image.Image, name: str, index: int):
```

Raster an image and insert the layer

### LayeredImage().json

[[find in source code]](../../layeredimage/layeredimage.py#L30)

```python
def json() -> dict[(str, Any)]:
```

Get the object as a dict

### LayeredImage().removeLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L49)

```python
def removeLayerOrGroup(index: int):
```

Remove a LayerOrGroup at a specific index

### LayeredImage().updateGroups

[[find in source code]](../../layeredimage/layeredimage.py#L122)

```python
def updateGroups():
```

Update the groups from the image

### LayeredImage().updateLayers

[[find in source code]](../../layeredimage/layeredimage.py#L113)

```python
def updateLayers():
```

Update the layers from the image

## flattenAll

[[find in source code]](../../layeredimage/layeredimage.py#L169)

```python
def flattenAll(
    layers: list[Union[(Layer, Group)]],
    imageDimensions: tuple[(int, int)],
    ignoreHidden: bool = True,
):
```

Flatten a list of layers and groups

#### Arguments

layers (list[Union[Layer, Group]]): A list of layers and groups
imageDimensions (tuple[int, int]): size of the image
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

## flattenLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L139)

```python
def flattenLayerOrGroup(
    layerOrGroup: Union[(Layer, Group)],
    imageDimensions: tuple[(int, int)],
    flattenedSoFar: Optional[Image.Image] = None,
    ignoreHidden: bool = True,
):
```

Flatten a layer or group on to an image of what has already been
flattened

#### Arguments

layerOrGroup (Union[Layer, Group]): A layer or a group of layers
imageDimensions (tuple[int, int]): size of the image
- `flattenedSoFar` *Image.Image, optional* - the image of what has already
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

## rasterImageOA

[[find in source code]](../../layeredimage/layeredimage.py#L126)

```python
def rasterImageOA(
    image: Image.Image,
    size: tuple[(int, int)],
    alpha: float = 1.0,
    offsets: tuple[(int, int)] = (0, 0),
):
```

Rasterise an image with offset and alpha to a given size

## rasterImageOffset

[[find in source code]](../../layeredimage/layeredimage.py#L132)

```python
def rasterImageOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    offsets: tuple[(int, int)] = (0, 0),
):
```

Rasterise an image with offset to a given size
