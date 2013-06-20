#-*- coding: utf-8 -*-
#kadai6

from pylab import *
import sys
import math
import numpy as np
import wave
import re
import scipy.fftpack
from singou import *
"""
def dft(x):
	N = len(x)
	X = [0.0] * N
	for k in range(N):
		for n in range(N):
			real = np.cos(2 * np.pi * k * n/N)
			imag = -np.sin(2 * np.pi * k * n/N)
			X[k] += x[ n] * complex(real, imag)
	return X


def rft(X):
	N = len(X)
	x = [0.0] * N
	for k in range(N):
		for n in range(N):
			real = np.cos(2 * np.pi * k * n/N)
			imag = np.sin(2 * np.pi * k * n/N)
			x[k] += X[n] * complex(real,imag)/N

	return x

"""
argvs = sys.argv
if ( len(argvs) != 2):
	print 'miss'
	quit()

title = argvs[1]
WinWidth = 64
xdata = []
zdata = []
X = []
Z = []

H = []

start = 0

f = open(title,'r')
fn = f.readlines()

for i in fn:
	match = re.findall(r'[0-9.-]+',i)
	xdata.append(float(match[1]))
	zdata.append(float(match[2]))

	print match[1],match[2]
N = len(xdata)
M = N / WinWidth
for j in range(M):
	x = xdata[start:WinWidth+start]
	z = zdata[start:WinWidth+start]
	X.append(dft(x))
	Z.append(dft(z))
	#x = xdata[start:WinWidth+start]
	#z = zdata[start:WinWidth+start]
	#X.append(np.fft.fft(x))
	#Z.append(np.fft.fft(z))
	#X.append(scipy.fftpack.fftfreq(x))
	#Z.append(scipy.fftpack.fftfreq(z))
	start += WinWidth

for k in range(WinWidth):
	Wxz = 0.0
	Wxx = 0.0
	for r in range(M):
		xz = X[r][k].conjugate()*Z[r][k]
		xx = X[r][k].conjugate()*X[r][k]
		Wxz += xz
		Wxx += xx
	H.append(Wxz/Wxx)	


h = ift(H)
imag = [ d.imag for d in h]
real = [ d.real for d in h]
Ximag = [ d.imag for d in X[1]]
Xreal = [ d.real for d in X[1]]

length = range(WinWidth)
leng = range(len(xdata))
plot( length,real,label ='real')
plot( length,imag,label ='imag')
#plot( sinlength,sindata)
xlabel("sample")
ylabel("h(sample)")
legend()
show()

