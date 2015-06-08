import sys, os, re
import time, datetime
import getopt
from PIL import Image
from PIL import ImageEnhance

OUT_DIR = "contrasted"

def resizeImage(fileSrc, fileDest, opt_c):
	format = "JPEG"
	fileName, fileExtension = os.path.splitext(fileSrc)
	fileExtension = fileExtension.lower()
	if fileExtension == ".png":
		format = "PNG"
	elif fileExtension == ".gif":
		format = "GIF"
	im = Image.open(fileSrc)
	width, height = im.size
	im = ImageEnhance.Contrast(im).enhance(1.5)
	im = ImageEnhance.Brightness(im).enhance(1.5)
	im = ImageEnhance.Sharpness(im).enhance(2)
	#im.thumbnail((int(width/divideFactor), int(height/divideFactor)), Image.ANTIALIAS)
	im.save(fileDest, format)

# command line options: note the first line parameter and the if statements below
opt_c = 4
optlist, args = getopt.getopt(sys.argv[1:], "f:")
for opt,arg in optlist:
	if opt == "-f":
		opt_c = int(arg)
dirname = '.'
if len(args) > 0:
	dirname = args[0]
print("scaling by factor of", opt_c)

#output dir
outdir = dirname + "/" + OUT_DIR
if not os.path.exists(outdir):
	os.mkdir(outdir)

# list dir
dirList = os.listdir('.')
for fname in dirList:
	fullPath = dirname + "/" + fname
	fullPathDest = outdir + "/" + fname
	if os.path.isdir(fullPath):
		continue
	filename, fileExtension = os.path.splitext(fname)
	exts = ['.jpg', '.jpeg', '.png', 'gif', 'bmp', 'tiff']
	if not fileExtension.lower() in exts:
		continue
	print ("file", fullPath)
	resizeImage(fullPath, fullPathDest, opt_c)
	#break


