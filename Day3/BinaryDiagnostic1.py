import math

report = open("input.txt")

sums = [0] * 12 #https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
gamma = [0] * 12
epsilon = [0] * 12

#get the sum of the number of 1s in each binary position
for diagnostic in report:
	for bit in range(12):
		sums[bit] += int(diagnostic[bit])

for bit in range(12):
	if sums[bit] < 500:
		gamma[bit] = 0
		epsilon[bit] = 1
	elif sums[bit] > 500:
		gamma[bit] = 1
		epsilon[bit] = 0
	else: #case never covered
		print('something has gone horribly wrong')

gammaString = ""
epsilonString = ""

for bit in gamma:
	gammaString += str(bit)

for bit in epsilon:
	epsilonString += str(bit)


gammaInt = int(gammaString, 2)
epsilonInt = int(epsilonString, 2)

print('Power consumption: ' + str(gammaInt * epsilonInt))