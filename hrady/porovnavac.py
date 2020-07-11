from mechanics import engine
from mechanics import generation
from gui import gui
import ai
import time

def try_():
    engine.init()
    engine.hraci =[ai.FEmpire10("#6df","FE10"),
                   ai.FEmpire9("white","FE9"),#ai.FEmpire9("white","FE9"),
                   ai.FEmpire8("yellow","FE8"),
                   ai.FEmpire7("orange","FE7"),
                   #ai.FEmpire6("red","FE6"),
                   #ai.FEmpire5("magenta","FE5"),
                   #ai.FEmpire("blue","FE1"),
                   #ai.FEmpirep("cyan","FE1+"),ai.FEmpirep("cyan","FE1+"),
                   #ai.FRandom2("lime","FRand2"),ai.FRandom2("lime","FRand2"),ai.FRandom2("lime","FRand2"),
                   #ai.ComboBot("green","ACombo"),ai.ComboBot("green","ACombo"),
                   #ai.FTornado("indigo", "FA+FT"),
                   #ai.FAir("light gray", "FA+FT"),ai.FAir("light gray", "FA+FT"),ai.FAir("light gray", "FA+FT"),
                   #ai.AFirework2("purple", "AF2"),ai.AFirework2("purple", "AF2"),ai.AFirework2("purple", "AF2"),ai.AFirework2("purple", "AF2"),
                   #ai.ComboBot("#ddd","ACombo1"),ai.ComboBot("#bbb","ACombo2"),ai.ComboBot("#999","ACombo3"),
                   ]
    engine.mapsiz = generation.gen_grid1(engine.hrady, engine.hraci)
    limit = 1200
    while True:
        if limit % 3 == 0:
            gui.vykresli(engine.ghrady(), engine.garmady(), engine)
        x=next(iter([x.hrac for x in engine.ghrady() if x.hrac is not None])).tym
        end=True
        for player in [x.hrac for x in engine.ghrady() if x.hrac is not None]:
            if player.tym!=x:end=False
        if end:
            return x
        if limit < 1:
            return "timeout"
        engine.tik(0.05)
        limit -= 1
        #time.sleep(0.001)
out={}
def add(w, s):
    global out
    if w not in out:
        out[w] = 0
    out[w]+=s
for _ in range(100):
    w = try_()
    add(w, 1)
    #if w == "timeout":
    #    for h in engine.hrady:
    #        if h.hrac is not None:
    #            add(h.hrac.tym, 0.001)
    print (out)
