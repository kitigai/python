#coding: utf-8
import numpy as npa
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
    N = len(x)
    yd = y + y
    

def filt1():
    H = [1.0]*9 + [0.5] + [0.0]*44 + [0.5] + [1.0]*9
    h = ift(H)
    return h


if __name__ == '__main__':
    h = filt1()
    print len(h)
    leng = range(len(h))
    plot(leng,h)
    show()
    
