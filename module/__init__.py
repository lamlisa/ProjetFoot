from .strategy import Fonceur3Strategy, DefenseurStrategy, Defenseur_topStrategy, Defenseur_downStrategy, Fonceur3_downStrategy, Fonceur3_topStrategy, GoalStrategy, Defenseur_2v2Strategy, Fonceur3_2v2Strategy
from soccersimulator import SoccerTeam

def get_team(nb_players):
	myteam = SoccerTeam(name="MaTeam")
	if nb_players == 1:
		myteam.add("Joueur " ,Fonceur3Strategy())
	if nb_players == 2:
		myteam.add("Fonceur3_2v2", Fonceur3_2v2Strategy())
		myteam.add("Defenseur_2v2", Defenseur_2v2Strategy())
	if nb_players == 4:
		myteam.add("Joueur 1",Defenseur_downStrategy())
		myteam.add("Joueur 2",Defenseur_topStrategy())
		myteam.add("Joueur 3",Fonceur3_downStrategy())
		myteam.add("Joueur 4",Fonceur3_topStrategy())
	return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),Fonceur3Strategy())
	return myteam
