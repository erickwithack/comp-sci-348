import common
import math  # note, for this lab only, your are allowed to import math

WIDTH = common.constants.WIDTH
HEIGHT = common.constants.HEIGHT
CONVERTED_SIZE = 2000


def detect_slope_intercept(image):
    space = common.init_space(CONVERTED_SIZE, CONVERTED_SIZE)
    line = common.Line()

    point_list = get_points(image)

    for row in range(CONVERTED_SIZE):
        for point in point_list:
            # Change m range from [0, 2000] to [-10, 10]
            m = row / 100 - 10
            b = point[1] - m * point[0]  # y = mx + b  =>  b = y - mx

            # Change b range from [-1000, 1000] to [0, 2000]
            b_cast = int(b + 1000)

            # Change m range from [-10, 10] to [0, 2000]
            m_cast = int((m + 10) * 100)

            if 0 <= b_cast < CONVERTED_SIZE and 0 <= m_cast < CONVERTED_SIZE:
                space[b_cast][m_cast] += 1

    max_value = -1
    for b in range(CONVERTED_SIZE):
        for m in range(CONVERTED_SIZE):
            if space[b][m] > max_value:
                max_value = space[b][m]
                line.b = b - 1000
                line.m = m / 100 - 10

    return line


def detect_circles(image):
    space = common.init_space(HEIGHT, WIDTH)
    circle = common.Line()
    circle.r = 30
    circles_num = 0

    point_list = get_points(image)

    tot_steps = 2 * 360
    angle_per_step = 2 * math.pi / tot_steps

    for theta in range(tot_steps):
        for point in point_list:
            # (x - a)^2 + (y - b)^2 = r^2
            a = int(point[0] + circle.r * math.cos(angle_per_step * theta) + 1)
            b = int(point[1] - circle.r * math.sin(angle_per_step * theta) + 1)

            if 0 <= a < HEIGHT and 0 <= b < WIDTH:
                space[a][b] += 1

    for a in range(HEIGHT):
        for b in range(WIDTH):
            if space[a][b] > 650:
                circles_num += 1

    return circles_num


def get_points(image):
    point_list = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == 0:
                point_list.append((x, y))

    return point_list
