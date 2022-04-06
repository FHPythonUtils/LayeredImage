# LayeredImage

> Auto-generated documentation for [layeredimage.layeredimage](../../../layeredimage/layeredimage.py) module.

LayeredImage class.

- [Layeredimage](../README.md#layeredimage-index) / [Modules](../MODULES.md#layeredimage-modules) / [Layeredimage](index.md#layeredimage) / LayeredImage
    - [LayeredImage](#layeredimage)
        - [LayeredImage().\_\_repr\_\_](#layeredimage__repr__)
        - [LayeredImage().\_\_str\_\_](#layeredimage__str__)
        - [LayeredImage().addImageAsLayer](#layeredimageaddimageaslayer)
        - [LayeredImage().addLayerOrGroup](#layeredimageaddlayerorgroup)
        - [LayeredImage().addLayerRaster](#layeredimageaddlayerraster)
        - [LayeredImage().extractGroups](#layeredimageextractgroups)
        - [LayeredImage().extractLayers](#layeredimageextractlayers)
        - [LayeredImage().flattenLayers](#layeredimageflattenlayers)
        - [LayeredImage().flattenTwoLayers](#layeredimageflattentwolayers)
        - [LayeredImage().getFlattenLayers](#layeredimagegetflattenlayers)
        - [LayeredImage().getFlattenTwoLayers](#layeredimagegetflattentwolayers)
        - [LayeredImage().getLayerOrGroup](#layeredimagegetlayerorgroup)
        - [LayeredImage().insertImageAsLayer](#layeredimageinsertimageaslayer)
        - [LayeredImage().insertLayerOrGroup](#layeredimageinsertlayerorgroup)
        - [LayeredImage().insertLayerRaster](#layeredimageinsertlayerraster)
        - [LayeredImage().json](#layeredimagejson)
        - [LayeredImage().removeLayerOrGroup](#layeredimageremovelayerorgroup)
        - [LayeredImage().updateGroups](#layeredimageupdategroups)
        - [LayeredImage().updateLayers](#layeredimageupdatelayers)
    - [flattenAll](#flattenall)
    - [flattenLayerOrGroup](#flattenlayerorgroup)

## LayeredImage

[[find in source code]](../../../layeredimage/layeredimage.py#L15)

```python
class LayeredImage():
    def __init__(
        layersAndGroups: list[Layer | Group],
        dimensions: tuple[int, int] | None = None,
        **kwargs: Any,
    ):
```

A representation of a layered image such as an ora.

### LayeredImage().\_\_repr\_\_

[[find in source code]](../../../layeredimage/layeredimage.py#L46)

```python
def __repr__():
```

Get the string representation.

### LayeredImage().\_\_str\_\_

[[find in source code]](../../../layeredimage/layeredimage.py#L50)

```python
def __str__():
```

Get the string representation.

### LayeredImage().addImageAsLayer

[[find in source code]](../../../layeredimage/layeredimage.py#L91)

```python
def addImageAsLayer(image: Image.Image, name: str):
```

Resize an image to the canvas and add as a layer.

### LayeredImage().addLayerOrGroup

[[find in source code]](../../../layeredimage/layeredimage.py#L72)

```python
def addLayerOrGroup(layerOrGroup: Layer | Group):
```

Add a LayerOrGroup.

### LayeredImage().addLayerRaster

[[find in source code]](../../../layeredimage/layeredimage.py#L85)

```python
@deprecated(details='use addImageAsLayer', deprecated_in='2021.2.4')
def addLayerRaster(image: Image.Image, name: str):
```

### LayeredImage().extractGroups

[[find in source code]](../../../layeredimage/layeredimage.py#L176)

```python
def extractGroups():
```

Extract the groups from the image.

### LayeredImage().extractLayers

[[find in source code]](../../../layeredimage/layeredimage.py#L145)

```python
def extractLayers():
```

Extract the layers from the image.

### LayeredImage().flattenLayers

[[find in source code]](../../../layeredimage/layeredimage.py#L134)

```python
def flattenLayers(ignoreHidden: bool = True):
```

Flatten all layers.

### LayeredImage().flattenTwoLayers

[[find in source code]](../../../layeredimage/layeredimage.py#L126)

```python
def flattenTwoLayers(
    background: int,
    foreground: int,
    ignoreHidden: bool = True,
):
```

Flatten two layers.

### LayeredImage().getFlattenLayers

[[find in source code]](../../../layeredimage/layeredimage.py#L108)

```python
def getFlattenLayers(ignoreHidden: bool = True) -> Image.Image:
```

Return an image for all flattened layers.

### LayeredImage().getFlattenTwoLayers

[[find in source code]](../../../layeredimage/layeredimage.py#L112)

```python
def getFlattenTwoLayers(
    background: int,
    foreground: int,
    ignoreHidden: bool = True,
) -> Image.Image:
```

Return an image for two flattened layers.

### LayeredImage().getLayerOrGroup

[[find in source code]](../../../layeredimage/layeredimage.py#L68)

```python
def getLayerOrGroup(index: int):
```

Get a LayerOrGroup.

### LayeredImage().insertImageAsLayer

[[find in source code]](../../../layeredimage/layeredimage.py#L102)

```python
def insertImageAsLayer(image: Image.Image, name: str, index: int):
```

Resize an image to the canvas  and insert the layer.

### LayeredImage().insertLayerOrGroup

[[find in source code]](../../../layeredimage/layeredimage.py#L76)

```python
def insertLayerOrGroup(layerOrGroup: Layer | Group, index: int):
```

Insert a LayerOrGroup at a specific index.

### LayeredImage().insertLayerRaster

[[find in source code]](../../../layeredimage/layeredimage.py#L96)

```python
@deprecated(details='use insertImageAsLayer', deprecated_in='2021.2.4')
def insertLayerRaster(image: Image.Image, name: str, index: int):
```

### LayeredImage().json

[[find in source code]](../../../layeredimage/layeredimage.py#L62)

```python
def json() -> dict[str, Any]:
```

Get the object as a dict.

### LayeredImage().removeLayerOrGroup

[[find in source code]](../../../layeredimage/layeredimage.py#L80)

```python
def removeLayerOrGroup(index: int):
```

Remove a LayerOrGroup at a specific index.

### LayeredImage().updateGroups

[[find in source code]](../../../layeredimage/layeredimage.py#L184)

```python
def updateGroups():
```

Update the groups from the image.

### LayeredImage().updateLayers

[[find in source code]](../../../layeredimage/layeredimage.py#L172)

```python
def updateLayers():
```

Update the layers from the image.

## flattenAll

[[find in source code]](../../../layeredimage/layeredimage.py#L229)

```python
def flattenAll(
    layers: list[Layer | Group] | list[Layer],
    imageDimensions: tuple[int, int],
    ignoreHidden: bool = True,
):
```

Flatten a list of layers and groups.

#### Arguments

layers (list[Layer | Group] | list[Layer]): A list of layers and groups
imageDimensions (tuple[int, int]): size of the image
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

## flattenLayerOrGroup

[[find in source code]](../../../layeredimage/layeredimage.py#L189)

```python
def flattenLayerOrGroup(
    layerOrGroup: Layer | Group,
    imageDimensions: tuple[int, int],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
):
```

Flatten a layer or group on to an image of what has already been flattened.

#### Arguments

layerOrGroup (Layer, Group): A layer or a group of layers
imageDimensions (tuple[int, int]): size of the image
- `flattenedSoFar` *Image.Image, optional* - the image of what has already
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image
