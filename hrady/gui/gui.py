# coding=utf-8
#import engine
from tkinter import *
from data import configurations
from data import lang
import ai

configID = 0
gcfgID = 0

root = Tk()

cv = Canvas(root, width=500, height=500)
cv.pack(fill=BOTH, expand=True)

konec = False
auto = []
def posli(event, eng):
    nejblizsi=cv.find_closest(event.x, event.y)
    try:
        od = cv.gettags(nejblizsi)[0]
        if od == "r":
            global konec
            konec = True
        od = int(od)
        do = int(cv.gettags(nejblizsi)[1])
    except:
        return
    if eng.hrady[od].hrac is None:
        return
    if hasattr(eng.hrady[od].hrac, "hraj"):
        return
    eng.hrady[od].posli_armadu(od, do)

def auto_posli(event, eng):
    nejblizsi=cv.find_closest(event.x, event.y)
    try:
        od = int(cv.gettags(nejblizsi)[0])
        do = int(cv.gettags(nejblizsi)[1])
    except:
        return
    if eng.hrady[od].hrac is None:
        return
    if hasattr(eng.hrady[od].hrac, "hraj"):
        return
    if [od, do] not in auto:
        auto.append([od, do])
    else:
        auto.remove([od, do])

def vykresli(hrady, armady, eng):
    cv.delete("all")
    cv.unbind('<Button-1>')
    cv.bind('<Button-1>', lambda e: posli(e, eng))
    cv.bind("<Button-2>", lambda e: auto_posli(e, eng))
    wh = root.winfo_height()
    ww = root.winfo_width()
    scale = min(wh, ww)
    scale = (scale - 2) / eng.mapsiz
    #test
    fe8 = None
    for h in eng.hraci:
        if type(h) == ai.FEmpire8:
            fe8 = h
    #endtest
    for hradID, hrad in enumerate(hrady):
        for cesta in hrad.cesty:
            cv.create_line(hrad.x * scale, hrad.y * scale,
                            (int(hrady[cesta].x + hrad.x) * scale / 2), int((hrady[cesta].y + hrad.y) * scale / 2),
                            width=int(scale * 15), fill=hrad.barva,
                            tags=(str(hradID),str(cesta)))
        stroke = "black"
        #test
        if fe8 is not None:
            try:
                v = fe8.vahy[hradID]
                v = v * 2.55 if v > 0 else 0
                v = hex(int(v))[2:]
                if len(v) < 2:
                    v = "0" + v
                stroke = "#" + v + "00ff"
            except:
                pass
        #endtest
        cv.create_oval((hrad.x - hrad.velikost * 3) * scale, (hrad.y - hrad.velikost * 3) * scale,
                       (hrad.x + hrad.velikost * 3) * scale, (hrad.y + hrad.velikost * 3) * scale,
                       fill=hrad.barva, outline=stroke)
    for armada in armady:
        cv.create_oval((armada.x - armada.velikost * 2) * scale, (armada.y - armada.velikost * 2) * scale,
                       (armada.x + armada.velikost * 2) * scale, (armada.y + armada.velikost * 2) * scale,
                       fill=armada.hrac.barva)
    cv.create_text(25, 10, fill="blue", font="Times 16 bold",
                   text="reset", tags="r")
    winr = eng.test_vyhra()
    if winr is None or winr == "nikdo":
        for a in auto:
            if hasattr(hrady[a[0]].hrac, "hraj"):
                auto.remove(a)
                continue
            eng.hrady[a[0]].posli_armadu(a[0], a[1])
    root.update()
    root.update_idletasks()
    return konec

# limetkova, svetle modra, zluta, oranzova,     tmave modra, fialova,
# cervena,   ruzova,       hneda, tmave zelena, tyrkysova,   nebesky modra
vyber_hracu = [[lang.lang["hrac"], lang.lang["a"], "#00ff00"], [lang.lang[configurations.configs[configID].botl[2]], lang.lang["b"], "#00ffff"],
               [lang.lang["nehraje"], lang.lang["a"], "#ffff00"], [lang.lang["nehraje"], lang.lang["a"], "#ff8800"],
               [lang.lang["nehraje"], lang.lang["a"], "#0000ff"], [lang.lang["nehraje"], lang.lang["a"], "#8800ff"],
               [lang.lang["nehraje"], lang.lang["a"], "#ff0000"], [lang.lang["nehraje"], lang.lang["a"], "#ff99dd"],
               [lang.lang["nehraje"], lang.lang["a"], "#008800"]]

menu = True
def menu_hracu_klik(e):
    global configID
    global gcfgID
    nejblizsi=cv.find_closest(e.x, e.y)
    try:
        i = int(cv.gettags(nejblizsi)[0])
    except:
        return
    if i == 13:
        global menu
        menu = False
        return
    try:
        j = int(cv.gettags(nejblizsi)[1])
    except:
        return
    if j == 0:
        if vyber_hracu[i][0] == lang.lang[configurations.configs[configID].botl[-1]]:
            vyber_hracu[i][0] = lang.lang[configurations.configs[configID].botl[0]]
        else:
            try:
                vyber_hracu[i][0] = lang.lang[
                    configurations.configs[configID].botl[
                        configurations.configs[configID].botl.index(
                            lang.langi[
                                vyber_hracu[i][0]
                            ]
                        ) + 1
                    ]
                ]
            except ValueError:
                vyber_hracu[i][0] = lang.lang["nehraje"]
    elif j == 1:
        if vyber_hracu[i][1] == lang.lang["a"]:
            vyber_hracu[i][1] = lang.lang["b"]
        elif vyber_hracu[i][1] == lang.lang["b"]:
            vyber_hracu[i][1] = lang.lang["c"]
        elif vyber_hracu[i][1] == lang.lang["c"]:
            vyber_hracu[i][1] = lang.lang["d"]
        elif vyber_hracu[i][1] == lang.lang["d"]:
            vyber_hracu[i][1] = lang.lang["e"]
        elif vyber_hracu[i][1] == lang.lang["e"]:
            vyber_hracu[i][1] = lang.lang["f"]
        elif vyber_hracu[i][1] == lang.lang["f"]:
            vyber_hracu[i][1] = lang.lang["a"]
    elif j == 2:
        if i == 0:
            configID = (configID + 1) % len(configurations.configs)
        else:
            gcfgID = (gcfgID + 1) % len(configurations.genc)

def vykrasli_menu_hracu():
    cv.delete("all")
    cv.unbind('<Button-1>')
    cv.bind('<Button-1>', menu_hracu_klik)
    for i in range(len(vyber_hracu)):
        cv.create_text(101, i * 30 + 21, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][0], tags=(i, 0))
        cv.create_text(99,  i * 30 + 21, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][0], tags=(i, 0))
        cv.create_text(99,  i * 30 + 19, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][0], tags=(i, 0))
        cv.create_text(101, i * 30 + 19, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][0], tags=(i, 0))
        cv.create_text(100, i * 30 + 20, fill=vyber_hracu[i][2], font="Times 16 bold",
                       text=vyber_hracu[i][0], tags=(i, 0))
        cv.create_text(301, i * 30 + 21, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][1], tags=(i, 1))
        cv.create_text(299, i * 30 + 21, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][1], tags=(i, 1))
        cv.create_text(299, i * 30 + 19, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][1], tags=(i, 1))
        cv.create_text(301, i * 30 + 19, fill="black", font="Times 16 bold",
                       text=vyber_hracu[i][1], tags=(i, 1))
        cv.create_text(300, i * 30 + 20, fill=vyber_hracu[i][2], font="Times 16 bold",
                       text=vyber_hracu[i][1], tags=(i, 1))
    cv.create_text(400, 10, fill="blue", font="Times 16 bold",
                   text="start>", tags=13)
    cv.create_text(200, len(vyber_hracu) * 30 + 20, fill="blue", font="Times 16 bold",
                   text=configurations.configs[configID].name, tags=(0, 2))
    cv.create_text(200, len(vyber_hracu) * 30 + 50, fill="blue", font="Times 16 bold",
                   text=configurations.genc[gcfgID].name, tags=(1, 2))
    root.update()
    root.update_idletasks()
    return menu

def vyhra(winr):
    from tkinter import messagebox
    if winr != "ADMIN":
        winr = "tým " + lang.lang[winr]
    messagebox.showinfo("Výhra!", "Vyhrál " + winr + "!")
    global menu
    global auto
    menu = True
    auto = []
