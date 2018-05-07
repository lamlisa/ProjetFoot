from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerState
from .tools import *
from .comportement import *
import logging

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
		if t.ball_in_my_third():
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
				if not t.closest_ennemi_behind():
					if t.ennemi_in_my_small_perimeter():
						return c.dribble(5.)
					return c.dribble(1.5)
				if t.ball_in_his_goal_perimeter():
					return c.shoot()
				return c.shoot3(2.)
			else:
				return c.run_anticipe()
		else:
			self.cpt+=1
			if t.ball_in_my_half():
				if t.test_shoot():
					if not t.closest_ennemi_behind():
						if t.ennemi_in_my_small_perimeter():
							return c.dribble(5.)
						return c.dribble(1.5)
					if t.ball_in_his_goal_perimeter():
						return c.shoot()
					return c.petit_shoot2(2.)
				else:
					return c.run_anticipe()
			else:
				return SoccerAction(Vector2D(0,0),Vector2D(0,0))

class Fonceur3_2v2Strategy(Strategy):
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
				if not t.all_ennemi_behind():
					if t.ennemi_in_my_small_perimeter():
						if not t.ennemi_in_my_closest_friend_small_perimeter():
							if t.player().distance(t.closest_friend()) < 50.:
								return c.passe(3.)
						return c.dribble(5.)
					return c.dribble(1.5)
				if t.ball_in_his_goal_perimeter():
					return c.shoot()
				return c.shoot3(2.)
			else:
				return c.run_anticipe()
		else:
			self.cpt+=1
			if t.ball_in_my_half():
				if t.test_shoot():
					if not t.all_ennemi_behind():
						if t.ennemi_in_my_small_perimeter():
							if not t.ennemi_in_my_closest_friend_small_perimeter():
								if t.player().distance(t.closest_friend()) < 50.:
									return c.passe(3.)
							return c.dribble(5.)
						return c.dribble(1.5)
					if t.ball_in_his_goal_perimeter():
						return c.shoot()
					return c.petit_shoot2(2.)
				else:
					return c.run_anticipe()
			else:
				return SoccerAction(Vector2D(0,0),Vector2D(0,0))

class Fonceur3_topStrategy(Strategy):
	def __init__(self,cpt=0):
		Strategy.__init__(self,"Fonceur3")
		self.cpt = cpt
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.ball_in_top():
			if t.test_shoot():
				if not t.closest_ennemi_behind():
					if t.ennemi_in_my_small_perimeter():
						if not t.ennemi_in_my_closest_friend_small_perimeter():
							return c.passe(3.)
						return c.dribble(5.)
					return c.dribble(1.5)
				if t.ball_in_his_goal_perimeter():
					return c.shoot()
				return c.petit_shoot2(2.)
			else:
				return c.run_anticipe()
		else:
			return c.follow_ball_top()

class Fonceur3_downStrategy(Strategy):
	def __init__(self,cpt=0):
		Strategy.__init__(self,"Fonceur3")
		self.cpt = cpt
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if not t.ball_in_top():
			if t.test_shoot():
				if not t.closest_ennemi_behind():
					if t.ennemi_in_my_small_perimeter():
						if not t.ennemi_in_my_closest_friend_small_perimeter():
							return c.passe(3.)
						return c.dribble(5.)
					return c.dribble(1.5)
				if t.ball_in_his_goal_perimeter():
					return c.shoot()
				return c.petit_shoot()
			else:
				return c.run_anticipe()
		else:
			return c.follow_ball_down()

class Fonceur3_modifStrategy(Strategy):
	def __init__(self,cpt=0, cpt2=0):
		Strategy.__init__(self,"Fonceur3_modif")
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
				if not t.closest_ennemi_behind():
					if t.ennemi_in_my_small_perimeter():
						if not t.ennemi_in_my_closest_friend_perimeter():
							return c.passe(3.)
						if t.ball_in_his_third():
							return c.dribble(1.5)
						return c.dribble(5.)
					if t.ennemi_in_my_perimeter():
						return c.dribble(1.5)
					return c.petit_shoot()
				return c.shoot()
			else:
				#if t.ball_in_my_third():
					#return c.return_attaquant_defense()
				return c.run_anticipe()
		else:
			self.cpt+=1
			if t.ball_in_my_half():
				if t.test_shoot():
					if not t.all_ennemi_behind():
						return c.dribble(1.5)
					return c.shoot()
				return c.run_anticipe()
			return SoccerAction(Vector2D(0,0),Vector2D(0,0))


class DefenseurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.ball_in_my_third():
			if t.test_shoot():
				if not t.ennemi_in_my_closest_friend_small_perimeter():
					return c.passe(3.)
				return c.degage()
			else:
				return c.run_anticipe()
		else:
			return c.return_defense()

class Defenseur_topStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.ball_in_my_third():
			if t.test_shoot():
				return c.degage()
			else:
				return c.run_anticipe()
		else:
			if t.ball_in_top():
				return c.return_defense_top()
			return c.return_defense_milieu()

class Defenseur_downStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.ball_in_my_third():
			if t.test_shoot():
				return c.degage()
			else:
				return c.run_anticipe()
		else:
			if not t.ball_in_top():
				return c.return_defense_down()
			return c.return_defense_milieu()

class Defenseur_2v2Strategy(Strategy) :
	def __init__(self,cpt=0, cpt2=0):
		Strategy.__init__(self,"Defenseur_2v2")
		self.cpt = cpt
		self.cpt2=cpt2
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if state.get_score_team(1)+state.get_score_team(2)>self.cpt2:
			self.cpt2=state.get_score_team(1)+state.get_score_team(2)
			self.cpt=0
		if self.cpt>100:
			if t.ball_in_my_half():
				if t.test_shoot():
					if not t.ennemi_in_my_closest_friend_perimeter():
						return c.passe(3.)
					return c.degage()
				else:
					return c.run_anticipe()
			if t.ennemi_in_my_half():
				return c.return_defense()
			if t.test_shoot():
				if t.all_ennemi_behind():
					if t.ball_in_his_goal_perimeter:
						return c.shoot()
				if not t.ennemi_in_my_closest_friend_perimeter():
					return c.passe(3.)
				return c.dribble(1.5)
			return c.follow_fonceur()
		else:
			self.cpt+=1
			if t.ball_in_my_half():
				if t.test_shoot():
					if not t.ennemi_in_my_closest_friend_perimeter():
						return c.passe(3.)
					return c.degage()
				else:
					return c.run_anticipe()
			if t.ennemi_in_my_half():
				return c.return_defense()
			if t.test_shoot():
				if t.all_ennemi_behind():
					if t.ball_in_his_goal_perimeter:
						return c.shoot()
				if not t.ennemi_in_my_closest_friend_perimeter():
					return c.passe(3.)
				return c.dribble(1.5)
			return c.return_defense()

class GoalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.ball_in_my_goal_perimeter(): 
			if t.test_shoot():
				#if t.someone():
					#return c.passe()
				#else:
					#return c.degage()
				return c.degage()
			return c.run_anticipe()
		else:
			return c.return_goal()

class DTree_6Strategy(Strategy):
    def __init__(self,tree,dic,get_features):
        Strategy.__init__(self,"Tree Strategy")
        self.dic = dic
        self.tree = tree
        self.get_features = get_features
        self.logger = logging.getLogger("arbrestrategie")

    def compute_strategy(self, state, id_team, id_player):
        label = self.tree.predict([self.get_features(state,id_team,id_player)])[0]
        if label not in self.dic:
            self.logger.error("Erreur : strategie %s non trouve" %(label,))
            return SoccerAction()
        return self.dic[label].compute_strategy(state,id_team,id_player)

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
	def __init__(self, strength=None, decal=None, qd=None):
		Strategy.__init__(self,"Dribbleur Test")
		self.strength = strength
		self.decal= decal
		self.qd=qd
	def compute_strategy(self,state,id_team,id_player):
		t=Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.test_shoot():
			if not t.closest_ennemi_behind():
				if t.ennemi_in_my_perimeter2(self.qd):
					return c.dribble2(self.strength, self.decal)
				return c.petit_shoot()
			return c.shoot()
		else:
			return c.run_anticipe()

class Fonceur3TestStrategy(Strategy):
	def __init__(self, strD1=None, strD2=None, strPs=None, decal=None, qd=None):
		Strategy.__init__(self,"Fonceur Test")
		self.strD1 = strD1
		self.strD2 = strD2
		self.strPs = strPs
		self.decal= decal
		self.qd=qd
	def compute_strategy(self,state,id_team,id_player):
		t = Tools(state,id_team,id_player)
		c = Comportement(state,id_team,id_player)
		if t.test_shoot():
			if not t.closest_ennemi_behind():
				if t.ennemi_in_my_perimeter2(self.qd):
					return c.dribble(self.strD1)
				return c.dribble(self.strD2)
			if t.ball_in_his_fifth():
				return c.shoot()
			return c.petit_shoot2(self.strPs)
		else:
			return c.run_anticipe()
	

