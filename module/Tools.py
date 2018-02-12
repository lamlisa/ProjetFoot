from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator.settings import *

class Tools(object):
	def __init__(self,state):
		self.state = state

	def test_shoot(self,id_player,id_team):
		return self.state.ball.position.distance(self.state.player_state(id_team,id_player).position)<(PLAYER_RADIUS+BALL_RADIUS)

	def vect_ball_goal(self,id_team):
		return self.vect_goal(id_team) - self.state.ball.position

	def vect_ball_player(self,id_player,id_team):
		return self.vect_goal(id_team) - self.state.player_state(id_team,id_player).position

	def vect_goal(self,id_team):
		if id_team==1:
			return Vector2D(GAME_WIDTH, GAME_HEIGHT/2.)
		return Vector2D(0,GAME_HEIGHT/2.)

	def vect_player_ball(self,id_player,id_team):
		return (self.state.ball.position)-(self.state.player_state(id_team,id_player).position)

	def est_dans_terrain(self,id_team):
		if id_team==1:
			return self.state.ball.position.x < (GAME_WIDTH/2.)
		else:
			return self.state.ball.position.x > (GAME_WIDTH/2.)

	def le_plus_proche(self,id_player,id_team):
		L = [(it, ip) for (it, ip) in self.state.players if ((it == id_team) & (ip != id_player))]
		s=0
		v=0
		for i in range(len(L)-1):
			if i==0:
				s= self.state.player_state(id_team,id_player).position.distance(self.state.player_state(id_team,L[0][1]).position)
				v=L[0][1]
			u=self.state.player_state(id_team,id_player).position.distance(self.state.player_state(id_team,L[i+1][1]).position)
			if s>u:
				s=u
				v=L[i+1][1]
		return self.state.player_state(id_team,v).position


