#coding:utf-8
from pylab import *
import numpy as np
import singou as sg

x = [0.0]*7 + [np.sin(2*np.pi*(n-8)/16) for n in range(8,41)] + [0.0]*24
y = []

for i in x:
	y.append(i)
	y += [0.0]*3 

N = len(x)




h = sg.filt2()

Y = sg.fir2(y,h)



plot(y,label='x(n)')
plot(Y,label="y")
legend()

show()

