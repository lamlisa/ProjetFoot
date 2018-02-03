from fonceur2 import *
from soccersimulator import SoccerTeam

def get_team(nb_players):
    myteam = SoccerTeam(name="MaTeam")
    if nb_players == 1:
        myteam.add("Joueur " ,fonceur2())
    if nb_players == 2:
	myteam.add("Joueur 1", fonceur2())
	myteam.add("Joueur 2", fonceur2())
    if nb_players == 4:
	myteam.add("Joueur 1",fonceur2())
	myteam.add("Joueur 2",fonceur2())
	myteam.add("Joueur 3",fonceur2())
	myteam.add("Joueur 4",fonceur2())
    return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),fonceur2())
	return myteam
