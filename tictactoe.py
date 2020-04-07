'''
Tic tac toe med general sized grid, defaults to 3

'''
import os
import sys
import console


class grid():
	# Initialize the grid, default size is 3x3.
	# Empty spots characterized by '_'
	def __init__(self, width=0, size = 3):
		self.size = size
		self.grid = [['_']*size for i in range(size)]
		self.width = width

	def print_old(self):
		for row in range(self.size):
			for column in range(self.size):
				print(self.grid[row][column], end=' ')
			print()


	def print(self):
		if self.width==0:
			self.print_old()
		else:
			for row in range(self.size):
				tmp = ''
				for column in range(self.size):
					tmp = tmp + self.grid[row][column] + ' '
				
				centered = tmp.center(self.width)
				print(centered)



	# Can not just check for same pieces in rows/columns/diagonals
	def check_win(self, player1):

		# Check for 3 consecutive pieces in all rows
		for row in range(self.size):
			consecutive = 0
			for col in range(self.size):
				if self.grid[row][col] != '_':
					if col == 0:
						consecutive += 1
					else:
						if self.grid[row][col] == self.grid[row][col-1]:
							consecutive += 1
						else:
							consecutive = 1
				if consecutive == 3:
					if self.grid[row][col]=='X':
						print()
						print("Player one was victorious! Game over".center(self.width))
						sys.exit(0)
					else:
						print()
						print("Player two was victorious! Game over".center(self.width))
						sys.exit(0)

		# Check for 3 consecutive pieces in all columns
		for col in range(self.size):
			consecutive = 0
			for row in range(self.size):
				if self.grid[row][col] != '_':
					if row == 0:
						consecutive += 1
					else:
						if self.grid[row][col] == self.grid[row-1][col]:
							consecutive += 1
						else:
							consecutive = 1
				if consecutive == 3:
					if self.grid[row][col]=='X':
						print()
						print("Player one was victorious! Game over".center(self.width))
						sys.exit(0)
					else:
						print()
						print("Player two was victorious! Game over".center(self.width))
						sys.exit(0)

		# Left to right diagonal
		for index in range(self.size):
				if self.grid[index][index] != '_':
					if index==0:
						consecutive = 1
					else:
						if self.grid[index][index] == self.grid[index-1][index-1]:
							consecutive += 1
						else:
							consecutive = 1
				if consecutive == 3:
					if self.grid[index][index] == 'X':
						print()
						print("Player one was victorious! Game over".center(self.width))
						sys.exit(0)
					else:
						print()
						print("Player two was victorious! Game over".center(self.width))
						sys.exit(0)

		# Extra diagonals, left to right
		extra_diagonals = self.size - 3
		if extra_diagonals>0:
			for extra in range(extra_diagonals):
				consecutive = 0
				extra += 1
				for index in range(self.size-extra):
					if self.grid[index][index+extra] != '_':
						if index==0:
							consecutive = 1
						else:
							if self.grid[index][index+extra] == self.grid[index-1][index+extra-1]:
								consecutive += 1
							else:
								consecutive = 1
					if consecutive == 3:
						if self.grid[index][index+extra] == 'X':
							print()
							print("Player one was victorious! Game over".center(self.width))
							sys.exit(0)
						else:
							print()
							print("Player two was victorious! Game over".center(self.width))
							sys.exit(0)

				consecutive = 0
				for index in range(self.size-extra):
					if self.grid[index+extra][index] != '_':
						if index==0:
							consecutive = 1
						else:
							if self.grid[index+extra][index] == self.grid[index+extra-1][index-1]:
								consecutive += 1
							else:
								consecutive = 1
					if consecutive == 3:
						if self.grid[index+extra][index] == 'X':
							print()
							print("Player one was victorious! Game over".center(self.width))
							sys.exit(0)
						else:
							print()
							print("Player two was victorious! Game over".center(self.width))
							sys.exit(0)				


		# Right to left diagonal
		for index in range(self.size):
				if self.grid[index][self.size-1-index] != '_':
					if index==0:
						consecutive = 1
					else:
						if self.grid[index][self.size-1-index] == self.grid[index-1][self.size-index]:
							consecutive += 1
						else:
							consecutive = 1
				if consecutive == 3:
					if self.grid[index][self.size-1-index] == 'X':
						print()
						print("Player one was victorious! Game over".center(self.width))
						sys.exit(0)
					else:
						print()
						print("Player two was victorious! Game over".center(self.width))
						sys.exit(0)

		# Extra diagonals, right to left				
		if extra_diagonals>0:
			for extra in range(extra_diagonals):
				consecutive = 0
				extra += 1
				for index in range(self.size-extra):
					if self.grid[index][self.size-1-extra-index] != '_':
						if index==0:
							consecutive = 1
						else:
							if self.grid[index][self.size-1-extra-index] == self.grid[index-1][self.size-index-extra]:
								consecutive += 1
							else:
								consecutive = 1
					if consecutive == 3:
						if self.grid[index][self.size-1-extra-index] == 'X':
							print()
							print("Player one was victorious! Game over".center(self.width))
							sys.exit(0)
						else:
							print()
							print("Player two was victorious! Game over".center(self.width))
							sys.exit(0)

				consecutive = 0
				for index in range(self.size-extra):
					if self.grid[index+extra][self.size-1-index] != '_':
						if index==0:
							consecutive = 1
						else:
							if self.grid[index+extra][self.size-1-index] == self.grid[index+extra-1][self.size-index]:
								consecutive += 1
							else:
								consecutive = 1
					if consecutive == 3:
						if self.grid[index+extra][self.size-1-index] == 'X':
							print()
							print("Player one was victorious! Game over".center(self.width))
							sys.exit(0)
						else:
							print()
							print("Player two was victorious! Game over".center(self.width))
							sys.exit(0)				


def check_move_to(grid, row, col):
	return grid.grid[row][col] == '_'

def check_move_from(grid, player1, row, col):
	if player1:
		return grid.grid[row][col] == 'X'
	else:
		return grid.grid[row][col] == 'O' 


def check_row(grid, input_row):
	return input_row in range(1, grid.size+1)

def check_col(grid, input_col):
	return input_col in range(1, grid.size+1)

def get_col(grid):
	while True:
			try:
				col = int(input("Column: "))
				if col == 999:
					sys.exit(1)
				valid_col = check_row(grid, col)
				if valid_col:
					break
				else:
					print("Column not in correct range. Valid range is 1 to", grid.size)
			except:
				if row == 999:
					print("Thanks for playing! Hope to see you soon again".center(grid.width))
					sys.exit(1)
				print("Invalid column. Column has to be integer value")
	return col

def get_row(grid):
	while True:
		try:
			row = int(input("Row: "))
			if row == 999:
				sys.exit(1)
			valid_row = check_row(grid, row)
			if valid_row:
				break
			else:
				print("Row not in correct range. Valid range is 1 to", grid.size)
		except:
			if row == 999:
				print("Thanks for playing! Hope to see you soon again".center(grid.width))
				sys.exit(1)
			print("Invalid row. Row has to be integer value")
	return row

def move_from(player1, grid):
	valid_move = False
	if player1:
		print("Player one to enter first row then column for where to move piece from")
		while True:
			if valid_move:
				grid.grid[row-1][col-1] = '_'
				print("Valid move!")
				break
			else:

				row = get_row(grid)
				col = get_col(grid)			
				valid_move = check_move_from(grid, player1, row-1, col-1)
				if not valid_move:
					print("Invalid combination of row and column")

	else:
		print("Player two to enter first row then column for where to move piece from")
		while True:
			if valid_move:
				grid.grid[row-1][col-1] = '_'
				print("Valid move!")
				break
			else:

				row = get_row(grid)
				col = get_col(grid)			
				valid_move = check_move_from(grid, player1, row-1, col-1)
				if not valid_move:
					print("Invalid combination of row and column")



def move_to(player1, grid):
	valid_move = False
	if player1:
		print("Player one to enter first row then column for where to place piece")
		while True:

			if valid_move:
				grid.grid[row-1][col-1] = 'X'
				break
			else:

				row = get_row(grid)
				col = get_col(grid)			
				valid_move = check_move_to(grid, row-1, col-1)
				if not valid_move:
					print("Invalid combination of row and column")

	else:
		print("Player two to enter first row then column for where to place piece")
		while True:
			if valid_move:
				grid.grid[row-1][col-1] = 'O'
				break
			else:

				row = get_row(grid)
				col = get_col(grid)			
				valid_move = check_move_to(grid, row-1, col-1)
				if not valid_move:
					print("Invalid combination of row and column")




width, height = console.getTerminalSize()
os.system('cls' if os.name == 'nt' else 'clear')


print(''.center(width, '*'))
print(''.center(width, '*'))
print()

print("Hello and welcome to Tic Tac Toe by Erik!".center(width))
print("Here, players must make valid moves each round and can not pass on move".center(width))
print("Player one will be 'X', player two will be 'O and empty spots are symbolized by '_'".center(width))
print("At any time, enter 999 to exit the game".center(width))

print()
print(''.center(width, '*'))
print(''.center(width, '*'))

print()

start_text = "Let the game begin!"
centered = start_text.center(width)
print(centered)

if len(sys.argv) > 1:
	try:
		grid_size = int(sys.argv[1])
		if grid_size < 3:
			print("Tic tac toe not very fun with grid size < 3...".center(width))
			print("Setting default size, 3".center(width))
			grid_size = 3
	except:
		print("Had trouble reading grid size. Only integer values accepted".center(width))
		print("Setting default size, 3".center(width))
else:
	grid_size = 3

won = False
player1 = True
grid = grid(width = width, size = grid_size)

grid.print()

# First 6 rounds, no pieces are picked up
for i in range(3):
	move_to(player1, grid)
	grid.print()
	grid.check_win(player1)
	player1 = not player1
	
	move_to(player1, grid)
	grid.print()
	player1 = not player1

won = grid.check_win(not player1)
while not won: 

	move_from(player1, grid)
	grid.print()
	move_to(player1, grid)
	grid.print()
	won = grid.check_win(player1)
	player1 = not player1	



'''

Fix check_win
Extra effects?

Ghraphical version of game
Suduko solver?

'''










