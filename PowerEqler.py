#coding:utf-8
import wave
import sys
import math
import struct
from numpy import *
from pylab import *


def printWaveInfo(wf):
    """WAVEファイルの情報を取得"""
    print "チャンネル数:", wf.getnchannels()
    print "サンプル幅:", wf.getsampwidth()
    print "サンプリング周波数:", wf.getframerate()
    print "フレーム数:", wf.getnframes()
    print "パラメータ:", wf.getparams()
    print "長さ（秒）:", float(wf.getnframes()) / wf.getframerate()

def save(data, fs, bit, filename):
    """save wave file"""
    wf = wave.open(filename,"w")
    wf.setnchannels(1)
    wf.setsampwidth(bit / 8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

def seakK(xa, xb):
    """seeking k value"""
    lengthA = xa.getnframes()
    lengthB = xb.getnframes()

    bufferA = xa.readframes( lengthA )
    bufferB = xb.readframes( lengthB )
    

    dataA = frombuffer(bufferA, dtype="int16")/32768.0
    dataB = frombuffer(bufferB, dtype="int16")/32768.0

    if xa.getnchannels() != 1:
        dataA = dataA[::2]

    if xb.getnchannels() != 1:
        dataB = dataB[::2]

    powerA = calkpower( dataA, lengthA)
    powerB = calkpower( dataB, lengthB)

    k = math.sqrt( powerA/powerB )
    xa.close()
    xb.close()

    return k

    
    
def calkpower(buffer,length):
    """calklate power"""

    print 'length =',length
    power = 0.0
    for n in range(length ):
    #    print 'n=',n
        power += buffer[n]

    print 'power = ',power
    return power
    
    


def Nomalizer(filenameAlp,filenameBet,savefile):
    xa = wave.open(filenameAlp, "r")
    xb = wave.open(filenameBet, "r")
    xc = wave.open(filenameBet, "r")
    #printWaveInfo(xb)
    
    k = seakK(xa,xb)
    print 'k=',k

    fs = xc.getframerate()
    lengthC = xc.getnframes() #フレーム数
    bufferC = xc.readframes(lengthC)
    #print len(buffer)  # バイト数 = 1フレーム2バイト x フレーム数
    # bufferはバイナリなので2バイトずつ整数（-32768から32767）にまとめる
    dataC = frombuffer(bufferC, dtype="int16")/32768.0

    if xc.getnchannels() != 1:
        dataC = dataC[::2]




    print lengthC
    print dataC
    newdata = [0.0] * lengthC
    for n in range(lengthC):
        newdata[n] =  dataC[n] * k

    
    newdata = [int(x * 32767.0) for x in newdata]
    newdata = struct.pack("h" * len(newdata), *newdata )

    save(newdata, fs, 16, savefile )
    xa.close()
    xb.close()
    xc.close()

if __name__ == '__main__':
    '''filenameAlp のパワーに filenameBet のパワーを合わせsavefileへ1ch waveとしてセーブ　filenameAlpのパワーの方が小さい事が確認されていなければならない'''
    argvs = sys.argv
    if (len(argvs) != 4):
        print 'failed'
        quit()

    filenameAlp = argvs[1]
    filenameBet = argvs[2]
    savefile = argvs[3]
    Nomalizer(filenameAlp,filenameBet,savefile)
    # プロット
   # plot(data)
   # show()
