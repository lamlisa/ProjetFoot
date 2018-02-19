from .Strategy import FonceurStrategy
from soccersimulator import SoccerTeam

def get_team(nb_players):
	myteam = SoccerTeam(name="MaTeam")
	if nb_players == 1:
		myteam.add("Joueur " ,FonceurStrategy())
	if nb_players == 2:
		myteam.add("Joueur 1", FonceurStrategy())
		myteam.add("Joueur 2", DefenseurStrategy())
	if nb_players == 4:
		myteam.add("Joueur 1",FonceurStrategy())
		myteam.add("Joueur 2",FonceurStrategy())
		myteam.add("Joueur 3",FonceurStrategy())
		myteam.add("Joueur 4",FonceurStrategy())
	return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),FonceurStrategy())
	return myteam
