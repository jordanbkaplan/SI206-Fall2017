import re
fname=open("mbox-short.txt", "r")
flines = fname.readlines()
for a in flines:
	y =re.findall('From',a)
	if len(y) != 0:
		print (a)
		y=re.findall('[0-9]+',a)
		print (y)
		y=re.findall('\s.+@',a)
		print (y)