from ai.Combo import *
from ai.FEmpire import *
from ai.Random import *
from ai.FAir import *
from ai import Evolution
import ai.Nets

def FNEBot(b, t):
    try:
        return ai.Nets.FNEBot.from_file("neai0.dat", b, t)
    except:
        return Bot(b, t)

def FNEATBot(b, t):
    try:
        raise ArithmeticError("not implemented")
    except:
        return Bot(b, t)
