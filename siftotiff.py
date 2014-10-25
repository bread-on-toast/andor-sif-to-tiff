#! /usr/bin/python

#use hexdump to create an input-file

import numpy as np

def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size/2:]

x=0
y=0
num=0
a=[]
lines=1535
rows=2047

with open("img") as f:
	px=0
	add=0
	for i in f:
		line=i.split(" ")
		for word in line:
			if px==1 and add==0:
				num=num+1
				px=0
				print y,x,(int(word,16)/2**11)
#				a.append(int(word,16))
				y=y+1
				if y==1536:#6 #1600+64 somehow
					y=0
					x=x+1
			if px==1 and add==1:
				add=0
                                num=num+1
                                px=0
                                print x,y,(int("1"+word,16)/2**11)
#                               a.append(int(word,16))
                                y=y+1
                                if y==1536:#6 #1600+64 somehow
                                        y=0
                                        x=x+1

			if word=="0044": px=1
			if  word=="0045":
				px=1
				add=1


import numpy as np
import Image

data = np.random.randint(0, 255, (10,10)).astype(np.uint8)
im = Image.fromarray(data)
im.save('test.tif')

#import numpy as np

#b=autocorr(a[10000:30000])
#for i in b:
#	print abs(i)
