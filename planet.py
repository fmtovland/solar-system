from shapes import *

class Planet(Circle):
	'''a class to represent a planet'''
	def __init__(self,colour,speed,radius,sun,centre):
		'''speed is % of a orbit, sun is the celestial body it orbits around'''
		Circle.__init__(self,colour,radius,centre)
		self.speed=speed
		self.sun=sun.getCentre()
		self.islands=[]

	def __str__(self):
		returnme=Circle.__str__(self)
		for l in self.islands:
			returnme+="\n"+l.__str__()
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

	def sunOrbit(self,fps):
		self.orbit(self.speed/fps,self.sun)
