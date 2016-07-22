# **MODE OF USE**: Drag folder into me
#
# Creates a "convert" folder within and creates new w/4 for all images

import sys, os, re
import time, datetime
import getopt
from PIL import Image

OUT_DIR = "convert"

def convertImage(fileSrc, fileDest):
	format = ""
	fileNameDest, fileExtension = os.path.splitext(fileDest)
	format = "JPEG"
	im = Image.open(fileSrc)
	im.save(fileNameDest + ".jpg", format)

# command line options: note the first line parameter and the if statements below
optlist, args = getopt.getopt(sys.argv[1:], "f:")
dirname = args[0]

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
	convertImage(fullPath, fullPathDest)


