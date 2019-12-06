

def getInput(fn):
	ls = []
	with open(fn) as f:
		for l in f.readlines():
			ls.append(l.replace('\n', '').split(')'))
	return (ls)

#i want to have a branching sequential map

def mapOrbits(ol):
	orbits = []
	i = 0
	for item in ol:
		i += 1
	return (orbits)
		



def calcOrbits(fn):
	input = getInput(fn)
	orbs = mapOrbits(input)
	for o in orbs:
		print (o)

calcOrbits("inputs/t06")