QUEENS = 10


def gradient_search(board):
    """ The main gradient search function.
    Uses greedy hill-climbing search to find minima and solutions to the 10- queens problem.
    This problem tries to find a position for all 10 queens on the board where they cannot attack each other.
    Reminder - an attack is whenever a queen shares a row, column, or diagonal with another queen.
    """

    # Initialize the finish flag
    finish_flag = False

    # Initialize the attack value
    for i in range(QUEENS):
        if 1 not in board[i]:
            continue
        col_of_queen_0 = board[i].index(1)
        old_min_value = num_of_attacks(board, i, col_of_queen_0)
        break

    # print_board(board)
    new_board = board

    while not finish_flag:
        board = new_board

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

        new_min_value = min(possible_attack)
        min_col_index = find_min_index(possible_attack)
        min_row_index = possible_attack_index[min_col_index]

        move_queen(new_board, min_row_index, min_col_index)

        if new_min_value == old_min_value:
            finish_flag = True

        old_min_value = new_min_value

    # print_board(board)
    return old_min_value == 0


def move_queen(board, row_index, col_index):
    """ Move a queen to a desired position in the column
    """

    for row in board:
        row[col_index] = 0

    board[row_index][col_index] = 1


def copy_board(board):
    """ Generate a copy of the board
    """

    new_board = []
    for row in board:
        new_board.append(row[:])

    return new_board


def find_min_index(current_list):
    """ Finds the index of the minimum value in a list
    """

    return current_list.index(min(current_list))


def num_of_attacks(board, row_index, col_index):
    """ Calculates the total number of attacks in the board for a single point
    """

    move_queen(board, row_index, col_index)
    count_tot = 0

    for i_row in range(QUEENS):
        for i_col in range(QUEENS):
            if board[i_row][i_col] == 1:
                count_tot += num_of_attacks_for_point(board, i_row, i_col)

    return count_tot


def num_of_attacks_for_point(board, row_index, col_index):
    """ Calculates the number of attacks for a single point
    """

    count = 0
    diag_up_right = []
    diag_down_right = []
    diag_up_left = []
    diag_down_left = []

    # Calculate the number of attacks from queens in the same row
    count += sum(board[row_index][:col_index]) + sum(board[row_index][col_index + 1:])

    # Compute lists of diagonals for the current point (up_left and down_left)
    for j in range(col_index):
        if row_index - j - 1 >= 0:
            diag_up_left.append(board[row_index - j - 1][col_index - j - 1])
        if row_index + j + 1 <= QUEENS - 1:
            diag_down_left.append(board[row_index + j + 1][col_index - j - 1])

    # Compute lists of diagonals for the current point (up_right and down_right)
    for k in range(col_index + 1, QUEENS):
        if row_index - (k - col_index) >= 0:
            diag_up_right.append(board[row_index - (k - col_index)][k])
        if row_index + (k - col_index) <= QUEENS - 1:
            diag_down_right.append(board[row_index + (k - col_index)][k])

    # Calculate the number of attacks from queens in the same diagonal
    count += sum(diag_up_right) + sum(diag_down_right) + sum(diag_up_left) + sum(diag_down_left)

    return count


def print_board(board):
    """ Prints the current board in a readable format
    """

    for row in board:
        print(row)
    print("\n")

