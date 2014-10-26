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
data=[]
row=[]
with open("img") as f:
	px=0
	add=0
	for i in f:
		line=i.split(" ")
		for word in line:
			if px==1 and add==0:
				num=num+1
				px=0
				row.append(int(word,16))
#				print y,x,(int(word,16)/2**11)
				y=y+1
				if y==1536:#6 #1600+64 somehow
					data.append(row)
					row=[]
					y=0
					x=x+1
			if px==1 and add==1:
				add=0
                                num=num+1
                                px=0
                                row.append(int("1"+word,16))
                                #print y,x,(int("1"+word,16)/2**11)
                                y=y+1
                                if y==1536:#6 #1600+64 somehow
                                        data.append(row)
                                        row=[]
					y=0
                                        x=x+1

			if word=="0044": px=1
			if  word=="0045":
				px=1
				add=1




print "P2"
print len(data[0]),len(data),
print 2**16-1

for i in data:
	line=""
	for j in i:
		line=line+str(j/2)+" "
	print line
