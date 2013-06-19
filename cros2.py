#coding:utf-8

from pylab import *
import sys
import re

argvs = sys.argv
if(len(argvs) != 2):
	print "miss"
	quit()

title = argvs[1]

f = open(title,'r')
fn = f.readlines()

xdata = []
zdata = []

for i in fn:
	match = re.findall(r'[0-9.-]+',i)
	xdata.append(double(match[1]))
	zdata.append(double(match[2]))
subplot(211)
plot(xdata)
subplot(212)
plot(zdata)

show()
