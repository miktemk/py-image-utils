# takes a folder of images that need to be broken up (grid images)
# options: w (def:853), h (def:480) = width and height of cropping to do

import sys, os, re
import time, datetime
import getopt
from PIL import Image

OUT_DIR = "decomposed"

filenameIndexOut = 0

def doCroppings(imgPath, foldername_out, cropWidth, cropHeight):
	global filenameIndexOut
	print (imgPath)
	im = Image.open(imgPath)
	src_width, src_height = im.size
	print (src_width, src_height)
	cropC = src_width / cropWidth
	cropR = src_height / cropHeight
	for r in range(int(cropR)):
		for c in range(int(cropC)):
			x = c * cropWidth
			y = r * cropHeight
			outfile = foldername_out + "/crop_" + str(filenameIndexOut).zfill(3) + ".png"
			print (outfile, x, y, cropWidth, cropHeight)
			filenameIndexOut += 1
			cropping = im.crop((x, y, x + cropWidth, y + cropHeight))
			cropping.save(outfile, "PNG")

# command line options: note the first line parameter and the if statements below
optlist, args = getopt.getopt(sys.argv[1:], "w:h:")
opt_w = 853
opt_h = 533
for opt,arg in optlist:
	if opt == "-w":
		opt_w = int(arg)
	if opt == "-h":
		opt_h = int(arg)

if len(args) == 0:
	print ("Please specify the folder of images as the arg")
	sys.exit(1)

foldername = args[0]
foldername_out = foldername + "/" + OUT_DIR

# create output folder
if not os.path.exists(foldername_out):
	os.mkdir(foldername_out)

# do em!
dirList = os.listdir(foldername)
dirList.sort()
for fname in dirList:
	fullPath = foldername + "\\" + fname
	if not os.path.isdir(fullPath):
		doCroppings(fullPath, foldername_out, opt_w, opt_h)
