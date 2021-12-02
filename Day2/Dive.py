import math

instructions = open("input.txt")

depth = 0
horizontal = 0

for line in instructions:
	direction, amount = line.split(" ")
	amount = int(amount)
	if direction == 'up':
		depth -= amount
	elif direction == 'down':
		depth += amount
	elif direction == 'forward':
		horizontal += amount
	else:
		print('Something has gone horrible wrong')

print(horizontal * depth)