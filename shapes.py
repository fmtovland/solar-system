from numpy import matrix
from math import sin,cos,pi

def makePoints2D(shape):
	returnme=[]
	for point in shape.tolist():
		returnme.append((point[0],point[1]))
	if len(returnme) == 1:
		return returnme[0]
	else:
		return tuple(returnme)

def getMoveMatrix(x,y):
	'''get an matrix to move a shape along the x and y axis'''

	return matrix([
			[1,0,0],
			[0,1,0],
			[x,y,1]
		])

def getOriginTransform(point):
	'''return a matix to translate to the origin and back from point'''

	x,y=makePoints2D(point)

	to=getMoveMatrix(-x,-y)
	fro=getMoveMatrix(x,y)

	return to,fro

def getRotationMatrix(angle,point):
	'''get matrix to rotate shape angle radians around point'''

	rmatrix=getSimpleRotationMatrix(angle)

	to,fro=getOriginTransform(point)
	return to*rmatrix*fro

def getSimpleRotationMatrix(angle):
	return matrix([
			[cos(angle),sin(angle),0],
			[-sin(angle),cos(angle),0],
			[0,0,1]
		])

def getScaleMatrix(ratio,centre):
	'''generate a matrix to make a shape ratio times bigger'''
	smatrix=matrix([
			[ratio,0,0],
			[0,ratio,0],
			[0,0,1]
		])

	to,fro=getOriginTransform(centre)
	return to*smatrix*fro


class Shape:
	def __init__(self,colour):
		self.colour=colour

	def getCentre(self):
		'''return the 2d co-ordinates of the centre'''
		return makePoints2D(self.centre)

	def setColour(self,colour):
		self.colour=colour

	def move(self,x,y):
		'''move the shape x units along the x-axis and y units along the y-axis'''
		self.centre *= getMoveMatrix(x,y)

	def orbit(self,angle,point):
		'''rotate the shape around a point'''
		self.centre*=getRotationMatrix(angle,point)



class Polygon(Shape):
	'''a standard polygon'''
	def __init__(self,colour,*points):
		'''colour is a string,points is a matrix'''
		Shape.__init__(self,colour)

		self.points=[]
		tx,ty,tz=0,0,0
		for a in points:
			self.points.append([a[0],a[1],a[2]])
			tx+=a[0]
			ty+=a[1]
			tz+=a[2]
		self.points=matrix(self.points)
		poino=len(points)
		self.centre=matrix([tx/poino,ty/poino,tz/poino])

	def __str__(self):
		returnme="<polygon fill=\"%s\" points=\"" % self.colour
		for a in self.points.tolist():
			returnme+="%.2f,%.2f " % makePoints2D(a)
		returnme+="\"/>"
		return returnme

	def move(self,x,y):
		mm=getMoveMatrix(x,y)
		self.points *= mm
		self.centre *= mm

	def scale(self,ratio):
		'''scale the shape on the x and y axis'''
		self.points *= getScaleMatrix(ratio,self.centre)

	def rotate(self,angle):
		'''rotate shape angle radians around the shapes centre'''
		self.points *= getRotationMatrix(angle,self.centre)

	def orbit(self,angle,point):
		'''rotate a shape around another'''
		mm = getRotationMatrix(angle,point)
		self.centre *= mm
		self.points *= mm

class FreeShape(Polygon):
	'''like a polygon but with bendier lines'''
	def __init__(self,colour,*points,dpath,**dpathData):
		Polygon.__init__(self,colour,*points)
		self.dpath=dpath
		self.dpathData=dpathData


	def __str__(self):
		returnme1="<path fill=\"%s\" d=\"" % self.colour

		dpath=self.dpath
		for a in self.points:
			point="%.3f,%.3f" % makePoints2D(a)
			dpath=dpath.replace("%POINT%",point,1)
		for b in self.dpathData:
			dpath=dpath.replace("%"+ b +"%",str(self.dpathData[b]))

		returnme2="\" />"

		return returnme1+dpath+returnme2

	def scale(self,ratio):
		'''make the shape ratio times bigger'''
		self.points*=getScaleMatrix(ratio,self.getCentre())
		for a in self.dpathData:
			self.dpathData[a]*=ratio

class Circle(Shape):
	def __init__(self,colour,radius,centre):
		Shape.__init__(self,colour)
		self.radius=radius
		self.centre=matrix([centre[0],centre[1],1])

	def __str__(self):
		values=(self.colour,self.radius) + self.getCentre()
		return "<circle fill=\"%s\" r=\"%.3f\" cx=\"%.3f\" cy=\"%.3f\"/>" % values

	def scale(self,ratio):
		'''multiply the size of the circle by ratio'''
		self.radius *= ratio
