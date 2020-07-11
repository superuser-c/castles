import random
import math

__all__ = ["Bot", "FEmpire", "FEmpirep", "FEmpire2", "FEmpire3", "FEmpire4",
           "FEmpire5", "FEmpire6", "FEmpire7", "FEmpire8", "FEmpire9","FEmpire10"]

class Bot:
    def __init__(self, b, t):
        self.barva = b
        self.tym = t
    def hraj(self, hrady):
        pass

class FEmpire(Bot): # posila na frontu z generatoru
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac is not None and hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            typy[hrad] = "hranice"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice"
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if typy[hrad] == "generator":
                    if hrady[hrad].velikost > 3:
                        moznecesty = []
                        for cesta in hrady[hrad].cesty:
                            if typy[cesta] == "hranice":
                                moznecesty.append(cesta)
                        if len(moznecesty) > 0:
                            hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))
                        else:
                            hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))
                elif typy[hrad] == "hranice":
                    if hrady[hrad].velikost > 5:
                        moznecesty = []
                        for cesta in hrady[hrad].cesty:
                            if typy[cesta] == "cizi":
                                moznecesty.append(cesta)
                        if len(moznecesty) > 0:
                            hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))
                        else:
                            hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))

class FEmpirep(Bot): # posila na frontu z generatoru
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac is not None and hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            typy[hrad] = "hranice"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice"
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if hrady[hrad].velikost > 1:
                    if typy[hrad] == "generator":
                        moznecesty = []
                        for cesta in hrady[hrad].cesty:
                            if typy[cesta] == "hranice":
                                moznecesty.append(cesta)
                        if len(moznecesty) > 0:
                            hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))
                        else:
                            hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))
                    elif typy[hrad] == "hranice":
                        moznecesty = []
                        for cesta in hrady[hrad].cesty:
                            if typy[cesta] == "cizi":
                                moznecesty.append(cesta)
                        if len(moznecesty) > 0:
                            hrady[hrad].posli_armadu(hrad, random.choice(moznecesty))
                        else:
                            hrady[hrad].posli_armadu(hrad, random.choice(hrady[hrad].cesty))


class FEmpire2(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
    def rozdel_typy(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac is None:
                typy[hrad] = "nic"
            elif hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            typy[hrad] = "hranice"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice"
        return typy
    def generator(self, hrad, hrady, typy):
        if hrady[hrad].velikost > 3 and len(hrady[hrad].cesty) > 0:
            dalka = []
            for _ in range(len(hrady)):
                dalka.append(0)
            dalka[hrad] = 1
            self.vzdalenostni_vetetv(hrady, typy, hrad, dalka, 2)
            mind = 99
            minID = 0
            for d in range(len(dalka)):
                if typy[d] != "hranice":
                    continue
                if dalka[d] < mind:
                    mind = dalka[d]
                    minID = d
            hrady[hrad].posli_armadu(hrad, self.zpetna(hrady, typy, dalka, minID))
    def vzdalenostni_vetetv(self, hrady, typy, cesta, seznam, dalka):
        for c in hrady[cesta].cesty:
            if seznam[c] > 0:
                continue
            if typy[c] == "cizi" or typy[c] == "nic":
                seznam[c] = "98"
                continue
            seznam[c] = dalka
            if typy[c] == "hranice":
                return
            self.vzdalenostni_vetetv(hrady, typy, c, seznam, dalka + 1)
    def zpetna(self, hrady, typy, dalky, hrad):
        mind = 99
        minID = -1
        for h in hrady[hrad].cesty:
            if not (typy[h] == "generator" or typy[h] == "hranice"):
                continue
            if dalky[h] < mind:
                mind = dalky[h]
                minID = h
        if minID < 0:
            import time
            print(typy)
            print(dalky)
            print(hrad)
            time.sleep(999)
        if mind < 2:
            return hrad
        else:
            return self.zpetna(hrady, typy, dalky, minID)
    def hranice(self, hrad, hrady, typy):
        if hrady[hrad].velikost > 5:
            moznecesty = []
            for cesta in hrady[hrad].cesty:
                if typy[cesta] == "cizi":
                    moznecesty.append(cesta)
                elif typy[cesta] == "nic":
                    if hrady[cesta].velikost < 5:
                        moznecesty.append(cesta)
                        continue
                    volne = True
                    for c in hrady[cesta].cesty:
                        if typy[c] == "cizi":
                            volne = False
                    if volne:
                        moznecesty.append(cesta)
            if len(moznecesty) > 0:
                minv = 99
                minID = -1
                for c in moznecesty:
                    if typy[c] == "cizi" and typy[minID] == "nic" and minID > -1:
                        continue
                    if hrady[c].velikost < minv:
                        minv = hrady[c].velikost
                        minID = c
                hrady[hrad].posli_armadu(hrad, minID)
            else:
                moznecesty = []
                for cesta in hrady[hrad].cesty:
                    if typy[cesta] == "cizi" or typy[cesta] == "nic":
                        moznecesty.append(cesta)
                self.posli_do_nejmensiho(hrady, hrad, moznecesty)
    def posli_do_nejmensiho(self, hrady, hrad, cesty):
        minv = 99
        minID = 0
        for c in cesty:
            if hrady[c].velikost < minv:
                minv = hrady[c].velikost
                minID = c
        hrady[hrad].posli_armadu(hrad, minID)
    def hraj(self, hrady):
        typy = self.rozdel_typy(hrady)
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if typy[hrad] == "generator":
                    self.generator(hrad, hrady, typy)
                elif typy[hrad] == "hranice":
                    self.hranice(hrad, hrady, typy)

class FEmpire3(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
    def rozdel_typy(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac is None:
                typy[hrad] = "nic"
            elif hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            typy[hrad] = "hranice"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice"
        return typy
    def generator(self, hrad, hrady, typy):
        if hrady[hrad].velikost > 1 and len(hrady[hrad].cesty) > 0:
            dalka = []
            for _ in range(len(hrady)):
                dalka.append(0)
            dalka[hrad] = 1
            self.vzdalenostni_vetetv(hrady, typy, hrad, dalka, 2)
            for i in dalka:
                if i == 0:
                    i = 98
            mind = 99
            minID = 0
            for d in range(len(dalka)):
                if typy[d] != "hranice":
                    continue
                if dalka[d] < mind:
                    mind = dalka[d]
                    minID = d
            z = self.zpetna(hrady, typy, dalka, minID)
            if z > -5:
                hrady[hrad].posli_armadu(hrad, z)
    def vzdalenostni_vetetv(self, hrady, typy, cesta, seznam, dalka):
        for c in hrady[cesta].cesty:
            if seznam[c] > 0:
                continue
            if typy[c] == "cizi" or typy[c] == "nic":
                seznam[c] = "98"
                continue
            seznam[c] = dalka
            if typy[c] == "hranice":
                return
            self.vzdalenostni_vetetv(hrady, typy, c, seznam, dalka + 1)
    def zpetna(self, hrady, typy, dalky, hrad):
        mind = 99
        minID = -1
        for h in hrady[hrad].cesty:
            if not (typy[h] == "generator" or typy[h] == "hranice"):
                continue
            if dalky[h] < mind:
                mind = dalky[h]
                minID = h
        if minID < 0:
            print(":(")
            return -5
        if mind == 1:
            return hrad
        else:
            return self.zpetna(hrady, typy, dalky, minID)
    def hranice(self, hrad, hrady, typy):
        if hrady[hrad].velikost > 1:
            moznecesty = []
            for cesta in hrady[hrad].cesty:
                if typy[cesta] == "cizi":
                    moznecesty.append(cesta)
                elif typy[cesta] == "nic":
                    if hrady[cesta].velikost < 2:
                        moznecesty.append(cesta)
                        continue
                    volne = True
                    for c in hrady[hrad].cesty:
                        if typy[c] == "cizi":
                            volne = False
                    if volne:
                        moznecesty.append(cesta)
            if len(moznecesty) > 0:
                minv = 99
                minID = -1
                for c in moznecesty:
                    if typy[c] == "cizi" and typy[minID] == "nic" and minID > -1:
                        continue
                    if hrady[c].velikost < minv:
                        minv = hrady[c].velikost
                        minID = c
                hrady[hrad].posli_armadu(hrad, minID)
            else:
                moznecesty = []
                for cesta in hrady[hrad].cesty:
                    if typy[cesta] == "cizi" or typy[cesta] == "nic":
                        moznecesty.append(cesta)
                self.posli_do_nejmensiho(hrady, hrad, moznecesty)
    def posli_do_nejmensiho(self, hrady, hrad, cesty):
        minv = 99
        minID = 0
        for c in cesty:
            if hrady[c].velikost < minv:
                minv = hrady[c].velikost
                minID = c
        hrady[hrad].posli_armadu(hrad, minID)
    def hraj(self, hrady):
        typy = self.rozdel_typy(hrady)
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if typy[hrad] == "generator":
                    self.generator(hrad, hrady, typy)
                elif typy[hrad] == "hranice":
                    self.hranice(hrad, hrady, typy)
class FEmpire4(Bot):
    def __init__(self, b, t):
        super().__init__(b, t)
    def rozdel_typy(self, hrady):
        typy = []
        for hrad in range(len(hrady)):
            typy.append("cizi")
            if hrady[hrad].hrac is None:
                typy[hrad] = "nic"
            elif hrady[hrad].hrac.tym == self.tym:
                typy[hrad] = "generator"
                if len(hrady[hrad].cesty) > 0:
                    for cesta in hrady[hrad].cesty:
                        if hrady[cesta].hrac is None:
                            if typy[hrad] != "hranice+":
                                typy[hrad] = "hranice"
                        elif hrady[cesta].hrac.tym != self.tym:
                            typy[hrad] = "hranice+"
                            self.hplus = True
        return typy
    def generator(self, hrad, hrady, typy):
        if hrady[hrad].velikost > 1 and len(hrady[hrad].cesty) > 0:
            dalka = []
            for _ in range(len(hrady)):
                dalka.append(0)
            dalka[hrad] = 1
            self.vzdalenostni_vetetv(hrady, typy, hrad, dalka, 2)
            for i in dalka:
                if i == 0:
                    i = 98
            mind = 99
            minID = 0
            for d in range(len(dalka)):
                if (typy[d] != "hranice" and not self.hplus) or typy[d] == "hranice+":
                    if dalka[d] < mind:
                        mind = dalka[d]
                        minID = d
            z = self.zpetna(hrady, typy, dalka, minID)
            if z > -5:
                hrady[hrad].posli_armadu(hrad, z)
    def vzdalenostni_vetetv(self, hrady, typy, cesta, seznam, dalka):
        try:
            for c in hrady[cesta].cesty:
                if seznam[c] > 0:
                    continue
                if typy[c] == "cizi" or typy[c] == "nic":
                    seznam[c] = "98"
                    continue
                seznam[c] = dalka
                if typy[c] == "hranice" or typy[c] == "hranice+":
                    return
                self.vzdalenostni_vetetv(hrady, typy, c, seznam, dalka + 1)
        except:
            pass
    def zpetna(self, hrady, typy, dalky, hrad):
        mind = 99
        minID = -1
        for h in hrady[hrad].cesty:
            if not (typy[h] == "generator" or typy[h] == "hranice" or typy[h] == "hranice+"):
                continue
            if dalky[h] < mind:
                mind = dalky[h]
                minID = h
        if minID < 0:
            print(":(")
            return -5
        if mind == 1:
            return hrad
        else:
            return self.zpetna(hrady, typy, dalky, minID)
    def hranice(self, hrad, hrady, typy):
        if hrady[hrad].velikost > 1:
            moznecesty = []
            for cesta in hrady[hrad].cesty:
                if typy[cesta] == "cizi":
                    moznecesty.append(cesta)
                elif typy[cesta] == "nic":
                    if hrady[cesta].velikost < 2:
                        moznecesty.append(cesta)
                        continue
                    volne = True
                    for c in hrady[hrad].cesty:
                        if typy[c] == "cizi":
                            volne = False
                    if volne:
                        moznecesty.append(cesta)
            if len(moznecesty) > 0:
                minv = 99
                minID = -1
                for c in moznecesty:
                    if typy[c] == "cizi" and typy[minID] == "nic" and minID > -1:
                        continue
                    if hrady[c].velikost < minv:
                        minv = hrady[c].velikost
                        minID = c
                hrady[hrad].posli_armadu(hrad, minID)
            else:
                moznecesty = []
                for cesta in hrady[hrad].cesty:
                    if typy[cesta] == "cizi" or typy[cesta] == "nic":
                        moznecesty.append(cesta)
                self.posli_do_nejmensiho(hrady, hrad, moznecesty)
    def posli_do_nejmensiho(self, hrady, hrad, cesty):
        minv = 99
        minID = 0
        for c in cesty:
            if hrady[c].velikost < minv:
                minv = hrady[c].velikost
                minID = c
        hrady[hrad].posli_armadu(hrad, minID)
    def hraj(self, hrady):
        self.hplus = False
        typy = self.rozdel_typy(hrady)
        for hrad in range(len(hrady)):
            if hrady[hrad].hrac == self:
                if typy[hrad] == "generator":
                    self.generator(hrad, hrady, typy)
                elif typy[hrad] == "hranice":
                    if self.hplus:
                        self.generator(hrad, hrady, typy)
                    else:
                        self.hranice(hrad, hrady, typy)
                elif typy[hrad] == "hranice+":
                    self.hranice(hrad, hrady, typy)

class FEmpire5(Bot): # inspirovan :D Adamovym vahovym systemem
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        vahy = []
        for _ in hrady:
            vahy.append(0) # vahy zacinaji na nule
        def update_vahy(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            vahy[i] = nw
            for hr in hrady[i].cesty:
                if vahy[hr] < nw and hrady[hr].hrac is not None and hrady[hr].hrac.tym == self.tym:
                    vahy[hr] = nw
                    update_vahy(hr, nw - 1)
        for i, h in enumerate(hrady):
            if h.hrac is None:
                update_vahy(i, 12 - h.velikost * 0.3)
            elif h.hrac.tym != self.tym:
                update_vahy(i, 102 - h.velikost * 0.3)
        for index, hrad in enumerate(hrady):
            if hrad.hrac == self and hrad.velikost > 1:
                maxi = -1
                maxv = -1
                for x, c in enumerate(hrad.cesty):
                    if vahy[c] > maxv:
                        maxv = vahy[c]
                        maxi = c
                hrad.posli_armadu(index, maxi)

class FEmpire6(Bot): # inspirovan :D Adamovym vahovym systemem
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        vahy = []
        for _ in hrady:
            vahy.append(0) # vahy zacinaji na nule
        def update_vahy(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            vahy[i] = nw
            for hr in hrady[i].cesty:
                if vahy[hr] < nw and hrady[hr].hrac is not None and hrady[hr].hrac.tym == self.tym:
                    vahy[hr] = nw
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = x * x + y * y
                    update_vahy(hr, nw - 1 - delkacesty * 0.0000001)
        for i, h in enumerate(hrady):
            if h.hrac is None:
                update_vahy(i, 12 - h.velikost * 0.3)
            elif h.hrac.tym != self.tym:
                update_vahy(i, 102 - h.velikost * 0.3)
        for index, hrad in enumerate(hrady):
            if hrad.hrac == self and hrad.velikost > 1:
                maxi = -1
                maxv = -1
                for x, c in enumerate(hrad.cesty):
                    if vahy[c] > maxv:
                        maxv = vahy[c]
                        maxi = c
                hrad.posli_armadu(index, maxi)

class FEmpire7(Bot): # inspirovan :D Adamovym vahovym systemem
    def __init__(self, b, t):
        super().__init__(b, t)
    def hraj(self, hrady):
        vahy = []
        for _ in hrady:
            vahy.append(0) # vahy zacinaji na nule
        def update_vahy(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            vahy[i] = nw
            for hr in hrady[i].cesty:
                if vahy[hr] < nw and hrady[hr].hrac is not None and hrady[hr].hrac.tym == self.tym:
                    vahy[hr] = nw
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy(hr, nw - delkacesty * 0.01)
        for i, h in enumerate(hrady):
            if h.hrac is None:
                update_vahy(i, 12 - h.velikost * 0.3)
            elif h.hrac.tym != self.tym:
                update_vahy(i, 102 - h.velikost * 0.3)
        for index, hrad in enumerate(hrady):
            if hrad.hrac == self and hrad.velikost > 1:
                maxi = -1
                maxv = -1
                for x, c in enumerate(hrad.cesty):
                    if vahy[c] > maxv:
                        maxv = vahy[c]
                        maxi = c
                hrad.posli_armadu(index, maxi)

class FEmpire8(Bot): #
    def __init__(self, b, t):
        super().__init__(b, t)
        self.target = None
        self.vahy = []
    def retarget(self, hrady):
        nepratele = [i for i, x in enumerate(hrady) if x.hrac is not None and x.hrac.tym != self.tym]
        if len(nepratele) > 0:
            self.target = random.choice(nepratele)
    def hraj(self, hrady):
        # pro kazdy (hrad.cesty pro kazdy hrad ke hrad je muj) kde hrad[cesta] je nepritel
        osamocen = len([y for y in
                        [cesta for x in hrady if x.hrac is not None and x.hrac.tym == self.tym for cesta in x.cesty]
                        if hrady[y].hrac is not None and hrady[y].hrac.tym != self.tym]) == 0
        # vynulovani vah
        self.vahy = []
        for _ in hrady:
            self.vahy.append(0)
        # nesiri pres nezabrane nebo nepratele
        def update_vahy(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            self.vahy[i] = nw
            for hr in hrady[i].cesty:
                if self.vahy[hr] < nw and hrady[hr].hrac is not None and hrady[hr].hrac.tym == self.tym: # pro kazdy MUJ okolni hrad
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy(hr, nw - delkacesty * 0.05) # snizeni prenesene vahy o delku cesty
        # siri pres vsechny hrady
        def update_vahy_2(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            self.vahy[i] = nw
            for hr in hrady[i].cesty:
                if self.vahy[hr] < nw: # pro kazdy okolni hrad
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy_2(hr, nw - delkacesty * 0.05) # snizeni prenesene vahy o delku cesty
        if osamocen:
            # kdyz jsem zabral terc nebo jeste zadny neni
            if self.target is None or hrady[self.target].hrac is None or hrady[self.target].hrac.tym == self.tym:
                self.retarget(hrady)
            if self.target is not None:
                update_vahy_2(self.target, 100) # sir vahy od terce
        else:
            for i, h in enumerate(hrady):
                if h.hrac is None:
                    update_vahy(i, 12 - h.velikost * 0.3)
                elif h.hrac.tym != self.tym:
                    update_vahy(i, 100 - h.velikost * 0.3)
        for index, hrad in enumerate(hrady): # posle do hradu s nejvyssi vahou
            if hrad.hrac == self and hrad.velikost > 1:
                maxi = -1
                maxv = -1
                for x, c in enumerate(hrad.cesty):
                    if self.vahy[c] > maxv:
                        maxv = self.vahy[c]
                        maxi = c
                hrad.posli_armadu(index, maxi)

class FEmpire9(Bot): #
    def __init__(self, b, t):
        super().__init__(b, t)
        self.target = None
        self.vahy = []
    def retarget(self, hrady):
        nepratele = [i for i, x in enumerate(hrady) if x.hrac is not None and x.hrac.tym != self.tym]
        if len(nepratele) > 0:
            self.target = random.choice(nepratele)
    def hraj(self, hrady, dt, armady):
        # pro kazdy (hrad.cesty pro kazdy hrad ke hrad je muj) kde hrad[cesta] je nepritel
        osamocen = len([y for y in
                        [cesta for x in hrady if x.hrac is not None and x.hrac.tym == self.tym for cesta in x.cesty]
                        if hrady[y].hrac is not None and hrady[y].hrac.tym != self.tym]) == 0
        # vynulovani vah
        self.vahy = []
        for _ in hrady:
            self.vahy.append(0)
        # nesiri pres nezabrane nebo nepratele
        def update_vahy(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            self.vahy[i] = nw
            for hr in hrady[i].cesty:
                if self.vahy[hr] < nw and hrady[hr].hrac is not None and hrady[hr].hrac.tym == self.tym: # pro kazdy MUJ okolni hrad
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy(hr, nw - delkacesty * 0.05) # snizeni prenesene vahy o delku cesty
        # siri pres vsechny hrady
        def update_vahy_2(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            self.vahy[i] = nw
            for hr in hrady[i].cesty:
                if self.vahy[hr] < nw: # pro kazdy okolni hrad
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy_2(hr, nw - delkacesty * 0.05) # snizeni prenesene vahy o delku cesty
        if osamocen:
            # kdyz jsem zabral terc nebo jeste zadny neni
            if self.target is None or hrady[self.target].hrac is None or hrady[self.target].hrac.tym == self.tym:
                self.retarget(hrady)
            if self.target is not None:
                update_vahy_2(self.target, 100) # sir vahy od terce
        else:
            for i, h in enumerate(hrady):
                if h.hrac is None:
                    update_vahy(i, 12 - h.velikost * 0.3)
                elif h.hrac.tym != self.tym:
                    update_vahy(i, 100 - h.velikost * 0.3)
        for index, hrad in enumerate(hrady): # posle do hradu s nejvyssi vahou
            if hrad.hrac == self and hrad.velikost > 1:
                maxi = -1
                maxv = -1
                for x, c in enumerate(hrad.cesty):
                    if self.vahy[c] > maxv:
                        maxv = self.vahy[c]
                        maxi = c
                if osamocen and hrady[maxi].hrac is None and \
                    len([x for x in hrady[maxi].cesty if hrady[x].hrac is not None and hrady[x].hrac.tym != self.tym]) > 0:
                    vel = hrady[maxi].velikost
                    for a in armady:
                        if a.do == maxi and a.hrac.tym == self.tym:
                            vel -= a.velikost
                    if hrad.velikost > vel:
                        hrad.posli_armadu(index, maxi)
                else:
                    hrad.posli_armadu(index, maxi)

class FEmpire10(Bot): #
    def __init__(self, b, t):
        super().__init__(b, t)
        self.target = None
        self.vahy = []
    def retarget(self, hrady, armady):
        vels = {i: x.velikost for i,x in enumerate(hrady) if x.hrac is not None and x.hrac.tym == self.tym}
        for a in armady:
            if hrady[a.do].hrac is not None and hrady[a.do].hrac.tym == self.tym:
                vels[a.do] += a.velikost
        m = max(vels.items(), key=(lambda key: key[1]))[0]
        cesty = [x for x in hrady[m].cesty if hrady[x].hrac is None]
        mind = -1
        mini = 0
        for c in cesty:
            x = hrady[m].x - hrady[c].x
            y = hrady[m].y - hrady[c].y
            delkacesty = x * x + y * y
            if len([z for z in hrady[c].cesty if hrady[z].hrac is not None and hrady[z].hrac.tym != self.tym]) > 0:
                delkacesty *= 2
            if mind == -1 or mind > delkacesty:
                mind = delkacesty
                mini = c
        self.target = mini
    def hraj(self, hrady, dt, armady):
        # pro kazdy (hrad.cesty pro kazdy hrad ke hrad je muj) kde hrad[cesta] je nepritel
        osamocen = len([y for y in
                        [cesta for x in hrady if x.hrac is not None and x.hrac.tym == self.tym for cesta in x.cesty]
                        if hrady[y].hrac is not None and hrady[y].hrac.tym != self.tym]) == 0
        # vynulovani vah
        self.vahy = []
        for _ in hrady:
            self.vahy.append(0)
        # nesiri pres nezabrane nebo nepratele
        def update_vahy(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            self.vahy[i] = nw
            for hr in hrady[i].cesty:
                if self.vahy[hr] < nw and hrady[hr].hrac is not None and hrady[hr].hrac.tym == self.tym: # pro kazdy MUJ okolni hrad
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy(hr, nw - delkacesty * 0.05) # snizeni prenesene vahy o delku cesty
        # siri pres vsechny hrady
        def update_vahy_2(i, nw): # prida vahu do okolnich hradu (index, nova vaha)
            self.vahy[i] = nw
            for hr in hrady[i].cesty:
                if self.vahy[hr] < nw: # pro kazdy okolni hrad
                    x = hrady[i].x - hrady[hr].x
                    y = hrady[i].y - hrady[hr].y
                    delkacesty = math.sqrt(x * x + y * y)
                    update_vahy_2(hr, nw - delkacesty * 0.05) # snizeni prenesene vahy o delku cesty
        if osamocen:
            if self.target is None or hrady[self.target].hrac is None or hrady[self.target].hrac.tym == self.tym:
                self.retarget(hrady, armady)
            if self.target is not None:
                update_vahy(self.target, 100)
        else:
            for i, h in enumerate(hrady):
                if h.hrac is None:
                    update_vahy(i, 12 - h.velikost * 0.3)
                elif h.hrac.tym != self.tym:
                    update_vahy(i, 100 - h.velikost * 0.3)
        for index, hrad in enumerate(hrady): # posle do hradu s nejvyssi vahou
            if hrad.hrac == self and hrad.velikost > 1:
                maxi = -1
                maxv = -1
                for x, c in enumerate(hrad.cesty):
                    if self.vahy[c] > maxv:
                        maxv = self.vahy[c]
                        maxi = c
                if osamocen and hrady[maxi].hrac is None and \
                    len([x for x in hrady[maxi].cesty if hrady[x].hrac is not None and hrady[x].hrac.tym != self.tym]) > 0:
                    vel = hrady[maxi].velikost
                    for a in armady:
                        if a.do == maxi and a.hrac.tym == self.tym:
                            vel -= a.velikost
                    if hrad.velikost > vel:
                        hrad.posli_armadu(index, maxi)
                else:
                    hrad.posli_armadu(index, maxi)
