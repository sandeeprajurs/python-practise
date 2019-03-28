list = [" "," "," "," "," "," "," "," "," "]


def board():
	""" Created a blank board """

	global list
	print list[0]+"  | "+list[1]+" | "+list[2]
	print "---+---+---"
	print list[3]+"  | "+list[4]+" | "+list[5]
	print "---+---+---"
	print list[6]+"  | "+list[7]+" | "+list[8]


def user1_input():
	""" User 1 input """

	move=raw_input("Player1: What is your next move(1-9)?")
	type(move)

	if list[int(move)-1] == " ":
		list[int(move)-1] = "X"
	else:
		print "Place is already filled. Please select different place"
		user1_input()
		return

	board()
	game_status = check_for_winner_looser("X")
	return game_status


def user2_input():
	""" User 2 input """

	move=raw_input("Player2: What is your next move(1-9)?")
	type(move)

	if list[int(move)-1] == " ":
		list[int(move)-1] = "O"
	else:
		print "Place is already filled. Please select different place"
		user2_input()
		return 

	board()
	game_status = check_for_winner_looser("O")
	return game_status


def controller():
	""" Gives chance to player to make their moves """

	for chance in range(1,10):
		if chance % 2 == 0:
			if user2_input() == "stop":
				return
		else:
			if user1_input() == "stop":
				return
	print "Game is draw"

def find_who_is_winner(symbol):
		""" Finds who is the winner based on the symbol """

		if symbol == "X":
			print "Player1 is winner"
			return "stop"
		else:
			print "Player2 is winner"
			return "stop"

def check_for_winner_looser(symbol):
	""" This function checks the winning condition """

	if list[0] == symbol and list[1] == symbol and list[2] == symbol\
	or list[3] == symbol and list[4] == symbol and list[5] == symbol\
	or list[6] == symbol and list[7] == symbol and list[8] == symbol:
		return find_who_is_winner(symbol)
		
	elif list[0] == symbol and list[4] == symbol and list[8] == symbol\
	or list[2] == symbol and list[4] == symbol and list[6] == symbol:
		return find_who_is_winner(symbol)

	elif list[0] == symbol and list[3] == symbol and list[6] == symbol\
	or list[1] == symbol and list[4] == symbol and list[7] == symbol\
	or list[2] == symbol and list[5] == symbol and list[8] == symbol:
		return find_who_is_winner(symbol)

board()
controller()