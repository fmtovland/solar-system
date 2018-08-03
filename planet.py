from shapes import *
from copy import deepcopy
try:
	from __main__ import FRAMESKIP
except ImportError:
	FRAMESKIP=1

class Planet(Circle):
	'''a class to represent a planet'''
	def __init__(self,colour,year,hoursPerDay,radius,sun,centre,clockWise=True):
		'''year is days in the planets year, sun is the celestial body it orbits around'''
		Circle.__init__(self,colour,radius,centre)
		self.sun=sun
		self.year=year*hoursPerDay
		self.day=0
		self.hoursPerDay=hoursPerDay
		self.hours=0
		self.clockWise=clockWise	#which direction the planet rotates around it's sun
		self.islands=[]

	def __str__(self):
		tmp=deepcopy(self)
		tmp.centre *= self.getSunOrbitMatrix()
		self.sun.moonOrbit(tmp)
		returnme=Circle.__str__(tmp)
		for l in tmp.islands:
			l.points*=getSimpleRotationMatrix(2*pi*(self.hours/self.hoursPerDay))
			returnme+="\n"+l.__str__()
		centre="%.3f,%.3f" % tmp.getCentre()
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
		mm=getRotationMatrix(angle,self.centre)
		for i in range(0,len(self.islands)):
			self.islands[i].points*=mm

	def orbit(self,angle,point):
		self.centre *= getRotationMatrix(angle,point)

	def getSunOrbitMatrix(self):
		return getRotationMatrix(FRAMESKIP*(2*pi)*(self.day/self.year),self.sun.centre)

	def sunOrbit(self):
		if self.clockWise:
			self.day+=1
			self.hours+=1
		else:
			self.day-=1
			self.hours-=1

		self.day%=self.year
		self.hours%=self.hoursPerDay

	def moonOrbit(self,moon):
		self.sun.moonOrbit(moon)
		moon.centre *= self.getSunOrbitMatrix()

	def run(self):
		'''execute one frame of the programs logic'''
		self.sunOrbit()
		return self.__str__()+"\n"

class Sun(Circle):
	def moonOrbit(self,moon):
		pass
