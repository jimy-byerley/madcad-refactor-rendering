from svgwrite import ...

class SceneSVG:
	''' a static scene that renders to SVG file format 
		As this scene is static, it does not need a view to be rendered and all the viewing parameters are given at the scene creation
	'''
	overrides = {}
	options: dict
	stack: list
	
	def __init__(self, scene, view=mat4(1), projection=mat4(1), **options):
		...
	
	def render(self, svg):
		svg = SVG()
		# buffer faces to hide polygon lines
		positionmap = ...
		for item in self.stack:
			if isinstance(item, Face3D):
				# buffer faces into positionmap
				...
		# filter edges in Polygons3Ds
		for item in self.stack:
			if isinstance(item, Polygon3D):
				# create new Polygon3Ds by removing hidden edges
				# if edge in positionmap
				  # check for intersection
			      # if intersection, remove edge
				...
		
		# append items in document
		for item in sorted(self.stack):
			svg.append(item)
		return svg
		
	def display(self, displayable):  ...
		''' create a display for this scene out of a displayable. 
			the displayable must be compatible with this type of scene.
			this method must be called by subdisplays to create a display object from a source object, a function choosing to call displayable.display() directly instead has to manage overrides on its own
		'''
		
class SubSceneSVG:
	options: dict
	stack: list
	
	def __init__(self, scene, view=mat4(1), projection=mat4(1), **options):
		...
	def display(self, scene):
		...

def blueprint(content: list, view=mat4(1), projection=mat4(1), **options) -> Svg:
	''' create a SVG document out of a 2D scene made of SVG elements '''
	...
	svg = Svg(some_options)
	SceneSVG(content, options).render(svg)
	return svg
	
	

# these are just examples to illustrate
	
# how a displayable must implement display
class ExampleDisplayable:
	def display(self, scene):
		if isinstance(scene, SceneSVG):
			# must return an iterable of couples
			return [
				# each couple is (render priority, svg element)
				# the priority will sort the elements in the final SVG
				(1, Polygon3D(typedlist[vec3], color="...", line=...)),
				(1, Face3D(typedlist[vec3], typedlist[uvec3], color="#...")),
				(2, svgwrite.Text(...)),
				]

def example_usage():
	# a bug blueprint
	blueprint([
		# with a first view of the assembly
		SubSceneSVG([
			somemesh,
			someother,
			], 
			center=vec2(0.5,0.1),
			scale=1/3, 
			cut=union(plane(Axis(O,Z),100), cutmesh), 
			display_scale=True, 
			display_wireframe=True, 
			display_annotations=True,
			),
		# a second view with different parameters
		SubSceneSVG([
			somemesh,
			], 
			center=vec2(0.5, 0),
			scale=1/2,
			)
		# a blueprint frame around with a table
		SvgFrame(author="coucou"),
		]).write('somefile.svg')

