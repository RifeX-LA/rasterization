# theta(steps)
def step_by_step(x1: int, y1: int, x2: int, y2: int) -> list:
    k = (y2 - y1) / (x2 - x1)
    b = y2 - k * x2
    dx = abs(x2 - x1) / (max(abs(x2 - x1), abs(y2 - y1) * 2))

    if x2 < x1:
        dx = -dx

    x = x1
    y = k * x + b

    points = []
    while x < x2:
        point = (int(x), int(y))
        points.append(point)
        y = k * x + b
        x += dx

    return points


# theta(steps)
def dda(x0: int, y0: int, x1: int, y1: int) -> list:
    dx = x1 - x0
    dy = y1 - y0

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    points = []
    for i in range(0, int(steps + 1)):
        point = (int(round(x0)), int(round(y0)))
        points.append(point)
        x0 += x_inc
        y0 += y_inc

    return points


# theta(y1 - y0)
def bresenham(x0: int, y0: int, x1: int, y1: int) -> list:
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    m = dy / dx

    flag = True
    points = [(x0, y0)]

    step = 1
    if x0 > x1 or y0 > y1:
        step = -1

    mm = False
    if m < 1:
        x0, x1, y0, y1 = y0, y1, x0, x1
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        mm = True

    p0 = 2 * dx - dy
    x = x0
    y = y0

    for i in range(abs(y1 - y0)):
        if flag:
            x_previous = x0
            p_previous = p0
            p = p0
            flag = False
        else:
            x_previous = x
            p_previous = p

        if p >= 0:
            x = x + step

        p = p_previous + 2 * dx - 2 * dy * (abs(x - x_previous))
        y = y + 1

        if mm:
            points.append((y, x))
        else:
            points.append((x, y))

    return points


def mirror_points(x, y):
    return [(x, y),
            (y, x),
            (-x, y),
            (-y, x),
            (x, -y),
            (y, -x),
            (-x, -y),
            (-y, -x)]


# theta(r)
def bresenham_circle(x0: int, y0: int, r: int) -> list:
    points = []
    x = 0
    y = -r
    F_M = 1 - r
    d_e = 3
    d_ne = -(r << 1) + 5
    points.extend(mirror_points(x, y))
    while x < -y:
        if F_M <= 0:
            F_M += d_e
        else:
            F_M += d_ne
            d_ne += 2
            y += 1
        d_e += 2
        d_ne += 2
        x += 1
        points.extend(mirror_points(x, y))
    return points
