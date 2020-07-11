from mechanics import engine
from mechanics import generation
from gui import gui
import ai
import time
from data import lang
from data import configurations
from tkinter import TclError
import sys

def hraci(vyber):
    h = []
    for i in vyber:
        if i[0] == lang.lang["hrac"]:
            h.append(engine.Hrac(i[2], lang.langi[i[1]]))
        elif i[0] != lang.lang["nehraje"]:
            h.append(getattr(ai, lang.langi[i[0]])(i[2], lang.langi[i[1]]))
    return h
try:
    while gui.vykrasli_menu_hracu():
        pass
except TclError:
    sys.exit(0)

engine.init()
gui.konec = False
engine.hraci = hraci(gui.vyber_hracu)
engine.mapsiz = configurations.genc[gui.gcfgID].generator(engine.hrady, engine.hraci)
pr = time.process_time()
deltatime = 0
su = False
def suSwitch(_):
    global su
    su = not su
gui.root.bind("s", suSwitch)
while True:
    w = engine.tik(deltatime)
    try:
        if gui.vykresli(engine.ghrady(), engine.garmady(), engine):
            w  = "ADMIN"
    except TclError:
        sys.exit(0)
    if w is not None and w != "nikdo":
        gui.vyhra(w)
        try:
            while gui.vykrasli_menu_hracu():
                pass
        except TclError:
            sys.exit(0)
        engine.init()
        gui.konec = False
        engine.hraci = hraci(gui.vyber_hracu)
        engine.mapsiz = configurations.genc[gui.gcfgID].generator(engine.hrady, engine.hraci)
        deltatime = 0
        pr = time.process_time()
    n = time.process_time()
    deltatime = abs(pr - n)
    if su:
        deltatime *= 4
    pr = n
