#coding:utf-8
import pyaudio
import sys
import pylab
import numpy

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"

def roku():

    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    print "* recording"
    all = []
    for i in range(0, RATE / chunk * RECORD_SECONDS):
        data = stream.read(chunk)
        all.append(data)
    print "* done recording"
    stream.close()
    p.terminate()
    # write data to WAVE file
    data = ''.join(all)
    result = numpy.frombuffer(data,dtype="int16") / float(2**15)
    return result

if __name__ == "__main__":
    result = roku()
    pylab.plot(result)
    pylab.ylim([-1,1])
    pylab.show()

