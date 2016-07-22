import os, os.path, string, sys, re, getopt
import Image

def processImage(filename, postfix):
	global newWidth, newHeight, qqq, resizeResample
	mo = re.match("(.*)\.[A-Za-z0-9]*$", string.lower(filename))
	outdir = postfix
	if not os.path.exists(outdir):
		os.mkdir(outdir)
	fnameOut = outdir + "/" + mo.group(1) + "_" + postfix + "." + extOut
	print "processing "+filename+"->"+fnameOut+"...",
	img = Image.open(filename)
	try:
		transparency = img.info["transparency"]
	except KeyError:
		transparency = -1
	
	if (newWidth != -1) or (newHeight != -1):
		(width, height) = img.size
		asg = float(height) / float(width)
		print asg
		if (newWidth == -1):
			newWidth = width
		if (newHeight == -1):
			newHeight = int(asg * newWidth)
		img = img.resize((newWidth, newHeight), resizeResample)
	if (string.lower(extOut) == "jpg") or (string.lower(extOut) == "jpeg"):
		img = img.convert(mode="RGB")
	try:
		if transparency != -1:
			if qqq == -1:
				img.save(fnameOut, transparency=transparency)
			else:
				img.save(fnameOut, quality=qqq, transparency=transparency)
		else:
			if qqq == -1:
				img.save(fnameOut)
			else:
				img.save(fnameOut, quality=qqq)
		print "Done"
	except IOError:
		print "cannot save", fnameOut

def processFile(filename, postfix):
	global extsIn
	for ext in extsIn:
		if re.search(".*\."+string.lower(ext)+"$", string.lower(filename)):
			processImage(filename, postfix)

def runBatch(w, h, postfix):
	global newWidth, newHeight, qqq, resizeResample, extOut
	extOut = "jpg"
	newWidth = w
	newHeight = h
	qqq = 95
	resizeResample = Image.BILINEAR
	for fname in listFiles:
		if not os.path.isdir("./"+fname):
			processFile("./"+fname, postfix)

if __name__ == "__main__":
	opts, rest = getopt.getopt(sys.argv[1:], "i:o:w:h:q:r:")
	extsIn = ["jpg", "jpeg", "bmp", "gif", "tif"]
	listFiles = os.listdir(".")

	extOut = "jpg"
	
	#runBatch(640, 480, "vga")
	#runBatch(200, -1, "200")
	runBatch(800, -1, "800")
	#runBatch(1280, -1, "1280")


	

