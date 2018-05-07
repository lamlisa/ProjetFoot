from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from soccersimulator.settings import *

class Tools(object):
	def __init__(self, state, id_team, id_player):
		self.state=state
		self.id_team=id_team
		self.id_player=id_player

#Condition

	def can_shoot(self):
		return self.state.ball.vitesse.normalize()<0.01 and self.state.player_state(self.id_team, id_player).vitesse.normalize()<0.1


#position

	def ball(self):
		return self.state.ball.position

	def player(self):
		return self.state.player_state(self.id_team, self.id_player)

	def goal(self):
		return Vector2D(GAME_WIDTH, GAME_HEIGHT/2.)

#vecteur

	def player_ball(self):
		return self.ball()-self.player()

	def player_goal(self):
		return self.goal()-self.player()

	def ball_goal(self):
		return self.goal()-self.ball()

	def ball_closest_ball(self):
		return self.closest_ball()-self.ball()

	def goal_closest_ball(self):
		return self.goal()-self.closest_ball()



	def closest_ball(self):
		L=[i for i in self.state.balls]
		if len(L)==1:
			return L[0].position
		s=0
		v=0
		for j in range (len(L)-1):
			if j==0:
				s=self.ball().distance(L[j].position)
				v=L[j]
			u=self.ball().distance(L[j+1].position)
			if s>u:
				s=u
				v=L[j+1]
		return v.position


	
	
