from mechanics import engine
import random
import math

def pridej_hrad(hrady):
    x = 0
    y = 0
    ok = False
    while not ok:
        ok = True
        x = random.randint(25, 475)
        y = random.randint(25, 455)
        for hrad in hrady:
            if abs(hrad.x - x) < 80 and abs(hrad.y - y) < 80:
                ok = False
    hrady.append(engine.Hrad(x, y))

def gen_chaos1(hrady, hraci):
    def uhel(x1, y1, x2, y2): # uhel pravouhleho trojuhelniku (gama = pravy uhel)
        return math.asin(abs(x1 - x2) / (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))
    for _ in range(min(len(hraci) * 3, len(hraci) + 9)):
        pridej_hrad(hrady)
    for hrac in hraci:
        r = random.randrange(0, len(hrady))
        while hrady[r].hrac is not None:
            r = random.randrange(0, len(hrady))
        hrady[r].hrac = hrac
    for a in range(len(hrady)):
        for b in range(len(hrady)):
            if a == b:
                continue
            uhelab = uhel(hrady[a].x, hrady[a].y, hrady[b].x, hrady[b].y)
            uhelba = uhel(hrady[b].x, hrady[b].y, hrady[a].x, hrady[a].y)
            for c in range(len(hrady)):
                if c == a or c == b:
                    continue
                jecesta = False
                for cesta in hrady[a].cesty:
                    if cesta == c:
                        jecesta = True
                if jecesta:
                    uhelac = uhel(hrady[a].x, hrady[a].y, hrady[c].x, hrady[c].y)
                    if abs(uhelab - uhelac) < 0.5:
                        break
                jecesta = False
                for cesta in hrady[b].cesty:
                    if cesta == c:
                        jecesta = True
                if jecesta:
                    uhelbc = uhel(hrady[b].x, hrady[b].y, hrady[c].x, hrady[c].y)
                    if abs(uhelba - uhelbc) < 0.5:
                        break
            else:
                if random.randint(0, (hrady[a].x - hrady[b].x) ** 2 + (hrady[a].y - hrady[b].y) ** 2) < 5000 or (hrady[a].x - hrady[b].x) ** 2 + (hrady[a].y - hrady[b].y) ** 2 < 2000:
                    hrady[a].cesty.append(b)
                    hrady[b].cesty.append(a)
    if not propojene(hrady):
        hrady.clear()
        gen_chaos1(hrady, hraci)
    return 500

def gen_grid(hrady, hraci, rows, cols, mis, diag, prop):
    for i in range(cols):
        for j in range(rows):
            hrady.append(engine.Hrad(45 + i * 100 + random.randint(-20,20), 45 + j * 100 + random.randint(-20,20)))
    for hrac in hraci:
        r = random.randrange(0, len(hrady))
        while hrady[r].hrac is not None:
            r = random.randrange(0, len(hrady))
        hrady[r].hrac = hrac
    for i in range(len(hrady)):
        if i - rows >= 0:
            hrady[i].cesty.append(i - rows)
        if i + rows < len(hrady):
            hrady[i].cesty.append(i + rows)
        if i - 1 >= 0 and i % rows != 0:
            hrady[i].cesty.append(i - 1)
        if i + 1 < len(hrady) and (i + 1) % rows != 0:
            hrady[i].cesty.append(i + 1)
    for _ in range(mis):
        r1 = random.randrange(0, len(hrady))
        if len(hrady[r1].cesty) > 0:
            r2 = hrady[r1].cesty[random.randrange(0, len(hrady[r1].cesty))]
            hrady[r1].cesty.remove(r2)
            hrady[r2].cesty.remove(r1)
    for _ in range(diag):
        r1 = random.randrange(0, len(hrady))
        r2 = r1 + (random.randrange(0, 1) * 2 - 1) + rows * (random.randrange(0, 1) * 2 - 1)
        r1r = r1 % rows
        r1c = int(r1 / rows)
        r2r = r2 % rows
        r2c = int(r2 / rows)
        if r2 > 0 and r2 < len(hrady) and abs(r1c - r2c) < 2 and abs(r1r - r2r) < 2:
            hrady[r1].cesty.append(r2)
            hrady[r2].cesty.append(r1)
    if prop and not propojene(hrady):
        hrady.clear()
        gen_grid(hrady, hraci, rows, cols, mis, diag, prop)
    return max(rows, cols) * 100

gen_grid1 = lambda hrady, hraci: gen_grid(hrady, hraci, 5, 5, 5, 7, True)
gen_grid2 = lambda hrady, hraci: gen_grid(hrady, hraci, 10, 10, 5, 7, True)

def gen_chaos2(hrady, hraci):
    for _ in range(min(len(hraci) * 3, len(hraci) + 9)):
        pridej_hrad(hrady)
    for hrac in hraci:
        r = random.randrange(0, len(hrady))
        while hrady[r].hrac is not None:
            r = random.randrange(0, len(hrady))
        hrady[r].hrac = hrac
    def delka(a, b):
        x = hrady[a].x - hrady[b].x
        y = hrady[a].y - hrady[b].y
        return x * x + y * y
    for index,hrad in enumerate(hrady):
        c = min([(index,x) for x in hrady], key=lambda i: delka(i[0], i[1]))
        if c[1] not in hrad.cesty:
            hrad.cesty.append(c[1])
            hrady[c[1]].cesty.append(index)
    while not propojene(hrady):
        a = random.randrange(0, len(hrady))
        b = random.randrange(0, len(hrady))
        if a != b and b not in hrady[a].cesty and a not in hrady[b].cesty:
            hrady[a].cesty.append(b)
    return 500

gen_grid_islands1 = lambda hrady, hraci: gen_grid(hrady, hraci, 5, 5, 30, 7, True)

def propojene(hrady):
    propojeno=[]
    def sir_hrad(hrad):
        if hrad not in propojeno:
            propojeno.append(hrad)
            for h in hrad.cesty:
                sir_hrad(hrady[h])
    sir_hrad(hrady[0])
    if len(hrady) != len(propojeno):
        return False
    return True
