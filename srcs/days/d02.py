#day2 :program alarm
#opcode: 0 = mode 1 = val1 2 = val2 3 = pos
#0 can be 1, 2 or 99, representing add, multiply and terminate
def getInput(filename):
	ret = []
	cool = []
	with open(filename) as f:
		ret = f.readline()
	ret = ret.split(',')
	for i in ret:
		cool.append(int(i))
	return (cool)

def applyAdd(input, x):
	n1 = input[x + 1]
	n2 = input[x + 2]
	pos = input[x + 3]
	val = input[n1] + input[n2]
	input[pos] = val
	return (input)

def applyMul(input, x):
	n1 = input[x + 1]
	n2 = input[x + 2]
	pos = input[x + 3]
	val = input[n1] * input[n2]
	input[pos] = val
	return (input)

def programAlarm(input):
	pos = 0
	while (input[pos + 0] is not 99):
		if input[pos + 0] is 1:
			input = applyAdd(input, pos)
		elif input[pos + 0] is 2:
			input = applyMul(input, pos)
		pos += 4
	return (input[0])
		
def findOutput():
	for noun in range(0, 99):
		for verb in range(0, 99):
			input = getInput("inputs/i02")
			input[1] = noun
			input[2] = verb
			if (programAlarm(input) == 19690720):
				return (100 * noun + verb)


testInput = [1,1,1,4,99,5,6,0,99]
print(findOutput())