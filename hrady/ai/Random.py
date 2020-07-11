import random

__all__ = ["Bot", "FRandom", "FRandom2","AFirework","AFirework2", "ABot","FFirework"]

class Bot:
    def __init__(self, b, t):
        self.barva = b
        self.tym = t
    def hraj(self, hrady):
        pass

class FRandom(Bot): # random
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if hrady[hrad].velikost > 3:
                    if len(hrady[hrad].cesty) > 0:
                        if random.randint(0, 100) < 1 or hrady[hrad].velikost > 7:
                            hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))

class FRandom2(Bot): # random
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if len(hrady[hrad].cesty) > 0:
                    hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))


class AFirework(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac is not None and hrady[hrad].velikost > 1:
                hrady[hrad].posli_armadu(hrad, random.randrange(len(hrady)))

class FFirework(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self and hrady[hrad].velikost > 1:
                df = True
                for h in hrady[hrad].cesty:
                    if hrady[h].hrac is None or hrady[h].hrac.tym != self.tym:
                        df = False
                if df:
                    hrady[hrad].posli_armadu(hrad, random.randrange(len(hrady)))
                else:
                    if len(hrady[hrad].cesty) > 0:
                        hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))

class AFirework2(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self and hrady[hrad].velikost > 1:
                hrady[hrad].posli_armadu(hrad, random.randrange(len(hrady)))

class ABot(Bot):  # random
    def __init__(self, b, t):
        super().__init__(b, t)
    def __repr__(self):
        return f"ABot ({self.barva},{self.tym})"
    def hraj(self, hrady):
        for index, hrad in enumerate(hrady):
            if hrad.hrac == self:
                f = random.randint(hrad.velikost, 10)
                if f > 5: continue
                minimum = 100
                hradP = 0
                for indexP in hrad.cesty:
                    hradP = hrady[indexP]
                    if hrad != hradP:
                        if hradP.velikost < minimum:
                            minimum = hradP.velikost
                # print(f"minimu={minimum}")
                for indexP in hrad.cesty:
                    if hrad is hradP: continue
                    hradP = hrady[indexP]
                    if hradP.velikost == minimum:
                        hrad.posli_armadu(index, indexP)
