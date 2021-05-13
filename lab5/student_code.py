import common

SUDOKU_WIDTH = 9
SUDOKU_HEIGHT = 9
AVAILABLE_CELL = 0


class variables:
    """Class for counter"""
    counter = 0


def sudoku_backtracking(sudoku):
    """ Main forward checking function
    """
    # Initialize counter
    variables.counter = 0

    recursive_backtracking(variables, sudoku)

    return variables.counter


def sudoku_forwardchecking(sudoku):
    """ Main forward checking function
    """
    # Initialize counter
    variables.counter = 0

    domain = get_domain(sudoku)
    recursive_forwardtracking(variables, sudoku, domain)

    return variables.counter



############## Helper Functions ##############

def recursive_backtracking(variables, sudoku):
    """ Recursive function for the forward-tracking function
    """
    # Increase counter
    variables.counter += 1

    # Check if board is complete
    if check_complete(sudoku):
        return True

    # If board not complete - check next step
    for y in range(SUDOKU_HEIGHT):
        for x in range(SUDOKU_WIDTH):
            # Check if a cell is available
            if check_available(sudoku, y, x):

                # Check available next step
                for i in range(1, SUDOKU_WIDTH + 1):

                    # Check cell for constraints
                    if common.can_yx_be_z(sudoku, y, x, i):

                        # Copy board and check cell for index
                        new_sudoku = copy_board(sudoku)
                        new_sudoku = set_cell(sudoku, y, x, i)
                        result = recursive_backtracking(variables, new_sudoku)

                        if result:
                            # sudoku = set_cell(sudoku, y, x, i)
                            return True

                        else:
                            sudoku = set_cell(sudoku, y, x, AVAILABLE_CELL)

                if check_available(sudoku, y, x):
                    return False

    return False


def recursive_forwardtracking(variables, sudoku, domain):
    """ Recursive function for the forward-tracking function
    """
    # Increase counter
    variables.counter += 1

    # Check if board is complete
    if check_complete(sudoku):
        return True

    # If board not complete - check next step
    for y in range(SUDOKU_HEIGHT):
        for x in range(SUDOKU_WIDTH):
            # Check if a cell is available
            if check_available(sudoku, y, x):

                # Check available next step
                for value in range(1, SUDOKU_WIDTH + 1):

                    # Check cell for constraints
                    if common.can_yx_be_z(sudoku, y, x, value):

                        # Update a copy of the domain
                        new_domain = copy_board(domain.copy())
                        updated_domain, is_full_domain = update_domain(new_domain, y, x, value)

                        if is_full_domain:
                            # Set cell with value
                            sudoku = set_cell(sudoku, y, x, value)
                            result = recursive_forwardtracking(variables, sudoku, updated_domain)

                            if result:
                                return True

                            else:
                                sudoku = set_cell(sudoku, y, x, AVAILABLE_CELL)

                if check_available(sudoku, y, x):
                    return False

    return False


def copy_board(board):
    """ Deep-copies the input board (sudoku or domain)
    """
    new_board = []

    # Copy sudoku
    if type(board[0][0]) == int:
        for row in board:
            new_board.append(row[:])

    # Copy domain
    else:
        for grid in board:
            new_grid = []
            for row in grid:
                new_grid.append(row[:])
            new_board.append(new_grid)

    return new_board


def set_cell(sudoku, y, x, value):
    """ Sets the current cell to the input value
    """
    sudoku[y][x] = value

    return sudoku


def check_available(sudoku, y, x):
    """ Checks if the current cell is available (cell value = 0).
    If available, returns True
    """
    return sudoku[y][x] == AVAILABLE_CELL


def check_complete(sudoku):
    """ Checks if the board is complete.
    If complete, returns True
    """
    for y in range(SUDOKU_HEIGHT):
        for x in range(SUDOKU_WIDTH):
            if check_available(sudoku, y, x):
                return False
            
            # Check cell constraints
            if not (check_available(sudoku, y, x)):
                value = sudoku[y][x]
                sudoku = set_cell(sudoku, y, x, AVAILABLE_CELL)
                if common.can_yx_be_z(sudoku, y, x, value):
                    sudoku = set_cell(sudoku, y, x, value)

            else:
                return False

    return True


def get_domain(sudoku):
    """ Defines (initializes and updates) the initial domain
    """
    # Initialize domain
    domain = []

    for y in range(SUDOKU_HEIGHT):
        board = []
        for x in range(SUDOKU_WIDTH):
            domain_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            board.append(domain_row)
        domain.append(board)

    # Update domain
    for y in range(SUDOKU_HEIGHT):
        for x in range(SUDOKU_WIDTH):
            if not (check_available(sudoku, y, x)):
                value = sudoku[y][x]
                domain, _ = update_domain(domain, y, x, value)

    return domain


def update_domain(domain, y, x, z):
    """ Updates domain with the optional cell values and returns the updated
    domain and if all of the rows in the domain have values in them
    """
    is_full_domain = True

    for i in range(SUDOKU_HEIGHT):
        current_row = domain[y][i]
        if x != i and z in current_row:
            current_row.remove(z)

        current_col = domain[i][x]
        if y != i and z in current_col:
            current_col.remove(z)

        y_diag = int(y / 3) * 3 + int(i / 3)
        x_diag = int(x / 3) * 3 + i % 3
        current_diag = domain[y_diag][x_diag]
        if y != y_diag and x != x_diag and z in current_diag:
            current_diag.remove(z)

    for board in domain:
        for row in board:
            if not len(row):
                is_full_domain = False

    return domain, is_full_domain
