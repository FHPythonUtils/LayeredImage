# Ora

[Layeredimage Index](../../README.md#layeredimage-index) / [Layeredimage](../index.md#layeredimage) / [Io](./index.md#io) / Ora

> Auto-generated documentation for [layeredimage.io.ora](../../../../layeredimage/io/ora.py) module.

- [Ora](#ora)
  - [addLayer_ORA](#addlayer_ora)
  - [openLayer_ORA](#openlayer_ora)
  - [saveLayer_ORA](#savelayer_ora)

## addLayer_ORA

[Show source in ora.py:125](../../../../layeredimage/io/ora.py#L125)

Update the project with a shiny new layer.

#### Signature

```python
def addLayer_ORA(project, layer, blendLookup): ...
```



## openLayer_ORA

[Show source in ora.py:11](../../../../layeredimage/io/ora.py#L11)

Open an .ora file into a layered image.

#### Signature

```python
def openLayer_ORA(file: str) -> LayeredImage: ...
```



## saveLayer_ORA

[Show source in ora.py:81](../../../../layeredimage/io/ora.py#L81)

Save a layered image as .ora.

#### Signature

```python
def saveLayer_ORA(fileName: str, layeredImage: LayeredImage) -> None: ...
```