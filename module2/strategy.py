from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from module2.tools import *
from module2.comportement import *

class Fonceur1(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Fonceur1")
	def compute_strategy(self,state,idteam,idplayer):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.can_shoot():
			return c.shoot_closest_ball()
		return c.run_ball()

elo = SoccerTeam("moi")
elo.add("N",Fonceur1())
b = Billard(elo,type_game=0)
show_simu(b)
