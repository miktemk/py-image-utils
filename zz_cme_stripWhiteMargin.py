import sys, os, re
import time, datetime
import getopt
import Image

OUT_DIR = "convert"
EXTENSION_OVERRIDE = "JPEG" # None to use same as original image

def processImage(fileSrc, fileDest):
	global EXTENSION_OVERRIDE
	format = "JPEG"
	fileName, fileExtension = os.path.splitext(fileSrc)
	fileExtension = fileExtension.lower()
	if fileExtension == ".png":
		format = "PNG"
	elif fileExtension == ".gif":
		format = "GIF"
	if EXTENSION_OVERRIDE != None:
		format = EXTENSION_OVERRIDE
	fileName, fileExtension = os.path.splitext(fileDest)
	if format == "JPEG":
		fileDest = fileDest + ".jpg"
	elif format == "PNG":
		fileDest = fileDest + ".png"
	elif format == "GIF":
		fileDest = fileDest + ".gif"
	im = Image.open(fileSrc)
	rgb_im = im.convert('RGB')
	width, height = im.size
	margin = 0
	for i in range(width):
		# todo: check all rows
		r, g, b = rgb_im.getpixel((i, 1))
		#print (r,g,b)
		if not (r == 254 and g == 254 and b == 254):
			margin = i
			break
	print "removing a margin of", margin, "pixels", format
	im.crop((margin, 0, width - margin, height)).save(fileDest, format)

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
	print "file", fullPath;
	processImage(fullPath, fullPathDest)


