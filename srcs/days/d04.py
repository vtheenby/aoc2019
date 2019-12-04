
def checkDouble(l):
	ans = []
	count = 1
	for i in range(len(l) - 1):
		if l[i] == l[i + 1]:
			count += 1
		else:
			ans.append(count)
			count = 1
	ans.append(count)
	for i in ans:
		if i is 2:
			return (True)
	return (False)


def checkIncrement(lst):
	prev = 0
	for n in lst:
		if prev > n:
			return (False)
		prev = n
	return (True)

def checkPass(n):
	valid = True
	lst = [int(x) for x in str(n)]
	if not checkIncrement(lst):
		valid = False
	if not checkDouble(lst):
		valid = False
	return (valid)

def secureContainer(input):
	total = 0
	for n in range(input[0], input[1]):
		if checkPass(int(n)):
			total += 1
	return (total)

input = [356261, 846303]

print(secureContainer(input))