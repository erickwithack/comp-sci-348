import common

MAP_WIDTH = 6
MAP_HEIGHT = 6


def drone_flight_planner (map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	rival_list = []
	# Define values and optimal policies for initial map
	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):

			## value and optimal policy for customer cell
			if map[y][x] == common.constants.PIZZA:
				start = (y ,x)

			## value and optimal policy for customer cell
			elif map[y][x] == common.constants.CUSTOMER:
				goal = (y, x)
				values[y][x] = delivery_fee
				policies[y][x] = common.constants.EXIT

			## value and optimal policy for rival cell
			elif map[y][x] == common.constants.RIVAL:
				rival_list.append((y ,x))
				values[y][x] = -dronerepair_cost
				policies[y][x] = common.constants.EXIT
	
	# Initialize counter and value margin for correctness
	margin = 10000

	while True:
		# Increase counter and initialize value margin for correctness
		margin = 0
		margin_flag = True
		old_values = [x[:] for x in values]

		for y in range(MAP_HEIGHT):
			for x in range(MAP_WIDTH):
				if map[y][x] != common.constants.RIVAL and map[y][x] != common.constants.CUSTOMER:
					value_list = find_next_values(map, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount, y, x)
					max_value = max(value_list)
					max_index = value_list.index(max_value)
					values[y][x] = max_value
					policies[y][x] = max_index + 1

				margin = abs(values[y][x] - old_values[y][x])
				if margin > 0.01:
					margin_flag = False

		if margin_flag == True:
			break

	return values[start[0]][start[1]]


def find_next_values(map, values, delivery_fee, battery_drop_cost, dronerepair_cost, gamma, y, x):
	south_val = find_current_values(values, y + 1, x)
	west_val = find_current_values(values, y, x - 1)
	north_val = find_current_values(values, y - 1, x)
	east_val = find_current_values(values, y, x + 1)

	reward_off = find_reward(map, delivery_fee, battery_drop_cost, dronerepair_cost, False, y, x)
	reward_on = find_reward(map, delivery_fee, battery_drop_cost, dronerepair_cost, True, y, x)

	south_off = get_direction_value(reward_off, False, gamma,
									south_val, east_val, west_val)
	west_off = get_direction_value(reward_off, False, gamma,
								   west_val, south_val, north_val)
	north_off = get_direction_value(reward_off, False, gamma,
									north_val, east_val, west_val)
	east_off = get_direction_value(reward_off, False, gamma,
								   east_val, south_val, north_val)

	south_on = get_direction_value(reward_on, True, gamma,
								   south_val, east_val, west_val)
	west_on = get_direction_value(reward_on, True, gamma,
								  west_val, south_val, north_val)
	north_on = get_direction_value(reward_on, True, gamma,
								   north_val, east_val, west_val)
	east_on = get_direction_value(reward_on, True, gamma,
								  east_val, south_val, north_val)

	value_list = [south_off, west_off, north_off, east_off,
				  south_on, west_on, north_on, east_on]
	
	return value_list


def get_partial_direction_value(reward, gamma, direction):
	direction_value = reward + gamma*direction
	
	return direction_value


def get_direction_value(reward, special_propulsion, gamma, main_direction, right_direction, left_direction):
	if special_propulsion:
		
		tot_direction_value = 0.8*get_partial_direction_value(reward, gamma, main_direction)\
							+ 0.1*get_partial_direction_value(reward, gamma, right_direction)\
							+ 0.1*get_partial_direction_value(reward, gamma, left_direction)
	else:
		tot_direction_value = 0.7*get_partial_direction_value(reward, gamma, main_direction)\
						   + 0.15*get_partial_direction_value(reward, gamma, right_direction)\
						   + 0.15*get_partial_direction_value(reward, gamma, left_direction)

	return tot_direction_value


def find_current_values(values, y, x):
	if y < 0:
		y = 0

	if x < 0:
		x = 0
	
	if y >= MAP_HEIGHT:
		y = MAP_HEIGHT - 1
	
	if x >= MAP_WIDTH:
		x = MAP_WIDTH - 1

	return values[y][x]


def find_reward(map, delivery_fee, battery_drop_cost, dronerepair_cost, special_propulsion, y, x):
	current_reward = 0

	# If current cell is empty or the pizza shop
	if map[y][x] <= 1:
		if not special_propulsion:
			current_reward = -battery_drop_cost
		else:
			current_reward = -2*battery_drop_cost

	# If current cell is customer
	elif map[y][x] == common.constants.CUSTOMER:				
		current_reward = delivery_fee

	# If current cell is rival
	elif map[y][x] == common.constants.RIVAL:				
		current_reward = -dronerepair_cost

	return current_reward