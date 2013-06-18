#coding:utf-8
from pylab import *
import numpy
import re
import sys
import singou as sg

argvs = sys.argv
if ( len(argvs) != 2):
    print "miss"
    quit()

title = argvs[1]
xdata = []
ydata = []

f = open(title,'r')
fn = f.readlines()

for i in fn:
	match = re.findall(r'[0-9.-]+',i)
	xdata.append(float(match[1]))
	ydata.append(float(match[2]))

r1 = sg.correl(xdata,ydata)

X = sg.dft(xdata)
Y = sg.dft(ydata)
h = sg.filt1()
xd = sg.fir(h,xdata)
yd = sg.fir(h,ydata)
Xd = sg.dft(xd)
r2 = sg.correl(xd,yd)
subplot(311)

plot(range(-1023,len(r1)/2 +1),r1)
plt.xlim([-1023,1024])
#xticks(numpy.linspace(0,2500,6),numpy.linspace(-1024,2500-1048,6))
subplot(312)
plot(range(-1023,len(r2)/2 +1),r2)
plt.xlim([-1023,1024])
subplot(313)
plot(h)
#title(r"test",fontsize = 25,fontname="serif")
show()

