from shapes import *
from planet import *
from planetList import *
from rendersettings import *
from multiprocessing.dummy import Pool
import cairosvg

#generate svgs
print("generating frames")
svgstrings=[]
for i in range(0,frames):
	svgstring="<svg width=\"%s\" height=\"%s\" bgcolor=\"black\">\n" % (width,height)
	svgstring+=sun.__str__()+"\n"
	for planet in planetList:
		svgstring+=planet.run()
	svgstring+="</svg>"

	svgstrings.append(svgstring)

#render pngs
def renderImage(args):
	'''render the svg strings to png'''
	i,svgstring=args

	if RENDERMODE==0:
		filename="/tmp/test/file%5d.svg" % i
		filename=filename.replace(" ","0")
		print("saving frame",i)

		out=open(filename,"w+")
		out.write(svgstring)
		out.close()

	elif RENDERMODE==1:
		filename="/tmp/test/file%5d.png" % i
		filename=filename.replace(" ","0")
		print("rendering frame",i)
		cairosvg.svg2png(bytestring=svgstring.encode(),write_to=filename,scale=renderScale)

	else:
		print("invalid render mode")
		quit()

threadpool=Pool(threadnum)
threadpool.map(renderImage,zip(range(0,frames),svgstrings))
threadpool.close()
