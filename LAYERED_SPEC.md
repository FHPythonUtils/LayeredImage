# .layered
.layered is highly inspired by the open raster format and aims to provide an
exchange format in the cases when saving in ora would cause unacceptable data
loss. .layered has been designed so that if the format became deprecated and no
readers existed for it tomorrow, the data would be easily salvageable.


## Rationale
.ora is sufficient for the vast majority of layered images that are represented
by this library and should be used where possible. However, some blending
functions that are present in other formats such as xcf and psd are unable to
be stored in .ora. Meaning that yet another file format is required.

Ora supports the following blend modes:
```none
NORMAL
MULTIPLY
COLOURBURN
COLOURDODGE
REFLECT
OVERLAY
DIFFERENCE
LIGHTEN
DARKEN
SCREEN
HARDLIGHT
SOFTLIGHT
HUE
SATURATION
COLOUR
LUMINOSITY
ADDITIVE
DESTIN
DESTOUT
DESTATOP
SRCATOP
```

## When to use .layered
Ideally .layered should only be used when it is not possible to store the
layered image in another format that is more readily exchangeable due to
unacceptable data loss. .layered has been designed so that if the format
became deprecated and no readers existed for it tomorrow, the data would be
easily salvageable.

As previously stated it is far better to use ora whenever possible

However, if you make use of the following blendmodes .layered is preferable

```none
GLOW
NEGATION
XOR
GRAINEXTRACT
GRAINMERGE
DIVIDE
PINLIGHT
VIVIDLIGHT
EXCLUSION
```

## Advantages
.layered is able to store blend modes that cannot be stored in an open raster
image or other formats.

## Drawbacks
This is another format in a sea of formats and is only recommended to be used
where it is not possible to use another format for this reason. Graphics editor
support for .layered is unlikely unless this became an extremely popular format
which given the existence of ora isn't very likely.

## Versions
From 2020.2 to 2020.6 the only changes in the layered image object has been the
addition of more blending modes. Other elements have remained the same (2020.2
added blend modes and so there was a change to support these). Therefore,
aside from the potential for more blend modes to be added in the future, this
spec shouldn't change

### 2020


## Structure
Based very heavily upon the open raster specification. A .layered file is
basically a zip file containing data on the layers and groups such as the name,
offsets, the images stored as png and a composite image that can be extracted
by file managers/ viewers.

```none
example.layered
 ├ stack.json
 ├ data/
 │  └ [image data files referenced by stack.json, typically [layername].png]
 ├ thumbnail.png
 └ composite.png
```

## Required files
The files except for composite.png are required though composite.png is
highly recommended to be included

### stack.json
stack.json contains all text data on a layer or group such as the name,
dimensions and offsets.

#### Why json?
Json has been used as it is supported as part of a core python installation.
A large number of json parsers are available. It is used by the likes of
GraphQl. It's good enough for Apple LSR.

### data/\[layername\].png
Layer image data should be stored here.

## Optional files
### composite.png
Composite image that can be extracted by file managers/ viewers. This must
be representative of the .layered image for example hidden layers are not shown
as part of this image.
### thumbnail.png
Composite image that can be extracted by file managers/ viewers. This must
be representative of the .layered image for example hidden layers are not shown
as part of this image and have a maximum size of 256x256 pixels.

## Comparison to ORA

Here is a snippet of the ora spec for the structure:

```none
example.ora  [considered as a folder-like object]
 ├ mimetype
 ├ stack.xml
 ├ data/
 │  ├ [image data files referenced by stack.xml, typically layer*.png]
 │  └ [other data files, indexed elsewhere]
 ├ Thumbnails/
 │  └ thumbnail.png
 └ mergedimage.png
```

### Similarities
The file format is essentially a list of images, a composite image and a file
containing information on the layers and groups (name, size, offsets)

### Differences
.layered lacks the mimetype. This is because the file type can
and should be determined from the extension for .layered

Layers are identified by the layer name: eg a layer called 'example layer' would
have an image named 'example layer.png'.

Json is used instead of xml.

The thumbnail is in the root directory as multiple thumbnails are not planned.


## Stack data

### Image
```none
dimensions: (int, int)
layersAndGroups: [layer|group]
```

### Group
```none
name: string
offsets: (int, int)
opacity: float
visible: float
dimensions: (int, int)
type: GROUP
blendmode: BlendTypes.[]
layers: [layer]
```

### Layer
```none
name: string
offsets: (int, int)
opacity: float
visible: float
dimensions: (int, int)
type: LAYER
blendmode: BlendTypes.[]
image: PIL.Image
```

Consider an image that has the following structure:

Bottom layer
```none
Group ("group_0")
	Layer("layer_0")
	Layer("layer_1")
Layer("layer_2")
```
Top Layer

The stack.json would look something like this:

```none
{"dimensions": [640, 640], "layersAndGroups": [
	{"name": "group_0", "offsets": [0, 0], "opacity": 1.0, "visible": true,
	"dimensions": [640, 640], "type": "GROUP", "blendmode": "NORMAL",
	"layers": [
		{"name": "layer_0", "offsets": [100, 0], "opacity": 1.0, "visible": true,
		"dimensions": [640, 640], "type": "LAYER", "blendmode": "NORMAL"},
		{"name": "layer_1", "offsets": [100, 0], "opacity": 1.0, "visible": true,
		"dimensions": [640, 640], "type": "LAYER", "blendmode": "NORMAL"}
	]},
	{"name": "layer_2", "offsets": [295, 292], "opacity": 1.0, "visible": false,
	"dimensions": [250, 250], "type": "LAYER", "blendmode": "NORMAL"}]}
```
