#coding:utf-8
from pylab import *
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

r1 = sg.correl(ydata,xdata)

X = sg.dft(xdata)
Y = sg.dft(ydata)
h = sg.filt1()
xd = sg.fir(h,xdata)
yd = sg.fir(h,ydata)
Xd = sg.dft(xd)
r2 = sg.correl(yd,xd)
subplot(321)
plot(r1[0:64])
subplot(322)
plot(r2[0:64])
subplot(323)
plot(X)
subplot(324)
plot(Xd)
subplot(325)
plot(h)
show()

