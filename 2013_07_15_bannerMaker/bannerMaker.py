# makes banners for the travel blog... whoohoo!

import sys, os, re
import time, datetime
import getopt
import Image

OUT_DIR = "convert"

def resizeImage(files, fileDest, resultdim):
	resWidth = 0
	resHeight = 0
	for fileSrc in files:
		im = Image.open(fileSrc)
		width, height = im.size
		resWidth += width
		resHeight = height
		print fileSrc, resWidth
	result = Image.new('RGBA', (resWidth, resHeight), (0,0,0,0))
	x = 0
	for fileSrc in files:
		im = Image.open(fileSrc)
		width, height = im.size
		result.paste(im, (x, 0))
		x += width
	# we decided to not crop, better let the user crop
	#result.thumbnail(resultdim, Image.ANTIALIAS)
	result.save(fileDest, "JPEG")

# command line options: note the first line parameter and the if statements below
optlist, args = getopt.getopt(sys.argv[1:], "")
filenames = args

#output file
imgdir = os.path.dirname(filenames[0])
if imgdir == None or imgdir == "":
	imgdir = "."
outfile =  imgdir + "/combined_banner_RENAME_OR_LOSE_IT.jpg"

resizeImage(filenames, outfile, (800, 100))


