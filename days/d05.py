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

def applyAdd(intc, x):
	n1 = intc[x + 1]
	n2 = intc[x + 2]
	pos = intc[x + 3]
	val = intc[n1] + intc[n2]
	intc[pos] = val
	return (intc)

#for opcode 2

def applyMul(intc, x):
	n1 = intc[x + 1]
	n2 = intc[x + 2]
	pos = intc[x + 3]
	val = intc[n1] * intc[n2]
	intc[pos] = val
	return (intc)

#for opcode 3

def applyStore(intc, x, input):
	pass

#for opcode 4

def outputVal(intc, x):
	pass

def setModes(n):
	if len(n) == se

def getModes(n):
	n = [int(x) for x in str(n)]
	del n[-2]
	l = len(n)
	modes = []
	if 
	return (modes)

def intCode(intc, input):
	pos = 0
	op = Opcode()
	while opcode is not 99:
		op.opcode = intc[pos + 0] % 100
		op.modes = getModes(intc[pos + 0])
		if op.opcode is 1:
			intc = applyAdd(intc, pos, modes)
			pos += 4
		elif op.opcode is 2:
			intc = applyMul(intc, pos, modes)
			pos += 4
		elif op.opcode is 3:
			intc = applyStore(intc, pos, input, modes)
			pos += 2
		elif op.opcode is 4:
			outputVal(intc, pos, modes)
			pos += 2

n = getModes(2019)
