from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerState
from .tools import *
from .comportement import *

class RandomStrategy(Strategy):
	def __init__(self):
        	Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
        	return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

class Fonceur1Strategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Fonceur1")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.test_shoot():
			return c.shoot()
		if t.in_my_third():
			return SoccerAction(Vector2D(0,0),Vector2D(0,0))
		return c.run()


class Fonceur3Strategy(Strategy):
	def __init__(self,cpt=0, cpt2=0):
		Strategy.__init__(self,"Fonceur3")
		self.cpt = cpt
		self.cpt2=cpt2
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if state.get_score_team(1)+state.get_score_team(2)>self.cpt2:
			self.cpt2=state.get_score_team(1)+state.get_score_team(2)
			self.cpt=0
		if self.cpt>100:
			if t.test_shoot():
				if t.ennemi_in_my_perimeter():
					return c.dribble()
				if t.in_his_fifth():
					return c.shoot()
				return c.petit_shoot()
			else:
				return c.run_anticipe()
		else:
			self.cpt+=1
			if t.in_my_half():
				if t.test_shoot():
					if t.ennemi_in_my_perimeter():
						return c.dribble()
					return c.petit_shoot()
				return c.run_anticipe()
			return SoccerAction(Vector2D(0,0),Vector2D(0,0))

class DefenseurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.in_my_quarter():
			if t.test_shoot():
				if t.someone():
					return c.passe()
				else:
					return c.degage()
			else:
				return c.run()
		else:
			return c.return_goal()

class GoalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.goal_perimeter(): 
			if t.test_shoot():
				if t.someone():
					return c.passe()
				else:
					return c.degage()
			return c.run_anticipe()
		else:
			return c.return_goal()

class FonceurTestStrategy(Strategy):
	def __init__(self, strength=None):
		Strategy.__init__(self,"Fonceur Test")
		self.strength = strength
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.test_shoot():
			return c.shoot2(self.strength)
		return c.run()

class DribbleurTestStrategy(Strategy):
	def __init__(self, strength, decal, qd):
		Strategy.__init__(self,"Dribbleur Test")
		self.strength = strength
		self.decal= decal
		self.qd=qd
	def compute_strategy(self,state,id_team,id_player):
		t=Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.test_shoot():
			if t.ennemi_in_my_perimeter2(self.qd):
				return c.dribble2(self.strength, self.decal)
			return c.shoot()
		else:
			return c.run()


