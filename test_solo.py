from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy

class FonceurLent(Strategy):
    def __init__(self):
        super(FonceurLent,self).__init__("fonceur")
    def compute_strategy(self,state,idteam,idplayer):
        ball = state.ball
        me = state.player_state(1,0)
        oth = state.balls[0]
        shoot = (oth.position-ball.position)*100
        if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
            return SoccerAction(shoot=shoot)
        acc = ball.position-me.position
        if acc.norm<5:
            acc.norm=0.1
        return SoccerAction(acceleration=acc)

class tools(object):
	def __init__(self,state,idteam,idplayer):
		self.state = state
		self.idteam = idteam
		self.idplayer = idplayer

	def shoot_anticipe(self):
		oth = self.state.balls[0]
		me = self.state.player_state(1,0)
		ball = self.state.ball
		return SoccerAction(((oth.vitesse * 5. +oth.position)-me.position).normalize()*0.2,((oth.vitesse * 5. +oth.position)-me.position).normalize()*6 )
		
	def closest_ball(self):
		ball = self.state.ball
		me = self.state.player_state(1,0)
		others = self.state.balls
		oth = self.state.balls[0]
		for i in range(0,len(others)-1):
			if me.position.distance(others[i].position)<me.position.distance(others[i+1].position):
				oth = others[i]
			else:
				oth = others[i+1]
		return oth

	def loin(self):
		me = self.state.player_state(1,0)
		oth = self.closest_ball()
		return me.position.distance(oth.position)>50.

	def bon_angle(self,a,b):
		a = self.state.ball
		(va,vb) = get_collision(a,b)




class Fonceur1(Strategy):
	def __init__(self):
		Strategy.__init__(self,"fonceur1")
	def compute_strategy(self,state,idteam,idplayer):
		t=tools(state,idteam,idplayer)
		ball = state.ball
		me = state.player_state(1,0)
		oth = t.closest_ball()
		shoot = (oth.position-ball.position)
		if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and me.vitesse.norm<0.1:
			if oth.vitesse.norm<1.:
				if t.loin():
					return SoccerAction(shoot=shoot*6.)
				else:
					return SoccerAction(shoot=shoot*3.)
			return SoccerAction(shoot=shoot*1.)
		if me.position.distance(ball.position) < 2.:
			return SoccerAction(acceleration=(ball.position-me.position).normalize()*0.1)
		return SoccerAction(acceleration=(ball.position-me.position).normalize()*0.2)




myt = SoccerTeam("prof")
myt.add("N",Fonceur1())
b = Billard(myt,type_game=1)
show_simu(b)

