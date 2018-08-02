from shapes import *
from planet import *


#width,height=3840,2160
#width,height=500000,500000
width,height=1000,1000
frames=365*24
#frames=1

def getSunDist(dist):
	'''get a planets starting position from the distance from the sun'''
	return int(width/2),int(height/2)-dist


#sun
sun=Sun("yellow",100,getSunDist(0))

#mercury
mercury=Planet("white",87,2/3,5,sun,getSunDist(120))
mercury.addIsland(FreeShape("grey",(2.5,2.5),(-5,0),dpath="M %CENTRE% l %POINT% l %POINT%"))

#venus
venus=Planet("Purple",224,1/2,22,sun,getSunDist(180),clockWise=False)

#earth
earth=Planet("blue",365,24,25,sun,getSunDist(300))
earth.addIsland(FreeShape("green",(10,10),(-30,0),(10,-30),dpath="M %CENTRE% m %POINT% l %POINT% l %POINT%"))
ex,ey=earth.getCentre()
earthmoon=Planet("grey",1,27,5,earth,(ex,ey-50))

for i in range(0,frames):
	filename="/tmp/test/file%5d.svg" % i
	filename=filename.replace(" ","0")
	out=open(filename,"w+")

	out.write("<svg width=\"%s\" height=\"%s\" bgcolor=\"black\">" % (width,height))
	out.write(sun.__str__())
	out.write(mercury.__str__())
	out.write(venus.__str__())
	out.write(earth.__str__())
	out.write(earthmoon.__str__())
	out.write("</svg>")
	out.close()

	mercury.sunOrbit()
	venus.sunOrbit()
	earth.sunOrbit()
	earthmoon.sunOrbit()
