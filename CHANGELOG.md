# Changelog

## \[0.1.4] - 2025-09-15

### Added

* Introduced `BuilderMixin` to separate rendering logic from the Model.
* Added `build_img(forms)` method to generate images using `PillowMotor`.
* Added `build_pdf()` and `build_gif()` placeholder methods for future PDF/GIF generation.
* Added `ImageBuild` for handling multiple images:
  * `to_images()` → returns a list of PIL images.
  * `to_image()` → returns a single image, raises error if multiple exist.
  * `to_bytes(page=None)` → convert images to bytes.
  * `save(path)` → save images to PNG or PDF depending on path.
  * `show(page=None)` → preview images in default web browser.
* Enhanced `Page` with methods to set width, height, dimension, and background.
* Enhanced `Component` layer with robust getters and setters for `Text` and `Img`.
* Added `get_component(name)` factory function and `COMPONENTS` type alias.
* `Model` now separates page and field logic from rendering; `.render()` is deprecated in favor of `BuilderMixin` methods.
* Added JSON persistence methods: `export(path)` and `load(path)`.

### Fixed

* Fixed internal handling of multiple pages when generating images.
* Improved validation in component setters (`Text` and `Img`).
* Ensured `_make()` correctly maps form values to fields and handles missing keys with errors.

## [0.1.3] - 2025-09-12
### Added
- Documentation updated in **Portuguese (PT-BR)** and **English (EN)** (full README, quickstart, and contribution guide).
- Ready-to-use examples in `examples/` (e.g., basic badge generation).
- Automated test suite (unittest/pytest) covering `Model`, `Builder`, `engines/pillow`, and `build_results`.
- Instructions for running tests and suggestions for CI and `pytest.ini`.

### Changed
- `Model._pages`: removed mutable default; now uses `default_factory=dict` (or equivalent) to avoid sharing between instances.
- `Model.get_form()`: iteration fixed to loop over `Page` objects / their fields (instead of iterating dict keys).
- `Builder`: improved error messages and clearer integration with engines (better handling of `engine.build_result()` return).
- `BuildResult`: behavior of `to_bytes()` documented/clarified; `save()` improved for file paths vs directories and multi-page handling.

### Fixed
- Pillow Engine:
  - Opens images with `Image.open(...).convert("RGBA")` to ensure consistent modes.
  - Uses `paste(..., mask=...)` when needed to preserve alpha/transparency.
  - Font fallback fixed (do not use `ImageFont.load_default(size=...)`; ensure valid fallback).
- Avoid exceptions with empty messages; error messages are now descriptive.
- Various robustness fixes (dimension/background validation in `PillowMotor.new_page`, handling empty inputs in `ImageBuildResult`).

### Documentation & Tests
- Bilingual README (PT/EN) with quickstart, API summary, and best practices.
- Tests added with execution instructions (`pytest` / `python -m unittest`).
- Examples demonstrating `render().show()`, `save()` (file and directory), and multi-page export.

### Notes
- No breaking changes expected for end-users; some internal improvements may affect serialization/instances if you relied on `_pages` as a mutable reference attribute.

## [0.1.2] - 2025-09-11
### Fixed
- Bug fixes

## [0.1.1] - 2025-09-11
### Added
- Adjustment when building a form from the model
- Builder capable of creating images with Pillow or PDFs with ReportLib
- Added `CHANGELOG.md`.

### Fixed
- Fix in component getters and setters
- Renamed `add_field` to `add_component`

## [0.1.0] - 2025-09-10
### Added
- First published version of the library.
