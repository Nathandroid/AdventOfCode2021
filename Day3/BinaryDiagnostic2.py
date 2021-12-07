import math

report = open("input.txt")

sums = [0] * 12 #https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
gamma = [0] * 12
epsilon = [0] * 12
diagnostics = [] #the list to hold the inputs

#get the sum of the number of 1s in each binary position
for diagnostic in report:
	for bit in range(12):
		sums[bit] += int(diagnostic[bit])
	diagnostics.append(diagnostic.strip('\n'))



mostCommon = [0] * 12

for x in range(12):
	if sums[x] < 500:
		mostCommon[x] = '0'
	elif sums[x] >= 500:
		mostCommon[x] = '1'

oxygenList = []
CO2List = []

#first pass through the list
for diagnostic in diagnostics:
	if mostCommon[0] == diagnostic[0]:
		oxygenList.append(diagnostic)
	else:
		CO2List.append(diagnostic)

'''At this point, we have two lists:
	One list with all numbers beginning with the most common bit, 0
	One list with all numbers beginning with the least common bit, 1 '''

#first the oxygen list
tempList = []

for bit in range(12):
	sums[bit] = 0

for x in range(1, 12):

	for num in oxygenList:#for every remaining number in the oxygen list
		sums[x] += int(num[x]) #add the bit to sums

	if sums[x] < (len(oxygenList)/2):
		mostFrequent = '0'
	else:
		mostFrequent = '1'

	for num in oxygenList:
		if num[x] == mostFrequent:
			tempList.append(num)

	oxygenList = tempList.copy() #reset oxygenList
	tempList = [] #clear temp list

print(oxygenList)

#now the CO2 list
tempList = []

for bit in range(12):
	sums[bit] = 0

for x in range(1, 12):

	for num in CO2List:#for every remaining number in the CO2 list
		sums[x] += int(num[x]) #add the bit to sums

	if sums[x] > (len(CO2List)/2):
		leastFrequent = '0'
	else:
		leastFrequent = '1'

	for num in CO2List:
		if num[x] == leastFrequent:
			tempList.append(num)

	CO2List = tempList.copy() #reset oxygenList
	tempList = [] #clear temp list

print(CO2List)