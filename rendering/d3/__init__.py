from .base import *


class Scene3D(Scene):
	''' scene for 3D objects, with display overrides for 3D objects '''
	overrides = {}


class SubView3D(SubView):
	''' a specialized SubView adding few methods specific to 3D '''
	def __init__(self, scene, navigation=None, projection=None, **options):
		...
	
	def look(self, position:fvec3=None):	...
	def adjust(self, box:Box=None):  ...
	def center(self, center:fvec3=None):   ...


class Offscreen3D(Offscreen):
	''' a specialized Offscreen adding few methods specific to 3D '''
	def __init__(self, scene, scene, navigation=None, projection=None, **options):
		...
	
	def look(self, position:fvec3=None):	...
	def adjust(self, box:Box=None):  ...
	def center(self, center:fvec3=None):   ...

	def render(self):    ...


try:
	from .qt import *
except ImportError: pass
else:

	class QView3D(QOpenGLWidget):
		''' onscreen rendering using a QOpenGLWidget '''
		def __init__(self, scene, scene, projection=None, navigation=None, **options):
			...
		
		def look(self, position:fvec3=None):	...
		def adjust(self, box:Box=None):  ...
		def center(self, center:fvec3=None):   ...
		
		def inputEvent(self, event):   ...
	

