# Ora

> Auto-generated documentation for [layeredimage.io.ora](../../../../layeredimage/io/ora.py) module.

Do file io - ORA.

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../MODULES.md#layeredimage-modules) / [Layeredimage](../index.md#layeredimage) / [Io](index.md#io) / Ora
    - [addLayer_ORA](#addlayer_ora)
    - [openLayer_ORA](#openlayer_ora)
    - [saveLayer_ORA](#savelayer_ora)

## addLayer_ORA

[[find in source code]](../../../../layeredimage/io/ora.py#L128)

```python
def addLayer_ORA(project, layer, blendLookup):
```

Update the project with a shiny new layer.

## openLayer_ORA

[[find in source code]](../../../../layeredimage/io/ora.py#L14)

```python
def openLayer_ORA(file: str) -> LayeredImage:
```

Open an .ora file into a layered image.

## saveLayer_ORA

[[find in source code]](../../../../layeredimage/io/ora.py#L84)

```python
def saveLayer_ORA(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .ora.
