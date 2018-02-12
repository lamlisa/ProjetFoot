from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator.settings import *
from .Tools import *

class Comportement(object):
	def __init__(self,state):
		self.state = state

	def shoot_ball(self,id_team):
		t = Tools(self.state)
		return SoccerAction(t.vect_ball_goal(id_team)/(t.vect_ball_goal(id_team).norm) * 0.2, (t.vect_ball_goal(id_team)/t.vect_ball_goal(id_team).norm)*4.)
	
	def run_player(self,id_player,id_team):
		t = Tools(self.state)
		return SoccerAction(t.vect_player_ball(id_player,id_team)/t.vect_player_ball(id_player,id_team).norm * 0.2, Vector2D(0,0))

	def passe(self,id_player,id_team):
		t = Tools(self.state)
		return SoccerAction(t.vect_ball_player(id_player,id_team),(t.le_plus_proche(id_player,id_team) - self.state.player_state(id_team,id_player).position).normalize() * 4.)
