import math

instructions = open("input.txt")

depth = 0
horizontal = 0
aim = 0

for line in instructions:
	direction, amount = line.split(" ")
	amount = int(amount)
	if direction == 'up':
		aim -= amount
	elif direction == 'down':
		aim += amount
	elif direction == 'forward':
		horizontal += amount
		depth += (aim * amount)
	else:
		print('Something has gone horrible wrong')

print(horizontal * depth)