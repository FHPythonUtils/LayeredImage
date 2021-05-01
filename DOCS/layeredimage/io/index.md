# io

> Auto-generated documentation for [layeredimage.io](../../../layeredimage/io/__init__.py) module.

Do file io.

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../README.md#layeredimage-modules) / [layeredimage](../index.md#layeredimage) / io
    - [exportFlatImage](#exportflatimage)
    - [extNotRecognised](#extnotrecognised)
    - [openLayerImage](#openlayerimage)
    - [saveLayerImage](#savelayerimage)
    - Modules
        - [common](common.md#common)
        - [gif](gif.md#gif)
        - [layered](layered.md#layered)
        - [lsr](lsr.md#lsr)
        - [ora](ora.md#ora)
        - [pdn](pdn.md#pdn)
        - [psd](psd.md#psd)
        - [tiff](tiff.md#tiff)
        - [webp](webp.md#webp)
        - [xcf](xcf.md#xcf)

## exportFlatImage

[[find in source code]](../../../layeredimage/io/__init__.py#L100)

```python
def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Export the layered image to a unilayer image file.

## extNotRecognised

[[find in source code]](../../../layeredimage/io/__init__.py#L21)

```python
def extNotRecognised(fileName: str):
```

Output the file extension not recognised error.

## openLayerImage

[[find in source code]](../../../layeredimage/io/__init__.py#L31)

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

[[find in source code]](../../../layeredimage/io/__init__.py#L67)

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
