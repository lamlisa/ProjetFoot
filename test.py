from soccersimulator import SoccerTeam, Simulation, Player
from soccersimulator import show_simu
from module.Strategy import *

## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",FonceurStrategy())
pyteam.add("PyPlayer",DefenseurStrategy())
thon.add("ThonPlayer",FonceurStrategy())
thon.add("ThonPlayer22222",DefenseurStrategy())

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)


