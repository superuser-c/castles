import random
import math
from inspect import signature

def init():
    global timer
    global hrady
    global hraci
    global armady
    global mapsiz
    timer = 0
    hrady = []
    hraci = []
    armady = []
    mapsiz = 0

def ghrady():
    global hrady
    return hrady

def ghraci():
    global hraci
    return hraci

def garmady():
    global armady
    return armady

class Hrac:
    def __init__(self, barva, tym):
        self.barva = barva
        self.tym = tym

class Hrad:
    def __init__(self, x, y):
        self.velikost = 5
        self.hrac = None
        self.x = x
        self.y = y
        self.cesty = []
    @property
    def barva(self):
        if self.hrac is None:
            return "gray"
        return self.hrac.barva
    def posli_armadu(self, od, do):
        if self.velikost < 2:
            return
        armady.append(Armada(int(self.velikost/2), self.hrac, od, do))
        if self.velikost % 2 > 0:
            self.velikost += 1
        self.velikost /= 2
    def prichod_armady(self, armada):
        if self.hrac is None or armada.hrac.tym != self.hrac.tym:
            self.velikost -= armada.velikost
        else:
            self.velikost += armada.velikost
        if self.velikost < 1:
            self.velikost = 1
            self.hrac = armada.hrac
        if self.velikost > 8:
            self.velikost = 8

class Armada:
    def __init__(self, v, h, cestaod, cestado):
        self.velikost = v
        self.hrac = h
        self.od = cestaod
        self.do = cestado
        self.vzdalenost = 0
        x = hrady[cestaod].x - hrady[cestado].x
        y = hrady[cestaod].y - hrady[cestado].y
        self.delkacesty = (x ** 2 + y ** 2) ** 0.5
    @property
    def x(self):
        odx = hrady[self.od].x
        dox = hrady[self.do].x
        if self.delkacesty == 0:
            return odx
        return self.vzdalenost / self.delkacesty * (dox - odx) + odx
    @property
    def y(self):
        ody = hrady[self.od].y
        doy = hrady[self.do].y
        if self.delkacesty == 0:
            return ody
        return self.vzdalenost / self.delkacesty * (doy - ody) + ody

def test_vyhra():
    winr = "nikdo"
    for hrad in hrady:
        if hrad.hrac is not None:
            if winr == "nikdo":
                winr = hrad.hrac.tym
            elif hrad.hrac.tym != winr:
                winr = "nikdo"
                break
    else:
        for a in armady:
            if winr == "nikdo":
                winr = a.hrac.tym
            elif a.hrac.tym != winr:
                winr = "nikdo"
                break
    return winr

def tik(dt):
    for armadaID in range(len(armady)):
        armada = armady[armadaID]
        for a2 in range(armadaID + 1, len(armady)):
            if armada.hrac.tym != armady[a2].hrac.tym:
                vzdalenost = 100
                if armada.od == armady[a2].od and armada.do == armady[a2].do:
                    vzdalenost = abs(armada.vzdalenost - armady[a2].vzdalenost)
                if armada.do == armady[a2].od and armada.od == armady[a2].do:
                    vzdalenost = abs(armada.delkacesty - armada.vzdalenost - armady[a2].vzdalenost)
                if vzdalenost < 200 * dt:
                    if armada.velikost == armady[a2].velikost:
                        armady.pop(max(armadaID, a2))
                        armady.pop(min(armadaID, a2))
                        tik(dt)
                        return
                    if armada.velikost > armady[a2].velikost:
                        armada.velikost -= armady[a2].velikost
                        armady.pop(a2)
                        tik(dt)
                        return
                    if armada.velikost < armady[a2].velikost:
                        armady[a2].velikost -= armada.velikost
                        armady.pop(armadaID)
                        tik(dt)
                        return
        if armada.vzdalenost > armada.delkacesty:
            hrady[armada.do].prichod_armady(armada)
            armady.pop(armadaID)
            tik(dt)
            return
    for armada in armady:
        armada.vzdalenost += 100 * dt
    global timer
    timer += dt
    if timer > 1:
        for hrad in hrady:
            if hrad.hrac is not None:
                hrad.velikost += 1
                if hrad.velikost > 8:
                    hrad.velikost = 8
        timer = 0
    winr = test_vyhra()
    if winr is not None and winr != "nikdo":
        return winr
    for hrac in hraci:
        if hasattr(hrac, "hraj"):
            parlen = len(signature(hrac.hraj).parameters)
            if parlen > 2:
                hrac.hraj(hrady, dt, armady)
            elif parlen > 1:
                hrac.hraj(hrady, dt)
            else:
                hrac.hraj(hrady)
    return "nikdo"
