import common

MAP_WIDTH = common.constants.MAP_WIDTH
MAP_HEIGHT = common.constants.MAP_HEIGHT


def astar_search(map):
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1

    # Initializing variables
    found = False
    parents_list = []
    frontier = []
    frontier_f = []

    # Finding start & goal points
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map[y][x] == 2:
                start = (y, x)
            if map[y][x] == 3:
                goal = (y, x)

    # Finding the f(n) value of the start point
    temp_frontier_f = Manhattan_dist(start, goal)

    # Adding start point to frontier
    frontier.append([start, parents_list])
    frontier_f.append(temp_frontier_f)

    while len(frontier) != 0:
        min_f_index = find_min_index(frontier, frontier_f)
        curr_frontier, parents_list = frontier[min_f_index]

        if curr_frontier == goal:
            found = True
            break

        # Marking visited cells
        map[curr_frontier[0]][curr_frontier[1]] = 4

        # Checking frontier children
        right_cell = (curr_frontier[0], curr_frontier[1] + 1)
        down_cell = (curr_frontier[0] + 1, curr_frontier[1])
        left_cell = (curr_frontier[0], curr_frontier[1] - 1)
        up_cell = (curr_frontier[0] - 1, curr_frontier[1])

        if (curr_frontier[1] + 1 <= MAP_WIDTH - 1) and (check_available_cell(map, right_cell)):
            update_lists(frontier, frontier_f, curr_frontier, parents_list, right_cell, goal)

        if (curr_frontier[0] + 1 <= MAP_HEIGHT - 1) and (check_available_cell(map, down_cell)):
            update_lists(frontier, frontier_f, curr_frontier, parents_list, down_cell, goal)

        if (curr_frontier[1] - 1 >= 0) and (check_available_cell(map, left_cell)):
            update_lists(frontier, frontier_f, curr_frontier, parents_list, left_cell, goal)

        if (curr_frontier[0] - 1 >= 0) and (check_available_cell(map, up_cell)):
            update_lists(frontier, frontier_f, curr_frontier, parents_list, up_cell, goal)

        # Removing the current frontier from the frontier lists
        frontier.pop(min_f_index)
        frontier_f.pop(min_f_index)

    # Marking path
    if found:
        map[goal[0]][goal[1]] = 5
        for parent in parents_list:
            map[parent[0]][parent[1]] = 5

    # print_map(map)
    return found


def check_available_cell(map, curr_point):
    """ checks if a cell was visited before
    """
    return map[curr_point[0]][curr_point[1]] not in [1, 4]


def Manhattan_dist(curr_point, goal):
    """ Finds the Manhattan distance of a point from the goal point
    """
    return abs(goal[0] - curr_point[0]) + abs(goal[1] - curr_point[1])


def find_min_index(frontier, frontier_f):
    """ Finds the index of the minimum value in a list
    """
    min_index = 0
    min_element = frontier_f[min_index]

    for i in range(1, len(frontier_f)):
        if frontier_f[i] < min_element:
            min_index = i
            min_element = frontier_f[i]

        elif frontier_f[i] == min_element:
            curr_frontier, _ = frontier[i]
            former_frontier, _ = frontier[min_index]

            if curr_frontier[1] < former_frontier[1]:
                min_index = i

            elif curr_frontier[1] > former_frontier[1]:
                continue

            else:
                if curr_frontier[0] < former_frontier[0]:
                    min_index = i

                if curr_frontier[0] > former_frontier[0]:
                    continue

    return min_index


def update_lists(frontier, frontier_f, curr_frontier, parents_list, cell, goal):
    """ Updates the frontier lists
    """
    new_parents_list = parents_list[:]
    temp_frontier_f = Manhattan_dist(cell, goal) + len(new_parents_list)
    new_parents_list.append(curr_frontier)
    frontier.append([cell, new_parents_list])
    frontier_f.append(temp_frontier_f)


def print_map(map):
    """ Prints the current map in a readable format
    """
    for row in map:
        print(row)
    print("\n")
