#coding:utf-8
from pylab import *
import numpy as np
import singou as sg

x = [0.0]*7 + [np.sin(2*np.pi*(n-8)/16) for n in range(8,41)] + [0.0]*24

X = sg.dft(x)
xd = sg.ift(X)
N = len(x)
h1 = [complex(np.cos(2*np.pi*(k-N)/(N*2)),-np.sin(2*np.pi*(k-N)/(N*2))) for k in range(33,N)]
h2 = [complex(np.cos(2*np.pi*k/(N*2)),-np.sin(2*np.pi*k/(N*2))) for k in range(0,33)]

h = h2+h1

print len(h)
Y = [h[k]*X[k] for k in range(N)]
#Y = sg.fir(h,X)
y = sg.ift(Y)

plot(x,label='x(n)')
plot(y,label="x'(x)")
legend()

show()

