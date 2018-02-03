from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
from soccersimulator.settings import *
from tools import *

class fonceur2(Strategy):
	def __init__(self):
		Strategy.__init__(self,"fonceur2")
	def compute_strategy(self,state,id_team,id_player):
		t = tools(id_team, id_player, state)
		if t.test_shoot():
			return t.shoot_ball()
		return t.run_player()
