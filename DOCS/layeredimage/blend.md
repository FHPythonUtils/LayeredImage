# blend

> Auto-generated documentation for [layeredimage.blend](../../layeredimage/blend.py) module.

Provide blending functions

- [Layeredimage](../README.md#layeredimage-index) / [Modules](../README.md#layeredimage-modules) / [layeredimage](index.md#layeredimage) / blend
    - [BlendType](#blendtype)
    - [blendLayers](#blendlayers)

leverage blendmodes for this

## BlendType

[[find in source code]](../../layeredimage/blend.py#L10)

```python
class BlendType(Enum):
```

Specify supported blend types
NORMAL
MULTIPLY
ADDITIVE
COLOURBURN
COLOURDODGE
REFLECT
GLOW
OVERLAY
DIFFERENCE
NEGATION
LIGHTEN
DARKEN
SCREEN
XOR
SOFTLIGHT
HARDLIGHT
GRAINEXTRACT
GRAINMERGE
DIVIDE
HUE
SATURATION
COLOUR
LUMINOSITY
PINLIGHT
VIVIDLIGHT
EXCLUSION
DESTIN
DESTOUT
DESTATOP
SRCATOP

## blendLayers

[[find in source code]](../../layeredimage/blend.py#L75)

```python
def blendLayers(
    background: Image,
    foreground: Image,
    blendType: BlendType,
    opacity: float,
):
```

Blend layers using numpy array

#### Arguments

- `background` *PIL.Image* - background layer
- `foreground` *PIL.Image* - foreground layer
- `blendType` *BlendType* - The blendtype
- `opacity` *float* - The opacity of the foreground image

#### Returns

- `PIL.Image` - combined image

#### See also

- [BlendType](#blendtype)
