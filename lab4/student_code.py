import common


def minmax_tictactoe(board, turn):
    """ Returns an integer representing the winner of the game under optimal play,
    1 for X, 2 for O and 0 for tie, using min-max to explore the entire solution space.
    """
    # initialize a,b = None
    a, b = None, None

    # Find result
    result = check_turn(board, turn, a, b)

    return return_result(result)


def abprun_tictactoe(board, turn):
    """ Returns an integer representing the winner of the game,
    1 for X, 2 for O and 0 for tie, using alpha-beta pruning to trim the solution space.
    """
    # initialize a = -infinity , b = +infinity
    a, b = -1000000, 1000000

    # Find result
    result = check_turn(board, turn, a, b)

    return return_result(result)


def max_value(board, a, b):
    """ Returns the maximum value for thr board.
    """
    # initialize v = -infinity
    v = -1000000

    # Check state
    result = common.game_status(board)

    # Check results
    if result == common.constants.X:
        return 1

    elif result == common.constants.O:
        return -1

    elif check_tie(board):
        return 0

    # If game is not finished - check the value of v
    for i in range(3):
        for j in range(3):
            if common.get_cell(board, i, j) == common.constants.NONE:
                new_board = board[:]
                common.set_cell(new_board, i, j, common.constants.X)
                v = max(v, min_value(new_board, a, b))

                # For abprun_tictactoe()
                if (a is not None) and (b is not None):
                    if v >= b:
                        return v
                    a = max(a, v)
    return v


def min_value(board, a, b):
    """ Returns the minimum value for thr board.
    """
    # initialize v = +infinity
    v = 1000000

    # Check state
    result = common.game_status(board)

    # Check results
    if result == common.constants.X:
        return 1

    elif result == common.constants.O:
        return -1

    elif check_tie(board):
        return 0

    # If game is not finished - check the value of v
    for i in range(3):
        for j in range(3):
            if common.get_cell(board, i, j) == common.constants.NONE:
                new_board = board[:]
                common.set_cell(new_board, i, j, common.constants.O)
                v = min(v, max_value(new_board, a, b))

                # For abprun_tictactoe()
                if (a is not None) and (b is not None):
                    if v <= a:
                        return v
                    b = min(b, v)
    return v


def check_tie(board):
    """ Checks if the board's state is tie.
    """
    for element in board:
        if not element:
            return False

    return True


def check_turn(board, turn, a, b):
    """ Checks the minimum/maximum result for this turn.
    """
    result = common.constants.NONE

    if turn == common.constants.X:
        result = max_value(board, a, b)

    elif turn == common.constants.O:
        result = min_value(board, a, b)

    return result


def return_result(result):
    """ Returns the appropriate result for this turn.
    """
    if result == 1:
        return common.constants.X

    elif result == -1:
        return common.constants.O

    return common.constants.NONE
