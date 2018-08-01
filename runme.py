from shapes import *
from planet import *

width,height=500,500
centre=width/2,height/2
frames=100

sun=Circle("yellow",50,centre)
earth=Planet("blue",pi/3,30,sun,(centre[0],centre[1]-170))
earth.addIsland(FreeShape("green",(10,10),(-30,0),(10,-30),dpath="M %POINT% L %POINT% L %POINT%"))
earth.sunOrbit()

for i in range(0,1):
	filename="file%3d.svg" % i
	filename=filename.replace(" ","0")
	out=open(filename,"w+")	

	out.write("<svg width=\"%s\" height=\"%s\">" % (width,height))
	out.write(sun.__str__())
	out.write(earth.__str__())
	out.write("</svg>")
	out.close()
