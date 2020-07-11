import math
import random

__all__ = ["randomw", "ClassicNeuron", "ClassicNet"]

def randomw():
    return random.random() + random.randrange(-1, 1)

class SRNN():
    def __init__(self, i, o):
        self.i = i
        self.o = o
        self.wmat = []
    def copy(self):
        r = SRRN(self.i, self.o)
        return r

###################################
class ClassicNeuron:
    def __init__(self, inc):
        self.w = []
        if inc is ClassicNeuron:
            for wheight in inc.w:
                self.w.append(wheight)
        else:
            for _ in range(inc + 1):
                self.w.append(randomw())
    def gout(self, ins):
        result = self.w[0]
        for i in range(len(ins)):
            result += self.w[i + 1] * ins[i]
        return 1 / (1 + math.exp(-result))
    def copy(self):
        return ClassicNeuron(self)

class ClassicNet:
    def __init__(self, ins, outc=1):
        self.hl1 = []
        self.hl2 = []
        self.ol = []
        if ins is ClassicNet:
            self.inc = ins.inc
            self.outc = ins.outc
            for n in ins.hl1:
                self.hl1.append(n.copy())
            for n in ins.hl2:
                self.hl2.append(n.copy())
            for n in ins.ol:
                self.ol.append(n.copy())
        else:
            self.inc = ins
            self.outc = outc
            for _ in range(32):
                self.hl1.append(ClassicNeuron(self.inc))
                self.hl2.append(ClassicNeuron(32))
            for _ in range(self.outc):
                self.ol.append(ClassicNeuron(32))
    def copy(self):
        return ClassicNet(self)
    def gout(self, ins):
        h1out = []
        for n in self.hl1:
            h1out.append(n.gout(ins))
        h2out = []
        for n in self.hl2:
            h1out.append(n.gout(h1out))
        olout = []
        for n in self.ol:
            h1out.append(n.gout(h2out))
        return olout
    @staticmethod
    def from_file(name, ins, outs):
        with open(name, 'r') as f:
            data = f.readlines()
        data_matrix = []
        for line in data:
            data = line.strip().split(";")
            dat = []
            for d in data:
                nums = d.split(",")
                dat2 = [float(x) for x in nums]
                dat.append(dat2)
            data_matrix.append(dat)
        r = ClassicNet(ins, outs)
        for layer_dat in range(len(data_matrix)):
            for n_dat in range(len(data_matrix[layer_dat])):
                for w in data_matrix[layer_dat][n_dat]:
                    if layer_dat == 0:
                        r.hl1[n_dat].w = w
                    elif layer_dat == 1:
                        r.hl2[n_dat].w = w
                    elif layer_dat == 2:
                        r.ol[n_dat].w = w
    def to_file(self, name):
        data = ""
        for l in [self.hl1, self.hl2, self.ol]:
            for n in l:
                for w in n.w:
                    data += str(w) + ","
                data[-1] = ";"
            data[-1] = "\n"
        with open(name, 'w') as f:
            f.write(data)
