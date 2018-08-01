from numpy import matrix
from math import sin,cos,pi

def getMoveMatrix(x,y):
	'''get an matrix to move a shape along the x and y axis'''

	return matrix([
			[1,0,0],
			[0,1,0],
			[x,y,1]
		])

def getOriginTransform(point):
	'''return a matix to translate to the origin and back from point'''

	x,y=point

	to=getMoveMatrix(-x,-y)
	fro=getMoveMatrix(x,y)

	return to,fro

def getRotationMatrix(angle,point):
	'''get matrix to rotate shape angle radians around point'''

	rmatrix=matrix([
			[cos(angle),sin(angle),0],
			[-sin(angle),cos(angle),0],
			[0,0,1]
		])

	to,fro=getOriginTransform(point)
	return to*rmatrix*fro

def getScaleMatrix(height,width,centre):
	'''get matrix to multiply height of shape by height and width by width'''
	x,y=centre
	smatrix=matrix([
			[height,0,0],
			[0,width,0],
			[0,0,1]
		])

	to,fro=getOriginTransform((x,y))
	return to*smatrix*fro


class Shape:
	def __init__(self,colour,centre):
		self.colour=colour
		self.centre=matrix([centre[0],centre[1],1])

	def getCentre(self):
		'''return the 2d co-ordinates of the centre'''
		a=self.centre.tolist()[0]
		return a[0],a[1]

	def move(self,x,y):
		'''move the shape x units along the x-axis and y units along the y-axis'''
		self.centre *= getMoveMatrix(x,y)

	def rotate(self,angle):
		'''rotate shape angle radians around the shapes centre'''
		self.points *= getRotationMatrix(angle,self.getCentre())


class Polygon(Shape):
	'''a standard polygon'''
	def __init__(self,colour,*points,centre):
		'''colour is a string,points is a matrix'''
		Shape.__init__(self,colour,centre)

		self.points=[]
		for a in points:
			self.points.append([a[0],a[1],1])
		self.points=matrix(self.points)

	def __str__(self):
		returnme="<polygon fill=\"%s\" points=\"" % self.colour
		for a in self.points.tolist():
			returnme+="%.2f,%.2f " % (a[0],a[1])
		returnme+="\"/>"
		return returnme

	def move(self,x,y):
		Shape.move(self,x,y)
		self.points *= getMoveMatrix(x,y)

	def scale(self,height,width):
		'''scale the shape on the x and y axis'''
		self.points *= getScaleMatrix(height,width,self.getCentre())

class FreeShape(Shape):
	'''like a polygon but with bendier lines'''
	def __init__(self,colour,*points,centre,dpath,**dpathData):
		Shape.__init__(self,colour,centre)
		self.dpath=dpath
		self.dpathData=dpathData

		self.points=[]
		for a in points:
			self.points.append([a[0],a[1],1])
		self.points=matrix(self.points)


	def __str__(self):
		returnme1="<path fill=\"%s\" d=\"" % self.colour

		dpath=self.dpath
		for a in self.points.tolist():
			point="%.3f,%.3f" % (a[0],a[1])
			dpath=dpath.replace("%POINT%",point,1)
		for b in self.dpathData:
			dpath=dpath.replace("%"+ b +"%",str(self.dpathData[b]))

		returnme2="\"/>"

		return returnme1+dpath+returnme2

	def move(self,x,y):
		Shape.move(self,x,y)
		self.points*=getMoveMatrix(x,y)

	def scale(self,ratio):
		'''make the shape ratio times bigger'''
		self.points*=getScaleMatrix(ratio,ratio,self.getCentre())
		for a in self.dpathData:
			self.dpathData[a]*=ratio

class Circle(Shape):
	def __init__(self,colour,radius,centre):
		Shape.__init__(self,colour,centre)
		self.radius=radius

	def __str__(self):
		values=(self.colour,self.radius) + self.getCentre()
		return "<circle fill=\"%s\" r=\"%d\" cx=\"%d\" cy=\"%d\"/>" % values

	def scale(self,ratio):
		'''multiply the size of the circle by ratio'''
		self.radius *= ratio

c=FreeShape("yellow",(50,0),(100,50),(50,50),centre=(50,50),dpath="M %POINT% A %Height%,%Width% 0 0,1 %POINT% L %POINT%",Height=120,Width=200)
c.move(-25,50)
#c.scale(2)

print("<svg height=\"%d\" width=\"%d\">" % (200,200))
print(c)
print("</svg>")
