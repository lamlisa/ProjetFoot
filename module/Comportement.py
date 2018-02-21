from soccersimulator  import Strategy, SoccerAction, Vector2D, SoccerState
from soccersimulator.settings import *
from .Tools import *

class Comportement(object):
	def __init__(self,state):
		self.state = state

	def shoot_ball(self,id_team):
		t = Tools(self.state)
		if t.tiers_attaque(id_team):
			return SoccerAction(t.vect_ball_goal(id_team).normalize() * 0.2, t.vect_ball_goal(id_team).normalize()*4.)
		return SoccerAction(t.vect_ball_goal(id_team).normalize() * 0.2, t.vect_ball_goal(id_team).normalize()*5.)
	
	def run_player(self,id_player,id_team):
		t = Tools(self.state)
		return SoccerAction(t.vect_player_ball(id_player,id_team).normalize() * 0.2, Vector2D(0,0))

	def passe(self,id_player,id_team):
		t = Tools(self.state)
		return SoccerAction((t.le_plus_proche_ami(id_player,id_team) - self.state.player_state(id_team,id_player).position).normalize() * 0.2,(t.le_plus_proche_ami(id_player,id_team) - self.state.player_state(id_team,id_player).position).normalize() * 2.)

	def se_demarquer(self,id_player,id_team):
		t=Tools(self.state)
		return SoccerAction((self.state.player_state(id_team,id_player).position-t.le_plus_proche_ennemi(id_player,id_team)).normalize() * 0.2,Vector2D(0,0))

	def marquer_joueur(self, id_player, id_team):
		t=Tools(self.state)
		return SoccerAction((t.le_plus_proche_ennemi(id_player,id_team)-self.state.player_state(id_team,id_player).position).normalize() * 0.2,Vector2D(0,0))

	def return_goal(self,id_player,id_team):
		t=Tools(self.state)
		return SoccerAction(t.vect_my_goal_player(id_player,id_team),Vector2D(0,0))

	def shoot_ball2(self,id_player,id_team,strength):
		t = Tools(self.state)
		return SoccerAction(t.vect_goal_player(id_player,id_team).normalize()* 0.2, t.g(strength,t.dist_goal_player(id_player,id_team))*(t.vect_goal_player(id_player,id_team).normalize()))

	def shoot_ball3(self,id_player,id_team,strength):
		t = Tools(self.state)
		return SoccerAction(t.vect_goal_player(id_player,id_team).normalize()*0.2 , t.vect_goal_player(id_player,id_team).normalize()*strength)

	def shoot_ballD(self,id_team):
		t = Tools(self.state)
		return SoccerAction(t.vect_ball_goal(id_team).normalize() * 0.2, t.vect_ball_goal(id_team).normalize()*6.)
	
	def run_playerD(self,id_player,id_team):
		t = Tools(self.state)
		return SoccerAction(((5*self.state.ball.vitesse+self.state.ball.position)-self.state.player_state(id_team,id_player).position).normalize() * 0.2, Vector2D(0,0))






