Module layeredimage.blend
=========================
Provide blending functions

leverage blendmodes for this

Functions
---------

    
`blendLayers(background, foreground, blendType, opacity)`
:   Blend layers using numpy array
    
    Args:
            background (PIL.Image): background layer
            foreground (PIL.Image): foreground layer
            blendType (BlendType): The blendtype
            opacity (float): The opacity of the foreground image
    
    Returns:
            PIL.Image: combined image

Classes
-------

`BlendType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Specify supported blend types
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

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `ADDITIVE`
    :

    `COLOUR`
    :

    `COLOURBURN`
    :

    `COLOURDODGE`
    :

    `DARKEN`
    :

    `DESTATOP`
    :

    `DESTIN`
    :

    `DESTOUT`
    :

    `DIFFERENCE`
    :

    `DIVIDE`
    :

    `EXCLUSION`
    :

    `GLOW`
    :

    `GRAINEXTRACT`
    :

    `GRAINMERGE`
    :

    `HARDLIGHT`
    :

    `HUE`
    :

    `LIGHTEN`
    :

    `LUMINOSITY`
    :

    `MULTIPLY`
    :

    `NEGATION`
    :

    `NORMAL`
    :

    `OVERLAY`
    :

    `PINLIGHT`
    :

    `REFLECT`
    :

    `SATURATION`
    :

    `SCREEN`
    :

    `SOFTLIGHT`
    :

    `SRCATOP`
    :

    `VIVIDLIGHT`
    :

    `XOR`
    :