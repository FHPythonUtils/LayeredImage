# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

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
