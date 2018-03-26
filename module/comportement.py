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
		return SoccerAction(t.ball_goal().normalize()*0.2, t.ball_goal().normalize()*4.)

	def run(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.player_ball().normalize()*0.2, Vector2D(0,0))

	def passe(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction((t.closest_friend()-t.player()).normalize()*0.2, (t.closest_friend()-t.player()).normalize()*2.)

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

	def return_attaquant_defense(self):
		t=Tools(self.state,self.id_team,self.id_player)
		return SoccerAction(t.attaquant_my_defense(), Vector2D(0,0))

	def degage(self):
		t=Tools(self.state,self.id_team,self.id_player)
		decal=30.
		if t.closest_ennemi().y > t.player().y:
			return SoccerAction((t.player_his_goal()+Vector2D(0,-decal)).normalize()*0.2, (t.player_his_goal()+Vector2D(0,-decal)).normalize()*6.)
		else:
			return SoccerAction((t.player_his_goal()+Vector2D(0,decal)).normalize()*0.2, (t.player_his_goal()+Vector2D(0,decal)).normalize()*6.)
	
	def run_anticipe(self):
		t=Tools(self.state,self.id_team,self.id_player)
		"""if t.ball_in_my_perimeter():
			return SoccerAction(((0.6*self.state.ball.vitesse+t.ball())-t.player()).normalize()*0.2, Vector2D(0,0))"""
		return SoccerAction(((5*self.state.ball.vitesse+t.ball())-t.player()).normalize()*0.2, Vector2D(0,0))

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




