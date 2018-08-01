from shapes import *
from planet import *

width,height=500,500
centre=int(width/2),int(height/2)
frames=999

sun=Circle("yellow",50,centre)
earth=Planet("blue",150,30,sun,(centre[0],centre[1]-170))
earth.addIsland(FreeShape("green",(10,10),(-30,0),(10,-30),dpath="M %CENTRE% m %POINT% l %POINT% l %POINT%"))

for i in range(0,frames):
	filename="file%4d.svg" % i
	filename=filename.replace(" ","0")
	out=open(filename,"w+")	

	out.write("<svg width=\"%s\" height=\"%s\">" % (width,height))
	out.write(sun.__str__())
	out.write(earth.__str__())
	out.write("</svg>")
	out.close()

	earth.sunOrbit()
