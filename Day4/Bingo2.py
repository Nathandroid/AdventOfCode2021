import math
import numpy

#check for winning rows
def checkRows(board):
	for row in range(len(board)):
		numMarked = 0
		for col in range(len(board)):
			if board[row][col] == -1:
				numMarked += 1
		if numMarked == 5: #if it's a winning row
			return(True)
	return(False)

#check for winning columns
def checkColumns(board):
	for col in range(len(board)):
		numMarked = 0
		for row in range(len(board)):
			if board[row][col] == -1:
				numMarked += 1
		if numMarked == 5: #if it's a winning column
			return(True)
	return(False)

#check a board to see if it's a winner
def isWinner(board):
	return checkRows(board) or checkColumns(board)

#check if a number is found on the board, if yes, replace it with -1
def markNumber(board, number):
	for row in range(len(board)):
		for col in range(len(board)):
			if board[row][col] == number:#if the current spot matches the called number
				board[row][col] = - 1 #replace the called number with -1
				return

#calculate the score by adding together non-negative values
def calculateScore(board, lastNum):
	sum = 0
	for row in range(len(board)):
		for col in range(len(board)):
			if board[row][col] != -1:
				sum += board[row][col]

	print('Winning board:\n', board)
	print('Winning board\'s score: ', sum * lastNum)


inFile = open("input.txt", 'r')

numLine = inFile.readline()
numLine = numLine.split(',')
numList = []

for num in numLine:
	numList.append(int(num)) #because I hate strings

boards = []

#this will eat every 6th input until EOF
while(inFile.readline()):
	board = [[0]*5 for i in range(5)] #https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
	for row in range(5):
		line = inFile.readline().strip()
		line = line.split()
		board[row] = [int(n) for n in line]
	boards.append(board)

for num in numList: #every time a new number is called
	for board in boards: #check every board
		markNumber(board, num) #mark off given number if present
		if(isWinner(board)): #is this board a winner
			calculateScore(board, num)
			quit()

#try marking a number on a board, if successful, check if it's a winner, if not, move on