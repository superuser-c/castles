import random

__all__ = ["FAir", "FTornado"]

class Bot:
    def __init__(self, b, t):
        self.barva = b
        self.tym = t
    def hraj(self, hrady):
        pass

class FAir(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
        self.target = -1
    def hraj(self, hrady):
        i = 100
        while i > 0 and (self.target == -1 or (hrady[self.target].hrac is not None and hrady[self.target].hrac.tym == self.tym)):
            i -= 1
            self.target = random.randrange(0, len(hrady))
        if self.target != -1:
            for hrad in range(len(hrady)):
                if hrady[hrad].hrac == self and hrady[hrad].velikost > 1:
                    hrady[hrad].posli_armadu(hrad, self.target)

class FTornado(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
        self.map = -1
        self.remap_timer = 5
    def hraj(self, hrady, dt):
        if self.map == -1 or self.remap_timer < 0:
            self.map = [x for x in range(len(hrady))]
            random.shuffle(self.map)
            self.remap_timer = 5
        self.remap_timer -= dt
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self and hrady[hrad].velikost > 1:
                hrady[hrad].posli_armadu(hrad, self.map[hrad])
