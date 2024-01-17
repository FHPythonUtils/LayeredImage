# Ora

[Layeredimage Index](../../README.md#layeredimage-index) / [Layeredimage](../index.md#layeredimage) / [Io](./index.md#io) / Ora

> Auto-generated documentation for [layeredimage.io.ora](../../../../layeredimage/io/ora.py) module.

- [Ora](#ora)
  - [addLayer_ORA](#addlayer_ora)
  - [openLayer_ORA](#openlayer_ora)
  - [saveLayer_ORA](#savelayer_ora)

## addLayer_ORA

[Show source in ora.py:128](../../../../layeredimage/io/ora.py#L128)

Update the project with a shiny new layer.

#### Signature

```python
def addLayer_ORA(project: Any, layer: Any, blendLookup: dict[BlendType, str]) -> Any: ...
```



## openLayer_ORA

[Show source in ora.py:14](../../../../layeredimage/io/ora.py#L14)

Open an .ora file into a layered image.

#### Signature

```python
def openLayer_ORA(file: str) -> LayeredImage: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## saveLayer_ORA

[Show source in ora.py:84](../../../../layeredimage/io/ora.py#L84)

Save a layered image as .ora.

#### Signature

```python
def saveLayer_ORA(fileName: str, layeredImage: LayeredImage) -> None: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)