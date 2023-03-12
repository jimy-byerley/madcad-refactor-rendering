from .base import *

			
class Scene2D(Scene):
	''' scene for 2D objects, with display overrides for 2D objects '''
	overrides = {}

	
class SubView2D(SubView):
	''' a specialized SubView adding few methods specific to 2D '''
	def __init__(self, scene, navigation=None, projection=mat3(), **options):
		...
	
	def adjust(self, box:Box=None):  ...
	def center(self, center:fvec2=None):   ...
	
	
class Offscreen2D(Offscreen):
	''' a specialized Offscreen adding few methods specific to 2D '''
	def __init__(self, scene, scene, navigation=None, projection=mat3(), **options):
		...
	
	def adjust(self, box:Box=None):  ...
	def center(self, center:fvec2=None):   ...

	def render(self):    ...


try:
	from .qt import *
except ImportError: pass
else:

	class QView2D(QOpenGLWidget):
		''' onscreen rendering using a QOpenGLWidget '''
		def __init__(self, scene, scene, navigation=None, **options):
			...
		
		def adjust(self, box:Box=None):  ...
		def center(self, center:fvec2=None):   ...
		
		def inputEvent(self, event):   ...
