from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerState
from .Tools import *
from .Comportement import *

class RandomStrategy(Strategy):
	def __init__(self):
        	Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
        	return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

class FonceurStrategy(Strategy):
	def __init__(self,*args):
		Strategy.__init__(self,"Fonceur")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state)
		c = Comportement(state)
		if t.test_shoot(id_player,id_team):
			return c.shoot_ball(id_team)
		return c.run_player(id_player,id_team)

class DefenseurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state)
		c = Comportement(state)
		if t.est_dans_tiers_terrain(id_team): 
			if t.test_shoot(id_player,id_team):
				return c.shoot_ballD(id_team)
			return c.run_playerD(id_player,id_team)
		else:
			return c.return_goal(id_player,id_team)

class GoalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")

class FonceurTestStrategy(Strategy):
	def __init__(self, strength=None):
		Strategy.__init__(self,"Fonceur Test")
		self.strength = strength

	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state)
		c = Comportement(state)
		if t.test_shoot(id_player,id_team):
			return c.shoot_ball2(id_player,id_team,self.strength)
		return c.run_player(id_player,id_team)
