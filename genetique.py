import random as r

def mix_strength(i1,i2,d):
		j1 = d.get(i1)
		j2 = d.get(i2)
		temp1 = (j2[0],j1[1],j1[2])
		temp2 = (j1[0],j2[1],j2[2])
		d[i1] = temp1
		d[i2] = temp2

def mix_decal(i1,i2,d):
		j1 = d.get(i1)
		j2 = d.get(i2)
		temp1 = (j1[0],j2[1],j1[2])
		temp2 = (j2[0],j1[1],j2[2])
		d[i1] = temp1
		d[i2] = temp2

def mix_qd(i1,i2,d):
		j1 = d.get(i1)
		j2 = d.get(i2)
		temp1 = (j1[0],j1[1],j2[2])
		temp2 = (j2[0],j2[1],j1[2])
		d[i1] = temp1
		d[i2] = temp2

def mix_hasard(i1, i2,d):
	u=r.random()
	p=r.random()
	if u <= 1/2.:
		if p <= 1/3.:
			return mix_strength(i1,i2,d)
		if p <= 2/3.:
			return mix_decal(i1,i2,d)
		if p <= 1.:
			return mix_qd(i1,i2,d)
	else:
		if p <= 1/3.:
			mix_strength(i1,i2,d)
			return mix_decal(i1,i2,d)
		if p <= 2/3.:
			mix_decal(i1,i2,d)
			return mix_qd(i1,i2,d)
		if p <= 1.:
			mix_qd(i1,i2,d)
			return mix_strength(i1,i2,d)

def crossover(i,d):
	d2=d.copy()
	d2.pop(i)
	L=[]
	for k in d2.keys():
		L.append(k)
	i2 = L[r.randint(0,len(L)-1)]
	p = r.random()
	if p <= 0.7:
		return mix_hasard(i,i2,d)

def mutation_hasard(i,d):
	u = r.random()
	j = d.get(i)
	if u <=1/3:
		temp = (5*r.random()+1, j[1], j[2])
		d[i] = temp
		return j
	if u <=2/3:
		temp = (j[0], 40*r.random()+10, j[2])
		d[i] = temp
		return j
	if u <=1:
		temp = (j[0], j[1], 40*r.random()+10 )
		d[i] = temp
		return j

def mutation(i,d):
	if r.random()<=0.01:
		mutation_hasard(i,d)

def mix2_strD1(i1,i2,d):
	j1 = d.get(i1)
	j2 = d.get(i2)
	temp1 = (j2[0],j1[1],j1[2],j1[3],j1[4])
	temp2 = (j1[0],j2[1],j2[2],j2[3],j2[4])
	d[i1] = temp1
	d[i2] = temp2

def mix2_strD2(i1,i2,d):
	j1 = d.get(i1)
	j2 = d.get(i2)
	temp1 = (j1[0],j2[1],j1[2],j1[3],j1[4])
	temp2 = (j2[0],j1[1],j2[2],j2[3],j2[4])
	d[i1] = temp1
	d[i2] = temp2

def mix2_strPs(i1,i2,d):
	j1 = d.get(i1)
	j2 = d.get(i2)
	temp1 = (j1[0],j1[1],j2[2],j1[3],j1[4])
	temp2 = (j2[0],j2[1],j1[2],j2[3],j2[4])
	d[i1] = temp1
	d[i2] = temp2

def mix2_decal(i1,i2,d):
	j1 = d.get(i1)
	j2 = d.get(i2)
	temp1 = (j1[0],j1[1],j1[2],j2[3],j1[4])
	temp2 = (j2[0],j2[1],j2[2],j1[3],j2[4])
	d[i1] = temp1
	d[i2] = temp2

def mix2_qd(i1,i2,d):
	j1 = d.get(i1)
	j2 = d.get(i2)
	temp1 = (j1[0],j1[1],j1[2],j1[3],j2[4])
	temp2 = (j2[0],j2[1],j2[2],j2[3],j1[4])
	d[i1] = temp1
	d[i2] = temp2

