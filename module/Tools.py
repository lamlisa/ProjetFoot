from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator.settings import *

class Tools(object):
	def __init__(self,state):
		self.state = state

	def test_shoot(self,id_player,id_team):
		return self.state.ball.position.distance(self.state.player_state(id_team,id_player).position)<(PLAYER_RADIUS+BALL_RADIUS)

	def vect_ball_goal(self,id_team):
		if id_team==1:
			v = Vector2D(GAME_WIDTH, GAME_HEIGHT/2.)
			return v - self.state.ball.position
		else:
			v = Vector2D(0,GAME_HEIGHT/2.)
			return v - self.state.ball.position
	
	def shoot_ball(self,id_team):
		return SoccerAction(self.vect_ball_goal(id_team)/(self.vect_ball_goal(id_team).norm) * 0.2, (self.vect_ball_goal(id_team)/self.vect_ball_goal(id_team).norm)*4.)

	def vect_player_ball(self,id_player,id_team):
		return (self.state.ball.position)-(self.state.player_state(id_team,id_player).position)

	def run_player(self,id_player,id_team):
		return SoccerAction(self.vect_player_ball(id_player,id_team)/self.vect_player_ball(id_player,id_team).norm * 0.2, Vector2D(0,0))

	def est_dans_terrain(self,id_team):
		if id_team==1:
			return self.state.ball.position.x < (GAME_WIDTH/2.)
		else:
			return self.state.ball.position.x > (GAME_WIDTH/2.)
