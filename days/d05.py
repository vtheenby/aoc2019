class Opcode:
	opcode = 0
	modes = []
	

def getInput(filename):
	ret = []
	cool = []
	with open(filename) as f:
		ret = f.readline()
	ret = ret.split(',')
	for i in ret:
		cool.append(int(i))
	return (cool)

#for opcode 1

def applyAdd(intc, x, modes):
	n1 = intc[x + 1]
	n2 = intc[x + 2]
	pos = intc[x + 3]
	val = intc[n1] + intc[n2]
	intc[pos] = val
	return (intc)

#for opcode 2

def applyMul(intc, x, modes):
	n1 = intc[x + 1]
	n2 = intc[x + 2]
	pos = intc[x + 3]
	l = setModes(n1, n2, modes)
	val = intc[l[0]] * intc[l[1]]
	intc[pos] = val
	return (intc)

#for opcode 3

def applyStore(intc, x, input):
	pass

#for opcode 4

def outputVal(intc, x):
	pass

def setModes(intc, n1, n2, modes):
	l = []
	i = 0
	while i < len(modes) - 2:
		pass


def getModes(n):
	n = [int(x) for x in str(n)]
	while (len(n) < 5):
		n.insert(0, 0)
	if (n[-1] is 4 or n[-1] is 3):
		del n[0:2]
	del n[-1]
	del n[-1]
	return (n)

def intCode(intc, input):
	pos = 0
	op = Opcode()
	while opcode is not 99:
		op.opcode = intc[pos + 0] % 100
		op.modes = getModes(intc[pos + 0])
		if op.opcode is 1:
			intc = applyAdd(intc, pos, op.modes)
			pos += 4
		elif op.opcode is 2:
			intc = applyMul(intc, pos, op.modes)
			pos += 4
		elif op.opcode is 3:
			intc = applyStore(intc, pos, input, op.modes)
			pos += 2
		elif op.opcode is 4:
			outputVal(intc, pos, op.modes)
			pos += 2

print(getModes('103'))