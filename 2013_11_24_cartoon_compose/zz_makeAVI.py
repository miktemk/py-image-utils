# download mplayer binaries for this... you need mencoder.exe

import sys, os, re, getopt

optlist, args = getopt.getopt(sys.argv[1:], "w:h:f:")
opt_w = 853
opt_h = 480
opt_f = 30
for opt,arg in optlist:
	if opt == "-w":
		opt_w = int(arg)
	if opt == "-h":
		opt_h = int(arg)
	if opt == "-f":
		opt_f = int(arg)

if len(args) == 0:
	print "Please specify the folder of images as the arg"

foldername = args[0]

command = ('C:\Program Files (x86)\MPlayer\mencoder',
           foldername + '/*.png',
           '-mf',
           'type=png:w=' + `opt_w` + ':h=' + `opt_h` + ':fps=' + `opt_f` + '',
           '-ovc',
           'lavc',
           '-lavcopts',
           'vcodec=mpeg4',
           '-oac',
           'copy',
           '-o',
           'output_rename_it_or_lose_it.avi')

os.spawnlp(os.P_WAIT, 'mencoder', command)