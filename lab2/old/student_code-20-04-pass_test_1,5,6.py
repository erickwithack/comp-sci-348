QUEENS = 10


def gradient_search(board):
    finish_flag = False
    for i in range(QUEENS):
        if 1 not in board[i]:
            continue
        col_of_queen_0 = board[i].index(1)
        old_min_value = num_of_attacks(board, i, col_of_queen_0)  # TODO - what if the first iter is correct
        break

    print_board(board)
    new_board = board
    iteration_number = 0
    while not finish_flag:
        board = new_board

        iteration_number += 1

        possible_attack = []
        possible_attack_index = []

        for col_index in range(QUEENS):
            col_attacks_list = []
            for row_index in range(QUEENS):
                temp_board = copy_board(board)
                count = num_of_attacks(temp_board, row_index, col_index)
                col_attacks_list.append(count)

            possible_attack.append(min(col_attacks_list))
            possible_attack_index.append(find_min_index(col_attacks_list))
            # possible_attack_index.append(find_last(col_attacks_list, min(col_attacks_list)))

        new_min_value = min(possible_attack)
        min_col_index = find_min_index(possible_attack)
        min_row_index = possible_attack_index[min_col_index]

        move_queen(new_board, min_row_index, min_col_index)

        if new_min_value == old_min_value:
            finish_flag = True

        old_min_value = new_min_value

    print_board(board)
    return old_min_value == 0


def find_last(l, item):
    l.reverse()
    indx = l.index(item)
    l.reverse()
    return len(l) - 1 - indx


def move_queen(board, row_index, col_index):
    for row in board:
        row[col_index] = 0

    board[row_index][col_index] = 1


def copy_board(board):
    new_board = []
    for row in board:
        new_board.append(row[:])

    return new_board


def find_min_index(current_list):
    return current_list.index(min(current_list))


def num_of_attacks(board, row_index, col_index):  # TODO - change to total attacks in board
    move_queen(board, row_index, col_index)
    count_tot = 0

    for i_row in range(QUEENS):
        for i_col in range(QUEENS):
            if board[i_row][i_col] == 1:
                count_tot += num_of_attacks_for_point(board, i_row, i_col)

    return count_tot


def num_of_attacks_for_point(board, row_index, col_index):  # TODO - change to total attacks in board
    count = 0
    diag_up_right = []
    diag_down_right = []
    diag_up_left = []
    diag_down_left = []

    # if sum(board[row_index][:col_index]) > 0:
    #     count += 1
    # if sum(board[row_index][col_index + 1:]) > 0:
    #     count += 1
    count += sum(board[row_index][:col_index]) + sum(board[row_index][col_index + 1:])

    for j in range(1, col_index):
        if row_index - j >= 0 and col_index - j >= 0:
            diag_up_left.append(board[row_index - j][col_index - j])
        if row_index + j <= QUEENS - 1 and col_index - j >= 0:
            diag_down_left.append(board[row_index + j][col_index - j])

    for k in range(col_index + 1, QUEENS):
        if row_index - (k - col_index) >= 0 and k <= QUEENS - 1:
            diag_up_right.append(board[row_index - (k - col_index)][k])
        if row_index + (k - col_index) <= QUEENS - 1 and k <= QUEENS - 1:
            diag_down_right.append(board[row_index + (k - col_index)][k])

    # if sum(diag_up_right) > 0:
    #     count += 1
    # if sum(diag_down_right) > 0:
    #     count += 1
    # if sum(diag_up_left) > 0:
    #     count += 1
    # if sum(diag_down_left) > 0:
    #     count += 1
    count += sum(diag_up_right) + sum(diag_down_right) + sum(diag_up_left) + sum(diag_down_left)

    return count


# data = (
#     "1111111111"
#     "0000000000"
#     "0000000000"
#     "0000000000"
#     "0000000000"
#     "0000000000"
#     "0000000000"
#     "0000000000"
#     "0000000000"
#     "0000000000")


# data  = (
# "1000000000"
# "0100000000"
# "0010000000"
# "0001000000"
# "0000100000"
# "0000010000"
# "0000001000"
# "0000000100"
# "0000000010"
# "0000000001")

data =(
"0000000000"
"1000000000"
"0100100000"
"0010010010"
"0000000100"
"0001000000"
"0000000000"
"0000001000"
"0000000000"
"0000000001")


def init_board():
    return [[0 for x in range(0, 10)] for x in range(0, 10)]


def set_board(board, data):
    for y in range(0, 10):
        for x in range(0, 10):
            board[y][x] = int(data[y * 10 + x])
    return board


def print_board(board):
    for row in board:
        print(row)
    print("\n")


board = init_board()
board = set_board(board, data)
gradient_search(board)
