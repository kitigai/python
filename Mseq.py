#coding:utf-8
# 定数
P = 4
Q = 1
MASK = 2 ** P - 1

class Msequence:
    def __init__(self, seed = 1):
        self.reg = seed & MASK

    def output(self):
        bit = ((self.reg >> (P - 1)) ^ (self.reg >> (Q - 1))) & 1
        self.reg = (self.reg << 1 | bit) & MASK
        return bit

# テスト
if __name__ == '__main__':
    for x in xrange(16):
        a = Msequence(x)
        print x, ':',
        for _ in xrange(15): print a.output(),
        print
