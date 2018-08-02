from shapes import *
from copy import deepcopy

class Planet(Circle):
	'''a class to represent a planet'''
	def __init__(self,colour,year,radius,sun,centre):
		'''year is days in the planets year, sun is the celestial body it orbits around'''
		Circle.__init__(self,colour,radius,centre)
		self.year=year
		self.day=0
		self.sun=sun
		self.islands=[]

	def __str__(self):
		returnme=Circle.__str__(self)
		for l in self.islands:
			tmp=deepcopy(l)
			tmp.points*=getSimpleRotationMatrix(2*pi*(self.day/self.year))
			returnme+="\n"+tmp.__str__()
		centre="%.3f,%.3f" % self.getCentre()
		returnme=returnme.replace("%CENTRE%",centre)
		return returnme

	def addIsland(self,freeshape):
		'''add an island to the planet (as a freeshape)'''
		self.islands.append(freeshape)

	def move(self,x,y):
		'''move the shape x units along the x-axis and y units along the y-axis'''
		mm=getMoveMatrix(x,y)
		self.centre *= mm
		for i in range(0,len(self.islands)):
			self.islands[i].points*=mm

	def rotate(self,angle):
		mm=getRotationMatrix(angle,self.getCentre())
		for i in range(0,len(self.islands)):
			self.islands[i].points*=mm

	def orbit(self,angle,point):
		self.centre *= getRotationMatrix(angle,point)

	def getSunOrbitMatrix(self):
		return getRotationMatrix((2*pi)/self.year,self.sun.getCentre())

	def sunOrbit(self):
		self.sun.moonOrbit(self)
		self.centre *= self.getSunOrbitMatrix()
		self.day+=1
		self.day%=self.year

	def moonOrbit(self,moon):
		self.sun.moonOrbit(moon)
		moon.centre *= self.getSunOrbitMatrix()

class Sun(Circle):
	def moonOrbit(self,moon):
		pass
