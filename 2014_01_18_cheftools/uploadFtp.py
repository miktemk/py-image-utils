import os, os.path, string, sys, re, getopt
import ftplib

#ploades the file to chefmadeeasy.om
def uploadToChefFtp(filenameLocal, pathUpThere):
	session = ftplib.FTP('chefmadeeasy.com', 'chefmade', 'mikhail1234')
	# file to send
	file = open(filenameLocal,'rb')
	head, tail = os.path.split(filenameLocal)
	# send the file
	finalPath = 'public_html/' + pathUpThere + '/' + tail
	print 'uploading', filenameLocal, 'to', finalPath
	session.storbinary('STOR ' + finalPath, file)
	# close file and FTP
	file.close()
	session.quit()

listFiles = os.listdir(".")
extsIn = [".jpg", ".jpeg", ".bmp", ".gif", ".tif"]
for fname in listFiles:
	if os.path.isdir("./"+fname):
		continue
	noext, ext = os.path.splitext(fname)
	if not ext in extsIn:
		continue
	uploadToChefFtp(fname, "content/ingredients")

	
	

	

