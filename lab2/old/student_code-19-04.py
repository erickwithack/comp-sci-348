QUEENS = 10

def gradient_search(board):
	finish_flag = False
	possible_attack = []
	possible_attack_index = []

	new_board = copy_board(board)
	
	while not finish_flag:
		
		for col_index in range(QUEENS):
			col_attacks_list = num_of_attacks(board, col_index)
			possible_attack.append(min(col_attacks_list))
			possible_attack_index.append(find_min_index(col_attacks_list))

		min_col_index = find_min_index(possible_attack)
		min_row_index = possible_attack_index[min_col_index]

		for row in new_board:
			row[min_col_index] = 0

		new_board[min_row_index][min_col_index] = 1

		finish_flag = True

		for i in range(len(new_board)):
			if new_board[i] != board[i]:
				finish_flag = False
		
		board = copy_board(new_board)


def copy_board(board):
	new_board = []
	for row in board:
		new_board.append(row[:])
	
	return new_board


def find_min_index(current_list):
	return current_list.index(min(current_list))


def num_of_attacks(board, col_index):
	col_attacks_list = []

	for i in range(QUEENS):
		count = 0
		if sum(board[i][:col_index]) > 0:
			count += 1
		if sum(board[i][col_index+1:]) > 0:
			count += 1

		diag_up_right = []
		diag_down_right = []
		diag_up_left = []
		diag_down_left = []

		for j in range(1, col_index):
			if i-j >= 0 and col_index-j >= 0:
				diag_up_left.append(board[i-j][col_index-j])
			if i+j <= QUEENS-1 and col_index-j >= 0:
				diag_down_left.append(board[i+j][col_index-j])

		for k in range(col_index+1, QUEENS):
			if i-(k-col_index) >= 0 and k <= QUEENS-1:
				diag_up_right.append(board[i-(k-col_index)][k])
			if i+(k-col_index) <= QUEENS-1 and k <= QUEENS-1:
				diag_down_right.append(board[i+(k-col_index)][k])

		if sum(diag_up_right) > 0:
			count += 1
		if sum(diag_down_right) > 0:
			count += 1
		if sum(diag_up_left) > 0:
			count += 1
		if sum(diag_down_left) > 0:
			count += 1

		col_attacks_list.append(count)

	return col_attacks_list



data = ("0000000100"
		"0000000000"
		"0000100000"
		"0010000010"
		"1000000000"
		"0000010000"
		"0001000000"
		"0100000000"
		"0000001001"
		"0000000000")

def init_board():
	return [[0 for x in range(0,10)] for x in range(0,10)]
	
def set_board(board, data):
	for y in range(0,10):
		for x in range(0,10):
			board[y][x]=int(data[y*10+x])
	return board

board = init_board()
board = set_board(board, data)
print(board)

print(num_of_attacks(board, 2))