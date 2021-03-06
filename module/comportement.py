from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator.settings import *
from .tools import *

class Comportement(object):
	def __init__(self,state,id_team,id_player):
		self.state = state
		self.id_team = id_team
		self.id_player = id_player

	def shoot(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.ball_his_goal().normalize()*0.2, t.ball_his_goal().normalize()*4.)

	def run(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_ball().normalize()*0.2, Vector2D(0,0))

	def passe(self, strength):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction((t.closest_friend()-t.player()).normalize()*0.2, (t.closest_friend()-t.player()).normalize()*strength)

	def se_demarquer(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction((t.player()-t.closest_ennemi()).normalize()*0.2, Vector2D(0,0))

	def marquer_joueur(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction((t.closest_ennemi()-t.player()).normalize()*0.2, Vector2D(0,0))

	def return_goal(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_my_goal(), Vector2D(0,0))

	def return_defense(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_my_defense(), Vector2D(0,0))

	def return_defense_top(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_my_defense_top(), Vector2D(0,0))

	def return_defense_down(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_my_defense_down(), Vector2D(0,0))

	def return_defense_milieu(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_my_defense_milieu(), Vector2D(0,0))

	def return_attaquant_defense(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.attaquant_my_defense(), Vector2D(0,0))

	def follow_ball_top(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.top_ball_x(), Vector2D(0,0))

	def follow_ball_down(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.down_ball_x(), Vector2D(0,0))

	def degage(self):
		t=Tools(self.state,self.id_team,self.id_player)
		decal=40.
		if t.closest_ennemi().y > t.player().y:
			return SoccerAction((t.player_his_goal()+Vector2D(0,-decal)).normalize()*0.2, (t.player_his_goal()+Vector2D(0,-decal)).normalize()*6.)
		else:
			return SoccerAction((t.player_his_goal()+Vector2D(0,decal)).normalize()*0.2, (t.player_his_goal()+Vector2D(0,decal)).normalize()*6.)
	
	def run_anticipe(self):
		t=Tools(self.state,self.id_team,self.id_player)
		"""if t.ball_in_my_perimeter():
			return SoccerAction(((0.6*self.state.ball.vitesse+t.ball())-t.player()).normalize()*0.2, Vector2D(0,0))"""
		return SoccerAction(((5*self.state.ball.vitesse+t.ball())-t.player()).normalize()*0.2, Vector2D(0,0))

	def run_anticipe2(self,n):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(((n*self.state.ball.vitesse+t.ball())-t.player()).normalize()*0.2, Vector2D(0,0))
	
	def dribble(self,puiss):
		t=Tools(self.state,self.id_team,self.id_player)
		decal=50.
		if t.closest_ennemi().y > t.player().y:
			return SoccerAction((t.player_his_goal()+Vector2D(0,-decal)).normalize()*0.01, (t.player_his_goal()+Vector2D(0,-decal)).normalize()*puiss)
		else:
			return SoccerAction((t.player_his_goal()+Vector2D(0,decal)).normalize()*0.01, (t.player_his_goal()+Vector2D(0,decal)).normalize()*puiss)

	def petit_shoot(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_his_goal().normalize()*0.01, t.player_his_goal().normalize())

	def petit_shoot2(self, strength):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_his_goal().normalize()*0.01, t.player_his_goal().normalize()*strength)

	def shoot2(self,strength):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_his_goal().normalize()*0.2, t.g(strength,t.d_his_goal_player())*(t.player_his_goal().normalize()))

	def shoot3(self,strength):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_his_goal().normalize()*0.2, t.player_his_goal().normalize()*strength)

	def dribble2(self, strength, decal):
		t=Tools(self.state,self.id_team,self.id_player)
		if t.closest_ennemi().y > t.player().y:
			return SoccerAction((t.player_his_goal()+Vector2D(0,-decal)).normalize()*0.2, (t.player_his_goal()+Vector2D(0,-decal)).normalize()*strength)
		else:
			return SoccerAction((t.player_his_goal()+Vector2D(0,decal)).normalize()*0.2, (t.player_his_goal()+Vector2D(0,decal)).normalize()*strength)

	def follow_fonceur(self):
		t=Tools(self.state,self.id_team,self.id_player)
		p = 25.
		if self.id_team == 1:
			return SoccerAction(Vector2D(t.closest_friend().x - p, t.ball().y)-t.player(), Vector2D(0,0))
		else:
			return SoccerAction(Vector2D(t.closest_friend().x + p, t.ball().y)-t.player(), Vector2D(0,0))

		

