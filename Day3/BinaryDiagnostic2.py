import math

#determine the most common bit in the given list at the given position
def mostCommonBit(values, position):
	ones = 0 #how many bits '1' bits in the given position
	for val in values:
		if val[position] == '1':
			ones += 1

	if ones >= len(values)/2:
		return '1'
	else:
		return '0'

#determine the least common bit in the given list at the given position
def leastCommonBit(values, position):
	zeros = 0 #how many bits '1' bits in the given position
	for val in values:
		if val[position] == '0':
			zeros += 1

	if zeros > len(values)/2:
		return '1'
	else:
		return '0'

#determine the oxygen rating recursively
def oxygenRating(values, bitPosition):
	if len(values) == 1: #if there is only one value left
		return values

	else:
		newList = [] #for values that fit the unreasonable standards we've set for them go
		mostCommon = mostCommonBit(values, bitPosition)

		for val in values:
			if val[bitPosition] == mostCommon: #if the bit matches our most common bit
				newList.append(val) #add the value to our new list

		return oxygenRating(newList, bitPosition + 1) #do it again with the new list and the next position

#determine the oxygen rating recursively
def CO2Rating(values, bitPosition):
	if len(values) == 0:
		stop
	if len(values) == 1: #if there is only one value left
		return values

	else:
		newList = [] #for values that fit the unreasonable standards we've set for them go
		leastCommon = leastCommonBit(values, bitPosition)
		
		for val in values:
			if val[bitPosition] == leastCommon: #if the bit matches our most common bit
				newList.append(val) #add the value to our new list

		return CO2Rating(newList, bitPosition + 1) #do it again with the new list and the next position


report = open("input.txt")
diagnostics = [] #the list to hold the inputs

#get the input into a list
for diagnostic in report:
	diagnostics.append(diagnostic.strip('\n'))

oxygen = int(oxygenRating(diagnostics, 0)[0], 2)
CO2 = int(CO2Rating(diagnostics, 0)[0], 2)

print('Oxygen Generator rating: ', oxygen)
print('CO2 Scrubber rating: ', oxygen)
print('Life Support rating: ', oxygen * CO2)
