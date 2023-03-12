# refactoring of `pymadcad.rendering`

This repository is only a skeleton for possible evolutions of the madcad rendering pipeline, This should be a guideline but the features proposed here may not all land in pymadcad.

## features 

features are checked if implemented in [pymadcad](https://github.com/jimy-byerley/pymadcad)

- [x] 3D openGL rendering (dynamic)
	
- [ ] 2D blueprint rendering (static)

	+ [ ] SVG
	+ [ ] PDF
	+ [ ] handling occlusion of parts by others
	+ [ ] handling annotations
	
- [ ] 2D openGL rendering (dynamic)

- [ ] make Qt and openGL optional dependencies for pymadcad ([#71](https://github.com/jimy-byerley/pymadcad/issues/71))

	So users can install pymadcad and use it only for geometric computations without the burden of Qt and openGL installations and compatiblity
	
- [ ] instanced openGL rendering

	Allowing to render a scene with 100x the same parts without using more memory and openGL calls
