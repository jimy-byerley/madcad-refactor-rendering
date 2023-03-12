from .d3 import Scene3D, SubView3D
from .d2 import Scene2D, SubScene2D

try:
	from . import qt
except ImportError:
	pass
else:
	
	from .d3 import QView3D
	from .d2 import QView2D
	
	def show(scene:dict, interest:Box=None, size=uvec2(400,400), projection=None, navigation=None, **options):
		''' fenetre de rendu 3d dynamique (openGL+Qt) '''
		indev
	
	def drawing(scene:dict, view:mat4=None, **options):
		''' fenetre de rendu 2d dynamique (openGL+Qt) '''
		indev


try:
	from .svg import SceneSvg
except ImportError:
	pass
else:
	
	def blueprint(content: list, view=mat4(1), projection=mat4(1), size=A4, **options) -> Svg:
		''' image de rendu  2d statique (svg) '''
		...
		svg = Svg(some_options)
		SceneSVG(content, options).render(svg)
		return svg


def render(scene:dict, size=uvec2(400,400), view:mat4=None, projection:mat4=None, **options):
	''' image de rendu 2D/3d statique (openGL) '''
	indev
