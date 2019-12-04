from collections import defaultdict

def getInput(filename):
	ret = []
	with open (filename) as f:
		for line in f:
			ret.append(line)
	return(ret)

def processWires(input):
	wires = []
	for w in input:
		wire = defaultdict(lambda: 0)
		w = w.split(',')
		x = 0
		y = 0
		s = 0
		for step in w:	
			direction = step[0]
			distance = int(step[1:])
			if direction is 'U':
				for i in range(0, distance):
					wire[(x, y)] = s
					s += 1
					y += 1
			elif direction is 'D':
				for i in range(0, distance):
					wire[(x, y)] = s
					s += 1
					y -= 1
			elif direction is 'L':
				for i in range(0, distance):
					wire[(x, y)] = s
					s += 1
					x -= 1
			elif direction is 'R':
				for i in range(0, distance):
					wire[(x, y)] = s
					s += 1
					x += 1
		wires.append(wire)
	return (wires)

def manhattenDistance(coords):
	ret = abs(coords[0]) + abs(coords[1])
	return (ret)

def getIntersect(wires):
	intersects = []
	wire1keys = wires[0].keys()
	wire2keys = wires[1].keys()
	for i in wire1keys:
		if i in wire2keys:
				intersects.append(wires[0][i] + wires[1][i])
	return (intersects)

input = getInput("inputs/i03")
wires = processWires(input)
intersects = getIntersect(wires)
intersects.sort()
print (intersects[1])
