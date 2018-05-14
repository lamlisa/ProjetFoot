from soccersimulator import SoccerTeam, Simulation, Player, DTreeStrategy
from soccersimulator import show_simu
from module.strategy import *
import module_CaiEddy
import module_ariana
#import angeloortiz
import module_Austen
import module_aaTarek
import module_Baladeur
#import module_ahmedmelliti
import module_TalebMaham
import module_seb05
import module
import pickle
from exemple_apprentissage import my_get_features

# Creation d'une equipe
#pyteam = module_CaiEddy.get_team(2)
#pyteam = module_ariana.get_team(2)
"""pyteam = angeloortiz.get_team(2)"""
#pyteam = module_Austen.get_team(2)
#pyteam = module_aaTarek.get_team(1)
"""pyteam = module_ahmedmelliti.get_team(1)"""
#pyteam = module_Baladeur.get_team(2)
#pyteam = module_TalebMaham.get_team(2)
#pyteam = module_seb05.get_team(1)

#thon = module_CaiEddy.get_team(1)
#thon = module_ariana.get_team(2)
"""thon = module_angeloortiz.get_team(2)"""
#thon = module_Austen.get_team(1)
#thon = module_aaTarek.get_team(1)
"""thon = module_ahmedmelliti.get_team(1)"""
thon = module_Baladeur.get_team(4)
#thon = module_TalebMaham.get_team(2)
#thon = module_seb05.get_team(1)

#pyteam =SoccerTeam(name="PyTeam")
#thon = SoccerTeam(name="ThonTeam")
pyteam = module.get_team(4)
#thon = module.get_team(1)

#pyteam.add("PyDefenseur",DefenseurStrategy())
#pyteam.add("PyFonceur1",Fonceur1Strategy())
#pyteam.add("PyFonceur3",Fonceur3Strategy())
#pyteam.add("PyTree",DTree_6Strategy())

#thon.add("ThonDefenseur",DefenseurStrategy())
#thon.add("ThonFonceur1",RandomStrategy())
#thon.add("ThonFonceur3",Fonceur3Strategy())
#thon.add("ThonFonceur3_modif",Fonceur3_modifStrategy())
#thon.add("DribbleurTest", DribbleurTestStrategy(1.84, 49, 46))
#thon.add("Fonceur3TestStrategy", Fonceur3TestStrategy(4.73, 1.72, 4.08, 25.74, 26.47))
"""dic_strategy = {Fonceur3Strategy().name:Fonceur3Strategy(), DefenseurStrategy().name:DefenseurStrategy(), Fonceur3_downStrategy().name:Fonceur3_downStrategy(), Fonceur3_topStrategy().name:Fonceur3_topStrategy(), Defenseur_downStrategy().name:Defenseur_downStrategy(), Defenseur_topStrategy().name:Defenseur_topStrategy()}
with open("tree_test.pkl","rb") as f:
	dt = pickle.load(f)
pyteam.add("TreePlayer", DTree_6Strategy(dt,dic_strategy,my_get_features))"""

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)



"""from genetique import *
j1 = (1,2,3)
j2 = (4,5,6)
d = {1:j1,2:j2}
#mix_strength(1,2,d)
#crossover(1,d)
mutation(1,d)
print(d,j1,j2)"""


