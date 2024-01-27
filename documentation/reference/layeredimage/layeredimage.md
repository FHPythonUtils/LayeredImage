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

[Show source in layeredimage.py:46](../../../layeredimage/layeredimage.py#L46)

Get the string representation.

#### Signature

```python
def __repr__(self) -> str: ...
```

### LayeredImage().__str__

[Show source in layeredimage.py:50](../../../layeredimage/layeredimage.py#L50)

Get the string representation.

#### Signature

```python
def __str__(self) -> str: ...
```

### LayeredImage().addLayerOrGroup

[Show source in layeredimage.py:67](../../../layeredimage/layeredimage.py#L67)

Add a LayerOrGroup.

#### Signature

```python
def addLayerOrGroup(self, layerOrGroup: Layer | Group) -> None: ...
```

### LayeredImage().extractGroups

[Show source in layeredimage.py:123](../../../layeredimage/layeredimage.py#L123)

Extract the groups from the image.

#### Signature

```python
def extractGroups(self) -> list[Group]: ...
```

### LayeredImage().extractLayers

[Show source in layeredimage.py:92](../../../layeredimage/layeredimage.py#L92)

Extract the layers from the image.

#### Signature

```python
def extractLayers(self) -> list[Layer]: ...
```

### LayeredImage().getFlattenLayers

[Show source in layeredimage.py:80](../../../layeredimage/layeredimage.py#L80)

Return an image for all flattened layers.

#### Signature

```python
def getFlattenLayers(self) -> Image.Image: ...
```

### LayeredImage().getLayerOrGroup

[Show source in layeredimage.py:63](../../../layeredimage/layeredimage.py#L63)

Get a LayerOrGroup.

#### Signature

```python
def getLayerOrGroup(self, index: int) -> Layer | Group: ...
```

### LayeredImage().insertLayerOrGroup

[Show source in layeredimage.py:71](../../../layeredimage/layeredimage.py#L71)

Insert a LayerOrGroup at a specific index.

#### Signature

```python
def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int) -> None: ...
```

### LayeredImage().json

[Show source in layeredimage.py:57](../../../layeredimage/layeredimage.py#L57)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```

### LayeredImage().removeLayerOrGroup

[Show source in layeredimage.py:75](../../../layeredimage/layeredimage.py#L75)

Remove a LayerOrGroup at a specific index.

#### Signature

```python
def removeLayerOrGroup(self, index: int) -> None: ...
```

### LayeredImage().updateGroups

[Show source in layeredimage.py:131](../../../layeredimage/layeredimage.py#L131)

Update the groups from the image.

#### Signature

```python
def updateGroups(self) -> None: ...
```

### LayeredImage().updateLayers

[Show source in layeredimage.py:119](../../../layeredimage/layeredimage.py#L119)

Update the layers from the image.

#### Signature

```python
def updateLayers(self) -> None: ...
```



## render

[Show source in layeredimage.py:136](../../../layeredimage/layeredimage.py#L136)

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