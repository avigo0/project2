import random
class Minesweeper():
	_board = []
	_rows = 0
	_cols = 0
	_numOfBombs = 0

	#Constructor
	def __init__(self,height,width,bombs):
		self._rows = height
		self._cols = width
		self._numOfBombs = bombs

		#Create the board
		for row in range(height):
			templst = []
			for col in range(width):
				templst.append(" ")
			self._board.append(templst)
				
		#Generate bombs
		for bomb in range(bombs):
			row = random.randint(0,2)
			col = random.randint(0,2)

			#Check if already a bomb
			while self._board[row][col] == "B":
				row = random.randint(0,2)
				col = random.randint(0,2)

			self._board[row][col] = "B"

	def checkValid(self,row,col):
		'''
		Checks if the coordinate being chosen is a valid option, meaning not out of bounds or already taken.
		'''
		if row >= self._rows:
			return False
		if col >= self._cols:
			return False
		if self._board[row][col] == "X":
			return False
		return True




game = Minesweeper(3,4,3)
print(game.checkValid(2,3))


