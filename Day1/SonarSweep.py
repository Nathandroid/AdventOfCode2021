import math

measurements = open("input1.txt")

#get the first line
curr = int(measurements.readline())
increases = 0

#check each measurement
for depth in measurements:
	if int(depth) > curr:
		increases += 1

	curr = int(depth)

print(increases)