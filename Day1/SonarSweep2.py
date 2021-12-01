import math
import collections

measurements = open("input1.txt")

#deque to represent the sliding window
window = collections.deque()
currSum = 0

while len(window) < 3:
	measurement = int(measurements.readline())
	currSum += measurement
	window.append(measurement)

increases = 0

for depth in measurements:
	newSum = currSum - window.popleft() + int(depth)
	if newSum > currSum:
		increases += 1

	window.append(int(depth))
	currSum = newSum

print(increases)