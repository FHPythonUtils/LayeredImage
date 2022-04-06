# Io

> Auto-generated documentation for [layeredimage.io](../../../../layeredimage/io/__init__.py) module.

Do file io.

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../MODULES.md#layeredimage-modules) / [Layeredimage](../index.md#layeredimage) / Io
    - [exportFlatImage](#exportflatimage)
    - [extNotRecognised](#extnotrecognised)
    - [openLayerImage](#openlayerimage)
    - [saveLayerImage](#savelayerimage)
    - Modules
        - [Common](common.md#common)
        - [Gif](gif.md#gif)
        - [Layered](layered.md#layered)
        - [Lsr](lsr.md#lsr)
        - [Ora](ora.md#ora)
        - [Pdn](pdn.md#pdn)
        - [Psd](psd.md#psd)
        - [Tiff](tiff.md#tiff)
        - [Webp](webp.md#webp)
        - [Xcf](xcf.md#xcf)

## exportFlatImage

[[find in source code]](../../../../layeredimage/io/__init__.py#L101)

```python
def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Export the layered image to a unilayer image file.

## extNotRecognised

[[find in source code]](../../../../layeredimage/io/__init__.py#L23)

```python
def extNotRecognised(fileName: str):
```

Output the file extension not recognised error.

## openLayerImage

[[find in source code]](../../../../layeredimage/io/__init__.py#L32)

```python
def openLayerImage(file: str) -> LayeredImage:
```

Open a layer image file into a layer image object.

#### Arguments

- `file` *str* - path/ filename

#### Raises

- `FileExistsError` - If the layered image does not exist
- `ValueError` - If the extention is not recognised

#### Returns

- `LayeredImage` - a layered image object

## saveLayerImage

[[find in source code]](../../../../layeredimage/io/__init__.py#L68)

```python
def saveLayerImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image to a file.

#### Arguments

- `fileName` *str* - path/ filename
- `layeredImage` *LayeredImage* - the layered image to save

#### Raises

- `ValueError` - If the extention is not recognised

#### Returns

None
