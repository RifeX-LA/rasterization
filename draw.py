from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Circle
import rasterization


def draw_points(ax, points: list):
    for point in points:
        ax.add_patch(Rectangle(point, 1, 1, edgecolor='black', facecolor='gray', linewidth=1))


def draw_line(x0: int, y0: int, x1: int, y1: int, algorithm):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim((min(x0, x1), max(x0, x1)))
    ax.set_ylim((min(y0, y1), max(y0, y1)))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid()

    ax.plot((x0, x1), (y0, y1))
    draw_points(ax, algorithm(x0, y0, x1, y1))

    plt.title(algorithm.__name__)
    plt.show()


def draw_circle(x: int, y: int, r: int):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim((x - r - 1, x + r + 1))
    ax.set_ylim((y - r - 1, y + r + 1))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid()

    ax.add_patch(Circle((x, y), radius=r, facecolor='none', edgecolor='blue', linewidth=2))
    for point in rasterization.bresenham_circle(x, y, r):
        x0, y0 = point
        ax.add_patch(Rectangle((x0 + x - 0.5, y0 + y - 0.5), 1, 1, edgecolor='black', facecolor='gray', linewidth=1))

    plt.title('bresenham circle')
    plt.show()


def draw(*args):
    if len(args) == 3:
        draw_circle(*args)
    elif len(args) == 4:
        *points, dummy = args
        draw_circle(*points)
    elif len(args) == 5:
        draw_line(*args)
    else:
        raise RuntimeError('Invalid number of args')
