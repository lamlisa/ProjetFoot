from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from soccersimulator.settings import *
from .strategies import *

class Comportement(object):
	def __init__(self, state, id_team, id_player):
		self.state=state
		self.id_team=id_team
		self.id_player=id_player

	def run_ball(self):
		t=Tools(self.state, self.id_team, self.id_player)
		return SoccerAction(t.player_ball().normalize()*0.2, Vector2D(0,0))

	def shoot(self):
		t=Tools(self.state, self.id_team, self.id_player)
		return SoccerAction(t.player_goal().normalize*0.2, t.ball_goal().normalize()*0.4)


	def shoot_closest_ball(self):
		t=Tools(self.state, self.id_team, self.id_player)
		return SoccerAction(t.ball_closest_ball().normalize()*0.2, t.ball_closest_ball().normalize()*0.4)

	

