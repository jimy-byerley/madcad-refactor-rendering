from .d3 import Scene3D
from .d2 import Scene2D

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
		''' fenetre de rendu 2d dynamique (openGl) '''
		indev


try:
	from .d2 import SceneSvg
except ImportError:
	pass
else:
	
	def blueprint(scene:dict, size=A4, view:mat4=None, **options):
		''' image de rendu  2d statique (svg) '''
		indev


def render(scene:dict, size=uvec2(400,400), view:mat4=None, projection:mat4=None, **options):
	''' image de rendu 3d statique (openGL) '''
	indev
