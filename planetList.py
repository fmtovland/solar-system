from shapes import *
from planet import *

width,height=3840,2160		#internal resolution
planetList=[]

def getSunDist(dist):
	'''get a planets starting position from the distance from the sun'''
	return int(width/2),int(height/2)-dist,1

#sun
sun=Sun("yellow",100,getSunDist(0))

#mercury
mercury=Planet("white",87,87/2,5,sun,getSunDist(120))
planetList.append(mercury)
#mercury.addIsland(FreeShape("grey",(2.5,2.5,1),(-5,0,1),dpath="M %CENTRE% l %POINT% l %POINT%"))
mercury.addIsland(FreeShape("grey",
					(3,-3,1),

					(-0.7289186,-0.63019,1),
					(-2.1939827,-1.89453,1),
					(-3.0474332,-1.96075,1),
					(-1.8707536,1.81298,1),
					(-4.10800549,3.41,1),
					(-2.5749627,7.22879,1),
					(2.3843807,0.97439,1),
					(4.6852993,1.26439,1),
					(6.7563244,-0.33073,1),
					(0.4524238,-0.88031,1),
					(1.2859091,-1.90517,1),
					(0,-2.12611,1),
					(-9.09685919,-1.00435,1),
					(-3.9119129,-1.64497,1),
					(-1.1339285,-2.8112,1),
					dpath="M %CENTRE% m %POINT% c %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% z"))

#venus
venus=Planet("Purple",224,20,22,sun,getSunDist(180),clockWise=False)
planetList.append(venus)

#earth
earth=Planet("blue",365,24,25,sun,getSunDist(300))
planetList.append(earth)
earth.addIsland(FreeShape("green",(10,0,1),(3,3,1),(3,-3,1),(-3,-3,1),dpath="M %CENTRE% m %POINT% l %POINT% l %POINT% l %POINT% z"))
earth.addIsland(FreeShape("White",(5,10,1),(10,-10,1),(10,10,1),(-10,10,1),dpath="M %CENTRE% m %POINT% c %POINT% %POINT% %POINT% z"))
earth.addIsland(FreeShape("green",
			(3.6217870000000003, 3.7266,1),
			(5.9927805, 6.89365,1),
			(-2.1768825, 5.3451,1),
			(-3.7105230000000002, -2.6868,1),
			(-10.5827735, -4.9148,1),
			(-15.8277535, -0.23650000000000002,1),
			(-1.455168, -2.80335,1),
			(-7.17287445, -5.0039,1),
			(3.6616444999999995, -14.8828,1),
			(-3.7563445, 1.64935,1),
			(-10.6627487, -0.77015,1),
			(-2.126116, -8.9769,1),
			(3.477176, 4.0415,1),
			(7.472647500000001, 4.8696,1),
			(12.5204615, -0.82685,1),
			(4.5508315, 8.7447,1),
			(1.283088, 11.78395,1),
			(-5.7877605, 12.048000000000002,1),
			dpath="m %CENTRE% c %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% z"))

#earthmoon
ex,ey=earth.getCentre()
earthmoon=Planet("grey",1,27,5,earth,(ex,ey-50))
planetList.append(earthmoon)

#mars
mars=Planet("red",687,25,13,sun,getSunDist(420))
planetList.append(mars)

#mars moons
mx,my=mars.getCentre()
phobos=Planet("pink",11,1,2,mars,(mx,my-38))
planetList.append(phobos)
deimos=Planet("brown",70,1,3,mars,(mx,my-53))
planetList.append(deimos)

#jupiter
jupiter=Planet("aquamarine",10475,10,65,sun,getSunDist(700))
planetList.append(jupiter)

#moons of jupiter (oooooh boy!)
jx,jy=jupiter.getCentre()
#io
io=Planet("#B6A54B",1,42,7,jupiter,(jx,jy-90))
io.addIsland(FreeShape("#FF6600",
				(-3,2,1),

				(0.359492,-0.766,1),
				(0.784518,-0.555,1),
				(1.1960549,-0.544,1),
				(0.521177,0.846,1),
				(-0.02587,0.903,1),
				(-0.206217,1.2308,1),
				(0.648163,0.333,1),
				(0.773409,0.829,1),
				(0.824865,1.3491,1),
				(-0.137462,0.279,1),
				(-0.0576,0.782,1),
				(-0.703089,0.536,1),
				(0.222712,-0.618,1),
				(-0.24199,-0.604,1),
				(-0.534209,-0.749,1),
				(0.262228,0.874,1),
				(-0.06133,1.1422,1),
				(-0.329946,1.4675,1),
				(-0.724923,0.07,1),
				(-0.444299,-1.4224,1),
				(-1.0104602,-1.2781,1),
				(-1.0517035,-0.166,1),
				(-0.329951,-0.322,1),
				(-0.344174,-0.643,1),
				(0.149697,-0.965,1),
				(0.468952,-0.05,1),
				(0.656555,-0.06,1),
				(-0.806155,-1.5022,1),
				(0.228551,-1.0835,1),
				(0.539501,-0.766,1),

				dpath='m %CENTRE% m %POINT% c %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% l %POINT% c %POINT% %POINT% %POINT% l %POINT% %POINT% c %POINT% %POINT% %POINT% z'))

io.addIsland(FreeShape("#FF6600",
				(-3,-5,1),

				(-1.8386436,0.581,1),
				(-0.909711,1.662,1),
				(-0.518462,2.6454,1),
				(0.905769,0.417,1),
				(1.8783708,0.528,1),
				(3.0589259,-0.317,1),
				(-1.3998475,1.3756,1),
				(0.874958,0.3,1),
				(1.2366011,5.7504,1),
				(2.8515416,-1.3756,1),
				(-0.449484,-3.8112,1),
				(-2.5540932,-1.9219,1),
				(-3.9921578,-2.3282,1),
				dpath='m %CENTRE% m %POINT% c %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% l %POINT% c %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% z'))

io.addIsland(FreeShape("#FF6600",
				(4,-3,1),

				(-2.2128, 1.2008624, 1),
				( -2.6923, 6.2405444, 1),
				(0.119, 7.4414064, 1),
				( -0.967,-2.215555, 1),
				(-1.3459, -4.599093, 1),
				(-0.119, -7.4414064, 1),

				dpath='m %CENTRE% m %POINT% c %POINT% %POINT% %POINT% %POINT% %POINT% %POINT% z'))
planetList.append(io)

#europa
europa=Planet("white",1,84,6,jupiter,(jx,jy-115))
planetList.append(europa)
#ganymede
ganymede=Planet("silver",1,168,10,jupiter,(jx,jy-140))
planetList.append(ganymede)
#callisto
callisto=Planet("#527B7F",1,384,9,jupiter,(jx,jy-175))
planetList.append(callisto)

