#coding: utf-8
import numpy as np
from pylab import *

def dft(x):
    N = len(x)
    X = [0.0] * N
    for k in range(N):
        for n in range(N):
             real = np.cos(2 * np.pi * k * n/N)
             imag = -np.sin(2 * np.pi * k * n/N)
             X[k] += x[ n] * complex(real, imag)
    return X


def ift(X):
    N = len(X)
    x = [0.0] * N
    for k in range(N):
        for n in range(N):
             real = np.cos(2 * np.pi * k * n/N)
             imag = np.sin(2 * np.pi * k * n/N)
             x[k] += X[n] * complex(real,imag)/N

    return x

def correl(x, y):
	Nx = len(x)
	Ny = len(y)
	zx = 0.0
	zy = 0.0
	xh = 0.0
	yh = 0.0
	for i in range(Nx):
		xh += x[i]
	for k in range(Ny):
		yh += y[k]

	xh = xh/Nx
	yh = yh/Ny
	for j in range(Nx):
		zx += (x[j] - xh)**2
	for r in range(Ny):
		zy += (y[r] - yh)**2
    
	zx = np.sqrt(zx/Nx)
	zy = np.sqrt(zy/Ny)
	r = convolution(x,y)
	print zx,zy
	r = r/(Nx * zx * zy)
	return r
	

def convolution(x, y):
    N = len(x)
    Ny = len(y)
    print N,Ny
    yd = [0.0]*N + y + [0.0]*N
    print len(yd)
    r = [0.0] * Ny*2
    try:
        for m in range(Ny*2):
            for n in range(N):

                r[m] += x[n] * yd[n + m]
    except:
        print "error",m,n

    return r
       
def filt1():
    H = [1.0]*9 + [0.5] + [0.0]*44 + [0.5] + [1.0]*9
    h = ift(H)
    return h[0:32]
def filt2():
    H = [1.0]*8 +[0.5] + [0.0]*46+[0.5]  + [1.0]*8
    h = ift(H)
    return h[0:32]

def fir2(x, b):
    """FIRフィルタをかける、x:入力信号、b:フィルタ係数"""
    y = [0.0] * len(x)  # フィルタの出力信号
    N = len(b) - 1      # フィルタ係数の数
    for n in range(len(x)):
        for i in range(N+1):
            if n - i >= 0:
                y[n] += b[i] * x[n - i]
    return y

def fir(h,x):
    P = len(h) 
    xd = [0.0] * len(x)
    for n in range(len(x)):
        for p in range(P):
            if n - p >= 0:
                xd[n] += h[p] * x[n - p]

    return xd

if __name__ == '__main__':
    h = filt1()
    print len(h)
    leng = range(len(h))
    plot(leng,h)
    show()
    
