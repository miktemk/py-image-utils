#takes 1 image as arg and makes a rxc grid of it
# options: r (def:3), c (def:3), w (def:2560), h (def:1600)

import sys, os, re
import time, datetime
import getopt
import Image

# command line options: note the first line parameter and the if statements below
optlist, args = getopt.getopt(sys.argv[1:], "r:c:w:h:")
opt_r = 3
opt_c = 3
opt_w = 2560
opt_h = 1600
for opt,arg in optlist:
	if opt == "-r":
		opt_r = int(arg)
	if opt == "-c":
		opt_c = int(arg)
	if opt == "-w":
		opt_w = int(arg)
	if opt == "-h":
		opt_h = int(arg)

if len(args) == 0:
	print "Please specify the image as the arg"

result = Image.new('RGBA', (opt_w, opt_h), (0,0,0,0))
im = Image.open(args[0])
src_width, src_height = im.size

for r in range(opt_r):
	for c in range(opt_c):
		x = c * src_width
		y = r * src_height
		result.paste(im, (x, y))

#output file
imgdir = os.path.dirname(args[0])
if imgdir == None or imgdir == "":
	imgdir = "."
outfile =  imgdir + "/combined_result_RENAME_OR_LOSE_IT.png"

#...and save it
result.save(outfile, "PNG")


