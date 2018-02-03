from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator import SoccerTeam, Simulation, Player
from soccersimulator import show_simu
from soccersimulator.settings import *

class tools(object):
	def __init__(self, id_team, id_player,state):
		self.id_team = id_team
		self.id_player = id_player
		self.state = state

	def test_shoot(self):
		return self.state.ball.position.distance(self.state.player_state(self.id_team,self.id_player).position)<(PLAYER_RADIUS+BALL_RADIUS)

	def vect_ball_goal(self):
		if self.id_team==1:
			v = Vector2D(GAME_WIDTH, GAME_HEIGHT/2.)
			return v - self.state.ball.position
		else:
			v = Vector2D(0,GAME_HEIGHT/2.)
			return v - self.state.ball.position
	
	def shoot_ball(self):
		return SoccerAction(tools.vect_ball_goal(self)/(tools.vect_ball_goal(self).norm) * 0.2, (tools.vect_ball_goal(self)/tools.vect_ball_goal(self).norm)*4.)

	def vect_player_ball(self):
		return (self.state.ball.position)-(self.state.player_state(self.id_team,self.id_player).position)

	def run_player(self):
		return SoccerAction(tools.vect_player_ball(self)/tools.vect_player_ball(self).norm * 0.2, Vector2D(0,0))



