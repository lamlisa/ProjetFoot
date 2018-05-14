from module.strategy import DribbleurTestStrategy, Fonceur3TestStrategy
import random as r
from genetique import *
from soccersimulator import SoccerTeam, Simulation
from genetique_paramsearch import ParamSearch

#recherche genetique pour le dribble
d=dict()
for i in range(1,101):
	strength = 5*r.random()+1
	decal = 40*r.random()+10
	qd = 40*r.random()+10
	d[i] = (strength, decal, qd)

while len(d)>1:
	d2 = dict()
	for i in d.keys():
		strength = d.get(i)[0]
		decal = d.get(i)[1]
		qd = d.get(i)[2]
		expe = ParamSearch(strategy=DribbleurTestStrategy(strength, decal, qd), params={'strength' : [strength], 'decal' : [decal], 'qd' : [qd]})
		expe.start(show=False)
		key=expe.get_res().keys()
		d2[i]= ((strength, decal, qd),expe.get_res().get(list(expe.get_res().keys())[0]))
	S=sorted(d2.items(), key = lambda x: x[1][1], reverse=True)
	temp=dict()
	for k in range(int(len(d2)/2.)):
		a=S[k][0]
		b=S[k][1][0]
		temp.update({a:b})
	d=temp
	if len(d)>1:
		for i in d.keys():
			crossover(i,d)
			mutation(i,d)
print(d)


#recherche genetique pour le dribble et le shoot(fonceur3)
d=dict()
for i in range(100):
	strD1 = 5*r.random()+1
	strD2 = 5*r.random()+1
	strPs = 5*r.random()+1
	decal = 40*r.random()+10
	qd = 40*r.random()+10
	d[i] = (strD1, strD2, strPs, decal, qd)

while len(d)>1:
	d2 = dict()
	for i in d.keys():
		strD1 = d.get(i)[0]
		strD2 = d.get(i)[1]
		strPs = d.get(i)[2]
		decal = d.get(i)[3]
		qd = d.get(i)[4]
		expe = ParamSearch(strategy=Fonceur3TestStrategy(strD1, strD2, strPs, decal, qd), params={'strD1' : [strD1], 'strD2' : [strD2], 'strPs' : [strPs], 'decal' : [decal], 'qd' : [qd]})
		expe.start(show=False)
		key=expe.get_res().keys()
		d2[i]= ((strD1, strD2, strPs, decal, qd),expe.get_res().get(list(expe.get_res().keys())[0]))
	S=sorted(d2.items(), key = lambda x: x[1][1], reverse=True)
	temp=dict()
	for k in range(int(len(d2)/2.)):
		a=S[k][0]
		b=S[k][1][0]
		temp.update({a:b})
	d=temp
	if len(d)>1:
		for i in d.keys():
			crossover(i,d)
			mutation(i,d)
print(d)


