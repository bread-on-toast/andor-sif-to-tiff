#! /usr/bin/python

#use hexdump to create an input-file

import numpy as np


x=0
y=0
num=0
a=[]
rows=2048 # set according to your detector
data=[]
row=[]
file=""
with open("img") as f:
	for i in f:
		file=file+i
#print file

file=file.replace("\n"," ").split(" ")
rawdata=[]
for i in file:
	if len(i)==4:
		rawdata.append(i)

pos=0
while rawdata[pos]!="0044":
	pos=pos+1
pos=pos-1
y=0
while pos<len(rawdata)-1:
	px=int(rawdata[pos],16)
	bit=rawdata[pos+1]
	if bit=="0045":
		px=px+2**16

	row.append(px)
	if len(row)==rows:
		data.append(row)
#		print "row"
		row=[]
	pos=pos+2
#print data

print "P2"
print len(data[0]),len(data),
print 2**16-1

for i in data:
	line=""
	for j in i:
		line=line+str(j)+" "
	print line
