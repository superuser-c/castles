#from mechanics import engine
from data import lang
from mechanics import generation

class Configuration:
  def __init__(self, name, generator, botl):
    self.name = name
    self.generator = generator
    self.botl = botl

a = [x for x in lang.lang.keys()]

defbotl = ["nehraje","hrac","FRandom","FEmpire","FRandom2","ComboBot","FEmpire7","FEmpire10"]
airbotl = ["nehraje","hrac","AFirework","AFirework2","FFirework","FAir","FTornado","FEmpire10"]
fempirebotl = ["nehraje","hrac","FEmpire","FEmpirep","FEmpire2","FEmpire3","FEmpire4",
               "FEmpire5","FEmpire6","FEmpire7","FEmpire8","FEmpire9","FEmpire10"]
filipbotl = ["FRandom","FRandom2"] + fempirebotl + ["FFirework","FAir","FTornado"]
adambotl = ["nehraje","hrac","AFirework","AFirework2","ABot","ComboBot"]
configs = [
  Configuration("default", None, defbotl),
  Configuration("islands", None, airbotl),
  Configuration("F Empires", None, fempirebotl),
  Configuration("Filip", None, filipbotl),
  Configuration("Adam", None, adambotl),
  Configuration("all", None, a[:(len(a) - lang.teamcount)])
  ]
genc = [
  Configuration("grid 5x5", generation.gen_grid1, None),
  Configuration("grid 10x10", generation.gen_grid2, None),
  Configuration("chaos 1", generation.gen_chaos1, None),
  Configuration("chaos 2", generation.gen_chaos1, None),
  Configuration("islands (grid 5x5)", generation.gen_grid_islands1, None),
  ]

# Configuration("", generation.gen_, ["nehraje","hrac",""])
