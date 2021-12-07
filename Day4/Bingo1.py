import math

#check for winning rows
def checkRows(board):

#check for winning columns
def checkColumns(board):

#check a board to see if it's a winner
def isWinner(board):

#check if a number is found on the board, if yes, replace it
def markNumber(board, number):

inFile = open("input.txt", 'r')

numLine = inFile.readLine().split(',')
numList = []

for num in numLine():
	numList.append(int(num))

#try marking a number on a board, if successful, check if it's a winner, if not, move on