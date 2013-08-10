#coding:utf-8
import wave
import sys
import scipy
from underwater import *
import numpy as np
import struct
from pylab import *

samplelen = 64
N = 1024
SHIFT =512 


if __name__ == '__main__':
	"""filein1をフィルタとしてfilein2の周波数を削る
	"""
	
	argvs = sys.argv
	if(len(argvs) != 4):
		print 'miss'
		quit()

	filein1 = argvs[1]
	filein2 = argvs[2]
	#fileout = argvs[3]

	hammingwindow = np.hamming(N)

	xa = wave.open(filein1,"r")
	xb = wave.open(filein2,"r")

	fs = xa.getframerate()
	lengthA = xa.getnframes()
	bufferA = xa.readframes(lengthA)
	#print bufferA
	dataA = np.frombuffer(bufferA,dtype="int16")/32768.0

	lengthB = xb.getnframes()
	bufferB = xb.readframes(lengthB)
	dataB = np.frombuffer(bufferB,dtype="int16")/32768.0
	play(bufferB,44100,16)
	print len(dataA)
	if len(dataA) < len(dataB):
		j = np.zeros(len(dataB)-len(dataA))
		dataA = np.append(dataA,j)

	else:
		j = np.zeros(len(dataA)-len(dataB))
		dataB = np.append(dataB,j)	

	
	xa.close()
	xb.close()
	start = 0
	dataC = np.array([])
	while start+N < len(dataB):
		windowedDataA = hammingwindow * dataA[start:start+N]
		windowedDataB = hammingwindow * dataB[start:start+N]

		freqA = np.fft.fft(windowedDataA)
		freqB = np.fft.fft(windowedDataB)

		freqC = freqA+freqB
		dat = np.fft.ifft(freqC)
		dataC = np.append(dataC,dat[:SHIFT])
		start += SHIFT

	#dataC /=10	
	dataC = np.array([x.real for x in dataC])
	dataC *= 32767.0

	bit = struct.pack("h"*len(dataC), *dataC)
	play(bit,44100.0,16)
	subplot(311)		
	plot(dataC)
	subplot(312)
	plot(dataA)
	subplot(313)
	plot(bufferB)
	show()

	
