# LayerGroup

[Layeredimage Index](../README.md#layeredimage-index) / [Layeredimage](./index.md#layeredimage) / LayerGroup

> Auto-generated documentation for [layeredimage.layergroup](../../../layeredimage/layergroup.py) module.

- [LayerGroup](#layergroup)
  - [Group](#group)
    - [Group().json](#group()json)
  - [Layer](#layer)
    - [Layer().json](#layer()json)
  - [LayerGroup](#layergroup-1)
    - [LayerGroup().__repr__](#layergroup()__repr__)
    - [LayerGroup().__str__](#layergroup()__str__)
    - [LayerGroup().json](#layergroup()json)

## Group

[Show source in layergroup.py:123](../../../layeredimage/layergroup.py#L123)

A representation of an image group.

#### Signature

```python
class Group(LayerGroup):
    def __init__(
        self,
        name: str,
        layers: list[Layer],
        dimensions: tuple[int, int] | None = None,
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType | tuple[str, ...] = BlendType.NORMAL,
    ) -> None: ...
```

#### See also

- [LayerGroup](#layergroup)
- [Layer](#layer)

### Group().json

[Show source in layergroup.py:172](../../../layeredimage/layergroup.py#L172)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```



## Layer

[Show source in layergroup.py:70](../../../layeredimage/layergroup.py#L70)

A representation of an image layer.

#### Signature

```python
class Layer(LayerGroup):
    def __init__(
        self,
        name: str,
        image: Image.Image,
        dimensions: tuple[int, int] | None = None,
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType | tuple[str, ...] = BlendType.NORMAL,
    ) -> None: ...
```

#### See also

- [LayerGroup](#layergroup)

### Layer().json

[Show source in layergroup.py:110](../../../layeredimage/layergroup.py#L110)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```



## LayerGroup

[Show source in layergroup.py:10](../../../layeredimage/layergroup.py#L10)

A representation of an image layer or group.

#### Signature

```python
class LayerGroup:
    def __init__(
        self,
        name: str,
        dimensions: tuple[int, int],
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType | tuple[str, ...] = BlendType.NORMAL,
        **kwargs: dict[str, Any]
    ) -> None: ...
```

### LayerGroup().__repr__

[Show source in layergroup.py:50](../../../layeredimage/layergroup.py#L50)

Get the string representation.

#### Signature

```python
def __repr__(self) -> str: ...
```

### LayerGroup().__str__

[Show source in layergroup.py:54](../../../layeredimage/layergroup.py#L54)

Get the string representation.

#### Signature

```python
def __str__(self) -> str: ...
```

### LayerGroup().json

[Show source in layergroup.py:58](../../../layeredimage/layergroup.py#L58)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```