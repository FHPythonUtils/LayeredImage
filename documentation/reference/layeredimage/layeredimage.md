# LayeredImage

[Layeredimage Index](../README.md#layeredimage-index) / [Layeredimage](./index.md#layeredimage) / LayeredImage

> Auto-generated documentation for [layeredimage.layeredimage](../../../layeredimage/layeredimage.py) module.

- [LayeredImage](#layeredimage)
  - [LayeredImage](#layeredimage-1)
    - [LayeredImage().__repr__](#layeredimage()__repr__)
    - [LayeredImage().__str__](#layeredimage()__str__)
    - [LayeredImage().addLayerOrGroup](#layeredimage()addlayerorgroup)
    - [LayeredImage().extractGroups](#layeredimage()extractgroups)
    - [LayeredImage().extractLayers](#layeredimage()extractlayers)
    - [LayeredImage().getFlattenLayers](#layeredimage()getflattenlayers)
    - [LayeredImage().getLayerOrGroup](#layeredimage()getlayerorgroup)
    - [LayeredImage().insertLayerOrGroup](#layeredimage()insertlayerorgroup)
    - [LayeredImage().json](#layeredimage()json)
    - [LayeredImage().removeLayerOrGroup](#layeredimage()removelayerorgroup)
    - [LayeredImage().updateGroups](#layeredimage()updategroups)
    - [LayeredImage().updateLayers](#layeredimage()updatelayers)
  - [render](#render)

## LayeredImage

[Show source in layeredimage.py:13](../../../layeredimage/layeredimage.py#L13)

A representation of a layered image such as an ora.

#### Signature

```python
class LayeredImage:
    def __init__(
        self,
        layersAndGroups: list[Layer | Group],
        dimensions: tuple[int, int] | None = None,
        **kwargs: dict[str, Any]
    ) -> None: ...
```

### LayeredImage().__repr__

[Show source in layeredimage.py:47](../../../layeredimage/layeredimage.py#L47)

Get the string representation.

#### Signature

```python
def __repr__(self) -> str: ...
```

### LayeredImage().__str__

[Show source in layeredimage.py:51](../../../layeredimage/layeredimage.py#L51)

Get the string representation.

#### Signature

```python
def __str__(self) -> str: ...
```

### LayeredImage().addLayerOrGroup

[Show source in layeredimage.py:68](../../../layeredimage/layeredimage.py#L68)

Add a LayerOrGroup.

#### Signature

```python
def addLayerOrGroup(self, layerOrGroup: Layer | Group) -> None: ...
```

### LayeredImage().extractGroups

[Show source in layeredimage.py:124](../../../layeredimage/layeredimage.py#L124)

Extract the groups from the image.

#### Signature

```python
def extractGroups(self) -> list[Group]: ...
```

### LayeredImage().extractLayers

[Show source in layeredimage.py:93](../../../layeredimage/layeredimage.py#L93)

Extract the layers from the image.

#### Signature

```python
def extractLayers(self) -> list[Layer]: ...
```

### LayeredImage().getFlattenLayers

[Show source in layeredimage.py:81](../../../layeredimage/layeredimage.py#L81)

Return an image for all flattened layers.

#### Signature

```python
def getFlattenLayers(self) -> Image.Image: ...
```

### LayeredImage().getLayerOrGroup

[Show source in layeredimage.py:64](../../../layeredimage/layeredimage.py#L64)

Get a LayerOrGroup.

#### Signature

```python
def getLayerOrGroup(self, index: int) -> Layer | Group: ...
```

### LayeredImage().insertLayerOrGroup

[Show source in layeredimage.py:72](../../../layeredimage/layeredimage.py#L72)

Insert a LayerOrGroup at a specific index.

#### Signature

```python
def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int) -> None: ...
```

### LayeredImage().json

[Show source in layeredimage.py:58](../../../layeredimage/layeredimage.py#L58)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```

### LayeredImage().removeLayerOrGroup

[Show source in layeredimage.py:76](../../../layeredimage/layeredimage.py#L76)

Remove a LayerOrGroup at a specific index.

#### Signature

```python
def removeLayerOrGroup(self, index: int) -> None: ...
```

### LayeredImage().updateGroups

[Show source in layeredimage.py:132](../../../layeredimage/layeredimage.py#L132)

Update the groups from the image.

#### Signature

```python
def updateGroups(self) -> None: ...
```

### LayeredImage().updateLayers

[Show source in layeredimage.py:120](../../../layeredimage/layeredimage.py#L120)

Update the layers from the image.

#### Signature

```python
def updateLayers(self) -> None: ...
```



## render

[Show source in layeredimage.py:137](../../../layeredimage/layeredimage.py#L137)

Flatten a layer or group on to an image of what has already been flattened.

#### Arguments

----
 layerOrGroup (Layer, Group): A layer or a group of layers
 - `project_image` *np.ndarray, optional* - the image of what has already
 been flattened.

#### Returns

-------
 - `np.ndarray` - Flattened image

#### Signature

```python
def render(layerOrGroup: Layer | Group, project_image: np.ndarray) -> np.ndarray: ...
```