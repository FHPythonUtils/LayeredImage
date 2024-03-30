# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2024.3 - 2024/03/30

- fix bug where dimensions auto-calculation disregards layer offsets https://github.com/FHPythonUtils/LayeredImage/issues/7

## 2024.2.1 - 2024/03/17

- use absolute imports

## 2024.2 - 2024/01/27

- bug fixes
- use new blendmodes

## 2024.1 - 2024/01/17

- update tooling
	- ruff
	- pyright
- use loguru to replace print statements
- use pathlib in place of os.path
- absolute imports in the place of relative imports
- Address “The Boolean Trap” with kw only args
- More type hints
- remove deprecated functions from `2021.2.4`

## 2024 - 2024/01/07

- update dependencies

## 2023.0.2 - 2023/12/01

- add: Using os.path.splitext() to support Path objects https://github.com/FHPythonUtils/LayeredImage/pull/6, thank you https://github.com/denilsonsa!

## 2023 - 2023/08/31

- Update deps

## 2022.0.1 2022/04/06

- Remove metprint
- Move docs

## 2022 - 2022/01/23

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update deps
- Improve save layered image to gif functionality
- Update directory structure for formal tests

## 2021.2.8 - 2021/11/07

- add pre-commit
- code quality improvements

## 2021.2.7 - 2021/10/02

- code quality improvements

## 2021.2.6 - 2021/09/13

- Update pillow

## 2021.2.4 - 2021/06/08

- Update blend.py https://github.com/FHPythonUtils/LayeredImage/issues/3
- reduce duplication with upstream libs

## 2021.2.3 - 2021/05/01

- bugfix backwards compat

## 2021.2.2 - 2021/05/01

- Updated formatting
- Deprecated 'raster' functions and replaced with more accurate naming
- Improved docs

## 2021.2.1 - 2021/03/18

- Update Pillow >= 8.1.1 due to high severity security vulnerabilities:
	- CVE-2021-27923
	- CVE-2020-35654
	- CVE-2020-35653
	- CVE-2021-27921
	- CVE-2021-27922
	- CVE-2020-35655

## 2021.2 - 2021.03.03

- Improve MI score by refactoring `layeredimage.io.py` to `layeredimage.io/`

## 2021.1.1 - 2021.03.02

- Try out new yapf formatting.
- Tidy up
- `pyupgrade`

## 2021.1 - 2021.01.20

- `pypdn` compatible with py 3.9 so added back

## 2021 - 2021.01.18

- Fix bug on python 3.7/3.8

## 2020.7 - 2020/10/29

- Using FHMake to build
- Added type hinting
- Dropped support for python < 3.7
- Added support for python 3.9
- pypdn has been dropped until it is compatible with python 3.9
- replaced `psd-tools3` with `psdtoolsx`

## 2020.6.5 - 2020/06/15

- Fix ora write bug causing the layers to be inverted (monkey patch)

## 2020.6.4 - 2020/05/14

- Fix png minifier for layeredc
- Fix fatal read xcf bug (upstream)
- Update pyora (security benefits and removal of save fix)

## 2020.6.3 - 2020/05/13

- Fix bug due to spelling error

## 2020.6.2 - 2020/05/10

- Removed redundant function
- File extensions can now be case-insensitive

## 2020.6.1 - 2020/05/08

- Minor change to stack.json for .layered (no longer minified)
- Added .layeredc that will attempt to optimize the image. Savings of 10 - 20%

## 2020.6 - 2020/05/08

- Added .layered image spec and implementation to store blendmodes that are
	not supported by ora and some other formats that this lib can write too.
	Still, use ora whenever possible as this is a more supported image format.
- Updates to `gimpformats` mean that visibility is now correctly preserved.
- Optimizations to save functions
- Added json functions to get data as a dictionary

## 2020.5.6 - 2020/05/06

- Updated classifiers

## 2020.5.5 - 2020/05/03

- Upgraded from `gimpformats_unofficial` to `gimpformats`
- Disable some pylint errors for snippets

## 2020.5.4 - 2020/05/02

- Bugfix openLayer_XCF: layer offsets in a group are now correct

## 2020.5.3 - 2020/05/02

- Added full support for Open Raster Image blend modes

## 2020.5.2 - 2020/05/01

- Added PINLIGHT, VIVIDLIGHT, EXCLUSION
- Moved blending heavy lifting to a shiny new library

## 2020.5.1 - 2020/04/29

- Added blend modes from pyora (credited in file docstring): GRAINEXTRACT,
GRAINMERGE, DIVIDE, HUE, SATURATION, COLOUR, LUMINOSITY

## 2020.5 - 2020/04/28

- Added LSR support
- Added make.py
- Bugfix pdn layer offset in group
- Print more descriptive LayerImage
- Bugfixes to flattenLayerOrGroup

## 2020.4.2 - 2020/04/27

- Update documentation (again) using pydoc-markdown 3

## 2020.4.1 - 2020/04/26

- Update documentation

## 2020.4 - 2020/04/26

- Added GIF and WEBP support
- Automate tests

## 2020.3.3 - 2020/04/25

- Updated blend.py to map blend types to functions, rather than use a series of
if statements

## 2020.3.2 - 2020/04/24

- Modules are no longer optional as this will create excess crashes for what is
four additional dependencies

## 2020.3.1 - 2020/04/24

- Fix ResourceWarning when opening a file

## 2020.3 - 2020/04/24

- Fixed bug that caused hidden layers to be rendered by default
- Using pypdn 1.05 - PDNs work again on python 3.8

## 2020.2.1 - 2020/04/24

- Fixed incorrect docstrings
- Added SOFTLIGHT and HARDLIGHT

## 2020.2 - 2020/04/23

- Added basic support for blend modes NORMAL, MULTIPLY, ADDITIVE, COLOURBURN,
COLOURDODGE, REFLECT, GLOW, OVERLAY, DIFFERENCE, NEGATION, LIGHTEN, DARKEN,
SCREEN, XOR
- Python 3.5 is no longer supported

## 2020.1.1 - 2020/04/22

- Export to a flat image
- Bugfix: If the file does not exist throws an error instead of exiting

## 2020.1 - 2020/04/22

- Added TIFF support 🎉
- Discovered that my patch for `pypdn` cannot be applied so throw an error and
message for python 3.8+ (waiting on upstream) 😭 - Therefore no test output for
these
- Better error for unrecognised extension
- Fixes to saving .ora files.
	- Groups are saved with an offset rather than relying on `project.add_layer()`.
	- Fixed `save_ORA_fix` to save images without additional padding
- Updates to README
- `LayeredImage.extractLayers` will now 'raster' layers in a group to deal with
offsets, dimensions etc

## 2020 - 2020/04/20

- First release
