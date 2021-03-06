#coding:utf-8
import struct
import thread
import wave
import numpy as np
from pylab import *
from Mseq import *
from rokuon import *
from singou import *

def createSineWave(f0,fs,leng,M):
	
	data = []
	for n in arange(leng * fs):
		s = np.sin(2 * np.pi * f0 * n/fs + M*np.pi/2  )

		data.append(s)

	data = [int(x * 32767.0) for x in data]

	#bit = struct.pack("h" * len(data), *data)
	return data

def play( data, fs, bit):
	import pyaudio
	p = pyaudio.PyAudio()
	stream = p.open(format = pyaudio.paInt16,
			channels = 1,
			rate = int(fs),
			output = True)

	chunk = 1024
	sp = 0
	buffer = data[sp:sp+chunk]
	while buffer != '':
		stream.write(buffer)
		sp = sp + chunk
		buffer = data[sp:sp+chunk]
	stream.close()
	p.terminate()

if __name__ == "__main__":
    freq = 1000.0
    leng = 4.0 / freq
    a = Msequence(15)
    Msq = []
    data = []
    for _ in xrange(64):
        Msq = a.output()
        print Msq
        data += createSineWave(freq,44100.0,leng,Msq)

    bit = struct.pack("h" * len(data), *data)
    args = (bit,44100.0,16)
    thread.start_new_thread(play,args)
    result = roku()
    r = correl(data,result)
    subplot(221)
    plot(data)
    subplot(222)
    plot(result)
    subplot(223)
    plot(r)
    show()	
