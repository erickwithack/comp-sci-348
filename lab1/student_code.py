import common

MAP_WIDTH = common.constants.MAP_WIDTH
MAP_HEIGHT = common.constants.MAP_HEIGHT


def df_search(map):

    # Initializing variables
    found = False
    visited = [[0] * (MAP_WIDTH - 1)] * (MAP_HEIGHT - 1)
    parents_list = []
    frontier = []

    # Finding start & goal points
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map[y][x] == 2:
                start = (y, x)
            if map[y][x] == 3:
                goal = (y, x)

    # Adding start point to frontier
    frontier.append([start, parents_list])

    while len(frontier) != 0:
        curr_frontier, parents_list = frontier.pop(-1)

        if curr_frontier == goal:
            found = True
            break

        # Marking visited cells
        map[curr_frontier[0]][curr_frontier[1]] = 4

        # Checking frontier children
        if (curr_frontier[0] - 1 >= 0) and (check_available_cell(map, curr_frontier[0] - 1, curr_frontier[1])):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0] - 1, curr_frontier[1]), new_parents_list])

        if (curr_frontier[1] - 1 >= 0) and (check_available_cell(map, curr_frontier[0], curr_frontier[1] - 1)):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0], curr_frontier[1] - 1), new_parents_list])

        if (curr_frontier[0] + 1 <= MAP_HEIGHT - 1) and (check_available_cell(map, curr_frontier[0] + 1, curr_frontier[1])):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0] + 1, curr_frontier[1]), new_parents_list])

        if (curr_frontier[1] + 1 <= MAP_WIDTH - 1) and (check_available_cell(map, curr_frontier[0], curr_frontier[1] + 1)):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0], curr_frontier[1] + 1), new_parents_list])

    # Marking path
    if found == True:
        map[goal[0]][goal[1]] = 5
        for parent in parents_list:
            map[parent[0]][parent[1]] = 5

    return found


def bf_search(map):

    # Initializing variables
    found = False
    visited = [[0] * (MAP_WIDTH - 1)] * (MAP_HEIGHT - 1)
    parents_list = []
    frontier = []

    # Finding start & goal points
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map[y][x] == 2:
                start = (y, x)
            if map[y][x] == 3:
                goal = (y, x)

    # Adding start point to frontier
    frontier.append([start, parents_list])

    while len(frontier) != 0:
        curr_frontier, parents_list = frontier.pop(0)

        if curr_frontier == goal:
            found = True
            break

        # Marking visited cells
        map[curr_frontier[0]][curr_frontier[1]] = 4

        # Checking frontier children
        if (curr_frontier[1] + 1 <= MAP_WIDTH - 1) and (check_available_cell(map, curr_frontier[0], curr_frontier[1] + 1)):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0], curr_frontier[1] + 1), new_parents_list])

        if (curr_frontier[0] + 1 <= MAP_HEIGHT - 1) and (check_available_cell(map, curr_frontier[0] + 1, curr_frontier[1])):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0] + 1, curr_frontier[1]), new_parents_list])

        if (curr_frontier[1] - 1 >= 0) and (check_available_cell(map, curr_frontier[0], curr_frontier[1] - 1)):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0], curr_frontier[1] - 1), new_parents_list])

        if (curr_frontier[0] - 1 >= 0) and (check_available_cell(map, curr_frontier[0] - 1, curr_frontier[1])):
            new_parents_list = parents_list[:]
            new_parents_list.append(curr_frontier)
            frontier.append(
                [(curr_frontier[0] - 1, curr_frontier[1]), new_parents_list])

    # Marking path
    if found == True:
        map[goal[0]][goal[1]] = 5
        for parent in parents_list:
            map[parent[0]][parent[1]] = 5

    return found


def check_available_cell(map, y, x):
    return map[y][x] not in [1, 4]
