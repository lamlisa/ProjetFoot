from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerState
from .Tools import *

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

class FonceurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Fonceur")
	def compute_strategy(self,state,id_team,id_player):
		if Tools(state).test_shoot(id_player,id_team):
			return Tools(state).shoot_ball(id_team)
		return Tools(state).run_player(id_player,id_team)

class DefenseurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		if Tools(state).est_dans_terrain(id_team):
			if Tools(state).test_shoot(id_player,id_team):
				return Tools(state).shoot_ball(id_team)
			return Tools(state).run_player(id_player,id_team)
		else:
			return SoccerAction(Vector2D(0,0),Vector2D(0,0))

class GoalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	
		
	
