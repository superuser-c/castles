import random

__all__ = ["Bot", "AComboBot", "SmaltBotForCombo", "HYPERSmaltBotForCombo", "ComboBot"]

class Bot:
    def __init__(self, b, t):
        self.barva = b
        self.tym = t
    def hraj(self, hrady):
        pass

class AComboBot(Bot):  # random
    def __init__(self, b, t):
        super().__init__(b, t)

    def __repr__(self):
        return f"ABot ({self.barva},{self.tym})"

    def hraj(self, hrady, kdo=None):
        for index, hrad in enumerate(hrady):
            if hrad.hrac == kdo:
                f = random.randint(hrad.velikost, 10)
                if f > 5: continue
                minimum = 100

                for indexP in hrad.cesty:
                    hradP = hrady[indexP]
                    if (hrad != hradP):
                        if hradP.hrac != self:
                            if hradP.velikost < minimum:
                                minimum = hradP.velikost
                if minimum == 100:
                    hrad.posli_armadu(index, random.choice(hrad.cesty))
                for indexP in hrad.cesty:
                    if hrad is hradP: continue
                    hradP = hrady[indexP]
                    if hradP.velikost == minimum:
                        hrad.posli_armadu(index, indexP)


class SmaltBotForCombo(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)

    def hraj(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac == None:
                typy[-1] = "neutral"
                continue
            if hrady[hrad].hrac is not None and hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            typy[hrad] = "hranice_neutral"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice"
        for hrad in range(len(hrady)):
            if typy[hrad] in ("generator",):
                if hrady[hrad].velikost > 1:
                    moznecesty = []
                    for cesta in hrady[hrad].cesty:
                        if typy[cesta] == "hranice":
                            moznecesty.append(cesta)
                            moznecesty.append(cesta)
                        elif typy[cesta] == "hranice_neutral":
                            moznecesty.append(cesta)
                    if len(moznecesty) > 0:
                        hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))
                    else:
                        hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))
            elif typy[hrad] == "hranice":
                if hrady[hrad].velikost > 4:
                    moznecesty = []
                    vrazedniSousedi = []
                    for cesta in hrady[hrad].cesty:
                        if typy[cesta] == "cizi":
                            moznecesty.append(cesta)
                            moznecesty.append(cesta)
                            vrazedniSousedi.append(cesta)
                        if typy[cesta] == "neutral":
                            moznecesty.append(cesta)

                    if len(vrazedniSousedi) == 1:
                        for _ in range(5):
                            hrady[hrad].posli_armadu(hrad, vrazedniSousedi[0])
                    elif len(moznecesty) > 0:
                        hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))

                    else:
                        hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))
            elif typy[hrad] == "hranice_neutral":
                if hrady[hrad].velikost > 5:
                    moznecesty = []
                    for cesta in hrady[hrad].cesty:
                        if typy[cesta] == "hranice":
                            moznecesty.append(cesta)
                        if typy[cesta] == "neutral":
                            moznecesty.append(cesta)

                    if len(moznecesty) > 0:
                        hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))
                    else:
                        hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))


class HYPERSmaltBotForCombo(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)

    def hraj(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac is None:
                typy[-1] = "neutral"
                continue
            if hrady[hrad].hrac is not None and hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            typy[hrad] = "hranice_neutral"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice"
        vahy = [100] * len(typy)  # vyšší = vzdálenější od nepřítele

        def updateVahy(index, value):
            vahy[index] = value
            for soused in hrady[index].cesty:
                if vahy[soused] > value + 1:
                    if hrady[soused].hrac is not None:
                        if hrady[soused].hrac.tym == self.tym:
                            updateVahy(soused, value + 2)

        for index, typ in enumerate(typy):
            if typ == "cizi":
                updateVahy(index, 0)
        min_soused_vaha = min((hrady[sousedID].velikost for sousedID in hrady[hrad].cesty))
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                vaha = vahy[hrad]
                for cesta in hrady[hrad].cesty:
                    if vahy[cesta] < vaha or vahy[cesta] == min_soused_vaha:
                        hrady[hrad].posli_armadu(hrad, cesta)


class ComboBot(Bot):
    osamocen = AComboBot
    utocnik = HYPERSmaltBotForCombo

    def __init__(self, b, t):
        super().__init__(b, t)
        self.vnitro = self.osamocen(b, t)
        self.armada = self.utocnik(b, t)
        self.prev_state = None

    def hraj(self, hrady):
        state = self.utok(hrady)
        if state != self.prev_state:
            self.prev_state = state
        if state:
            self.armada.hraj(hrady)
        else:
            self.vnitro.hraj(hrady, kdo=self)

    def utok(self, hrady):
        for myHrad in [hrad for hrad in hrady if hrad.hrac == self]:
            for nearHrad in [hrady[nearID] for nearID in myHrad.cesty]:
                if nearHrad.hrac is None:
                    continue
                if nearHrad.hrac.tym != self.tym:
                    return True
        return False

    def __eq__(self, x):
        return id(x) in (id(y) for y in (self.vnitro, self.armada, self))
