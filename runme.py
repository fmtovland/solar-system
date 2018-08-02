from shapes import *
from planet import *

#width,height=3840,2160
width,height=500,500
centre=int(width/2),int(height/2)
frames=500

sun=Sun("yellow",50,centre)
earth=Planet("blue",365,24,30,sun,(centre[0],centre[1]-170))
earth.addIsland(FreeShape("green",(10,10),(-30,0),(10,-30),dpath="M %CENTRE% m %POINT% l %POINT% l %POINT%"))
ex,ey=earth.getCentre()
moon=Planet("grey",27,27,5,earth,(ex,ey-50))
#moon.addIsland(FreeShape("red",(2.5,2.5),(-5,0),dpath="M %CENTRE% l %POINT% l %POINT%"))

for i in range(0,frames):
	filename="/tmp/test/file%3d.svg" % i
	filename=filename.replace(" ","0")
	out=open(filename,"w+")

	out.write("<svg width=\"%s\" height=\"%s\" bgcolor=\"black\">" % (width,height))
	out.write(sun.__str__())
	out.write(earth.__str__())
	out.write(moon.__str__())
	out.write("</svg>")
	out.close()

	earth.sunOrbit()
	moon.sunOrbit()
