# **MODE OF USE**: Drag folder into me
#
# Creates a "convert" folder within and creates new w/4 for all images

import sys, os, re
import time, datetime
import getopt
from PIL import Image

OUT_DIR = "convert"

def resizeImage(fileSrc, fileDest, divideFactor):
	format = ""
	fileName, fileExtension = os.path.splitext(fileSrc)
	fileExtension = fileExtension.lower()
	if fileExtension == ".jpg" or fileExtension == ".jpeg":
		format = "JPEG"
	if fileExtension == ".png":
		format = "PNG"
	elif fileExtension == ".gif":
		format = "GIF"
	if format == "":
		return
	im = Image.open(fileSrc)
	width, height = im.size
	im.thumbnail((int(width/divideFactor), int(height/divideFactor)), Image.ANTIALIAS)
	im.save(fileDest, format)

# command line options: note the first line parameter and the if statements below
opt_f = 4
optlist, args = getopt.getopt(sys.argv[1:], "f:")
for opt,arg in optlist:
	if opt == "-f":
		opt_f = int(arg)
dirname = args[0]
print ("scaling by factor of", opt_f)

#output dir
outdir = dirname + "/" + OUT_DIR
if not os.path.exists(outdir):
	os.mkdir(outdir)

# list dir
dirList = os.listdir(dirname)
for fname in dirList:
	fullPath = dirname + "/" + fname
	fullPathDest = outdir + "/" + fname
	if os.path.isdir(fullPath):
		continue
	print ("file", fullPath)
	resizeImage(fullPath, fullPathDest, opt_f)


