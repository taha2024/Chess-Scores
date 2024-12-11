# Taha Ahmad 101065676
'''
This is the main function, responsible for the user interface.

@params			none
@return			none
'''
def main():
	# prints instructions to the screen
	print("Instructions: In this program you must provide the current state of the chessboard. With this current state you can choose to calcualte score or move a piece. This program uses the relative value system in order to calcualte the score and show who's currently winning the game.")
	# creates a loop
	while True:
		# prints main menu to the screen
		print("MAIN MENU")
		# prints options to the screen
		print("(Enter the letter corresponding to the option you would like to use):\nA. LOAD CHESSBOARD\nB. SCORE\nC. MOVE PIECE\nD. QUIT")
		# asks user to input the option they would like to use
		option = input("Select and option: ")
		# checks if the input is the letter a or A
		if option == "a" or option == "A":
			# calls the current_state function and stores the return value in a variable called chessboard
			chessboard = current_state()
			# creates a loop
			for a in range(8):
				# creates a loop
				for b in range(8):
					# prints the value of the chessboard at the index [a][b]
					print(chessboard[a][b], end = "")
				# creates a new line
				print("")
		# checks if the input is the letter b or B
		elif option == "b" or option == "B":
			# runs the following code
			try:
				# calls the score function which takes the argument chessboard and returns the score for white and black
				score_white, score_black = score(chessboard)
				# prints text to screen
				print("According to the relative value system,")
				# prints the score of both teams to the screen
				print('"White" currently has a score of {} and "Black" has a score of {}'.format(score_white, score_black))
				# checks if score_white is bigger than score_black
				if score_white > score_black:
					# prints text to the screen saying white team is winning
					print('Therefore "White" is currently winning.')
				# checks if score_white is less than score_black
				elif score_white < score_black:
					# prints text to the screen saying black team is winning
					print('Therefore "Black" is currently winning.')
				# checks if score_white is equal to score_black
				elif score_white == score_black:
					# prints text to the screen saying the game is tied
					print("The game is currently tied.")
			# stops running the above code if the following error occurs
			except UnboundLocalError:
				# prints text to screen
				print("You must first enter the current state of the chessboard in order to calculate the score.")
				# continues loop
				continue
		# checks if the input is the letter c or C
		elif option == "c" or option == "C":
			# runs the following code			
			try:
				# calls the function move_piece which takes the argument chessboard and stores the return value in chessboard
				chessboard = move_piece(chessboard)
				try:
					# creates a loop
					for a in range(8):
						# creates a loop
						for b in range(8):
							# prints the value of the chessboard at the index [a][b]
							print(chessboard[a][b], end = "")
						# creates a new line
						print("")
					# calls the score function which takes the argument chessboard and returns the score for white and black
					score_white, score_black = score(chessboard)
					# prints text to screen
					print("According to the relative value system,")
					# prints the score of both teams to the screen
					print('"White" currently has a score of {} and "Black" has a score of {}'.format(score_white, score_black))
					# checks if score_white is bigger than score_black
					if score_white > score_black:
						# prints text to the screen saying white team is winning
						print('Therefore "White" is currently winning.')
					# checks if score_white is less than score_black
					elif score_white < score_black:
						# prints text to the screen saying black team is winning
						print('Therefore "Black" is currently winning.')
					# checks if score_white is equal to score_black
					elif score_white == score_black:
						# prints text to the screen saying the game is tied
						print("The game is currently tied.")
				except TypeError:
					continue
			# stops running the above code if the following error occurs
			except UnboundLocalError:
				# prints text to screen
				print("You must first enter the current state of the chessboard in order to calculate the score.")
				# continues loop
				continue
		# checks if the input is the letter d or D
		elif option == "d" or option == "D":
			# exits program
			exit()

		# checks if the user input a character other than the ones provided in the main menu
		else:
			# prints text to screen
			print("Invalid input.")
			# continues loop
			continue
'''
This is the current_state function, responsible for getting the current state of the chessboard by using input from the user.

@params			none
@return			chessboard (list of lists or rows containing the values of each position on the chessboard)
'''
def current_state():
	# creates an empty list
	chessboard = []
	# stores the number 0 in the variable 
	white_king_count = 0
	# stores the number 0 in the variable 
	black_king_count = 0
	# creates a list of possbile inputs the user can have for entering the current state of the chessboard
	possible_inputs = ["k", "K", "q", "Q", "b", "B", "n", "N", "r", "R", "p", "P", "-"]
	# creates a loop
	for row in range(8):
		# creates a loop
		while True:
			# gives the variable a value of True
			flag = True
			# creates an empty list
			chessboard_row = []
			# asks the user to input a row from the chessboard
			current_row = input("Enter current row ")
			# checks if the lenght of the row is 8 characters long
			if len(current_row) == 8:
				# creates a loop
				for char in current_row:
					# checks if the char is in the list of possbile_inputs
					if char in possible_inputs:
						# checks if char is equal to k
						if char == "k":
							# adds 1 to the value of white_king_count
							white_king_count += 1
						# checks if char is equal to K
						elif char == "K":
							# adds 1 to the value of black_king_count
							black_king_count += 1
						# checks if white_king_count and black_king_count have values of of 1 or less
						if white_king_count <= 1 and black_king_count <= 1:
							# adds char to chessboard_row
							chessboard_row.append(char)
						# checks if white_king_count has a value greater than 1
						elif white_king_count > 1:
							# sets white_king_count value to 1
							white_king_count = 1
							# sets the value for flag to False
							flag = False
						# checks if black_king_count has a value greater than 1
						elif black_king_count > 1:
							# sets black_king_count value to 1
							black_king_count = 1
							# sets the value for flag to False
							flag = False
					# checks if char is not in possbile_inputs
					else:
						# sets flag to False
						flag = False
				# checks if flag is equal to True
				if flag == True:
					# adds chessboard_row to chessboard
					chessboard.append(chessboard_row)
					# exits loop
					break
				# checks if flag is not equal to True
				else:
					# prints text to screen
					print("Invalid row. Try again.")
					# continue loop
					continue
			# checks if length of row is not equal to 8						
			else:
				# prints text to screen
				print("Invalid row. Try again.")
				# continue loop
				continue
	# returns the list chessboard
	return chessboard

'''
This is the score function, responsible for calculating the score of the game.

@params			chessboard
@return			score_white (variable containing an integer value representing the score of the white team), score_black (variable containing an integer value representing the score of the black team)
'''
def score(chessboard):
	# sets score for white to 0
	score_white = 0
	# sets score for black to 0
	score_black = 0
	# creates a loop
	for row in range(8):
		# creates a loop
		for column in range(8):
			# checks if value is q
			if chessboard[row][column] == "q":
				# adds 10 to the score of white
				score_white += 10
			# checks if value is Q
			elif chessboard[row][column] == "Q":
				# adds 10 to the score of black
				score_black += 10
			# checks if value is r
			elif chessboard[row][column] == "r":
				# adds 5 to the score of white
				score_white += 5
			# checks if value is R
			elif chessboard[row][column] == "R":
				# adds 5 to the score of black
				score_black += 5
			# checks if value is n
			elif chessboard[row][column] == "n":
				# adds 3.5 to the score of white
				score_white += 3.5
			# checks if value is N
			elif chessboard[row][column] == "N":
				# adds 3.5 to the score of black
				score_black += 3.5
			# checks if value is b 
			elif chessboard[row][column] == "b":
				# adds 3 to the score of white
				score_white += 3
			# checks if value is B
			elif chessboard[row][column] == "B":
				# adds 3 to the score of black
				score_black += 3
			# checks if value is p
			elif chessboard[row][column] == "p":
				# adds 1 to the score of white
				score_white += 1
			# checks if value is P
			elif chessboard[row][column] == "P":
				# adds 1 to the score of black
				score_black += 1
	# returns the score of white and the score of black
	return score_white, score_black

'''
This is the move_piece function, responsible for moving a piece from one position to another.

@params			chessboard
@return			chessboard (list of lists or rows containing the values of each position on the chessboard)
'''
def move_piece(chessboard):
	# creates a loop
	while True:
		# asks user for input
		piece_coord_x = input("Enter the x coordinates of the piece you would like to move (0-7) ")
		# asks user for input
		piece_coord_y = input("Enter the y coordinates of the piece you would like to move (0-7) ")
		# checks if the lenght of both inputs are bigger than or smaller than 1
		if 1 > len(piece_coord_x) > 1 or 1 > len(piece_coord_y) > 1:
			# continues loop
			continue
		# checks if the lenght of both inputs are equal to 1
		else:
			# checks if the ascii values of the input are between or equal to the ascii values of 0 and 7
			if "0" <= piece_coord_x <= "7":
				# checks if the ascii values of the input are between or equal to the ascii values of 0 and 7
				if "0" <= piece_coord_y	<= "7":
					# sets value of variable to 0
					int_piece_coord_x = 0
					# creates a loop
					for num in piece_coord_x:
						# creates a loop
						for integer in '01234567':
							# checks if ascii value of num is bigger than ascii value of integer
							if num > integer:
								# adds 1 to the value of the variable
								int_piece_coord_x += 1
					# sets value of variable to 0
					int_piece_coord_y = 0
					# creates a loop
					for num in piece_coord_y:
						# creates a loop
						for integer in '01234567':
							# checks if ascii value of num is bigger than ascii value of integer
							if num > integer:
								# adds 1 to the value of the variable
								int_piece_coord_y += 1
					# checks if the value of the chessboard at the specified location is -
					if chessboard[int_piece_coord_x][int_piece_coord_y] == "-":
						# prints text to the screen
						print("There's no piece at these coordinates.")
						#returns the unchanged chessboard
						return chessboard
					# checks if the value ofthe chessboard at the specified location is other than -
					else:
						# asks user for input
						move_coord_x = input("Enter the x coordinates of where you want to move the piece (0-7) ")
						# asks user for input
						move_coord_y = input("Enter the y coordinates of where you want to move the piece (0-7) ")
						# checks if lenght of both inputs are bigger or smaller than 1
						if 1 > len(move_coord_x) > 1 or 1 > len(move_coord_y) > 1:
							# continues loop
							continue
						# checks if the lenght of both inputs are equal to 1
						else:
							# checks if the ascii values of the input are between or equal to the ascii values of 0 and 7 
							if "0" <= move_coord_x <= "7":
								# checks if the ascii values of the input are between or equal to the ascii values of 0 and 7
								if "0" <= move_coord_y	<= "7":
									# sets value of variable to 0
									int_move_coord_x = 0
									# creates a loop
									for num in move_coord_x:
										# creates a loop
										for integer in '01234567':
											# checks if ascii value of num is bigger than ascii value of integer
											if num > integer:
												# adds 1 to the value of the variable
												int_move_coord_x += 1
									# sets the value of the variable to 1
									int_move_coord_y = 0
									# creates a loop
									for num in move_coord_y:
										# creates a loop
										for integer in '01234567':
											# checks if ascii value of num is bigger than ascii value of integer
											if num > integer:
												# adds 1 to the value of the variable 
												int_move_coord_y += 1
									# variable to hold the value of the piece being moved
									swap_variable = chessboard[int_piece_coord_x][int_piece_coord_y]
									# sets the move position to -
									chessboard[int_move_coord_x][int_move_coord_y] = "-"
									# sets the original position of the piece to -
									chessboard[int_piece_coord_x][int_piece_coord_y] = "-"
									# moves the piece to the position specified by the user
									chessboard[int_move_coord_x][int_move_coord_y] = swap_variable
									# returns the chessboard
									return chessboard
				# checks if input was invalid
				else:
					# prints text to screen
					print("Invalid input.")
					# continues loop
					continue
			# checks if input was invalid
			else:
				# prints text to screen
				print("Invalid input.")
				# continues loop
				continue

# calls the main function
main()
