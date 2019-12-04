def fileToIntList(input):
	ret = []
	with open(input) as f:
		for l in f.readlines():
			l = int(l)
			ret.append(l)
	return (ret)

def calcFuel(n):
	total = 0
	total += int(n / 3 - 2)
	return (total)

def fuelFuel(input):
	total = 0
	for n in input:
		fuel = calcFuel(n)
		while fuel >= 0:
			total += fuel
			fuel = calcFuel(fuel)
	return (total)

input = fileToIntList("inputs/i01")

print (fuelFuel(input))