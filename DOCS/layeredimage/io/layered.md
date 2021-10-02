# layered

> Auto-generated documentation for [layeredimage.io.layered](../../../layeredimage/io/layered.py) module.

Do file io - LAYERED(C).

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../README.md#layeredimage-modules) / [layeredimage](../index.md#layeredimage) / [io](index.md#io) / layered
    - [grabLayer_LAYERED](#grablayer_layered)
    - [openLayer_LAYERED](#openlayer_layered)
    - [openLayer_LAYEREDC](#openlayer_layeredc)
    - [saveLayer_LAYERED](#savelayer_layered)
    - [saveLayer_LAYEREDC](#savelayer_layeredc)
    - [writeImage_LAYERED](#writeimage_layered)

## grabLayer_LAYERED

[[find in source code]](../../../layeredimage/io/layered.py#L83)

```python
def grabLayer_LAYERED(
    zipFile: ZipFile,
    layer: dict[(str, Any)],
    blendLookup: dict[(str, Any)],
):
```

Grab an image from .layered.

## openLayer_LAYERED

[[find in source code]](../../../layeredimage/io/layered.py#L21)

```python
def openLayer_LAYERED(file: str) -> LayeredImage:
```

Open a .layered file into a layered image.

## openLayer_LAYEREDC

[[find in source code]](../../../layeredimage/io/layered.py#L133)

```python
def openLayer_LAYEREDC(file: str) -> LayeredImage:
```

Open a .layeredc file into a layered image.

## saveLayer_LAYERED

[[find in source code]](../../../layeredimage/io/layered.py#L98)

```python
def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .layered.

## saveLayer_LAYEREDC

[[find in source code]](../../../layeredimage/io/layered.py#L138)

```python
def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layeredc image as .layered.

## writeImage_LAYERED

[[find in source code]](../../../layeredimage/io/layered.py#L121)

```python
def writeImage_LAYERED(
    image: Image.Image,
    zipFile: ZipFile,
    path: str,
    compressed: bool = False,
):
```

Write an image to the archive.
