import matplotlib.pyplot as plt
from random_walk import RandomWalk
import pygal
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    points = list(zip(rw.x_values, rw.y_values))
    xy_chart = pygal.XY(stroke = False)
    xy_chart.add('Random Walk', points)
    xy_chart.add('Start', [points[0]], dots_size = 5)
    xy_chart.add('End', [points[-1]], dots_size = 5)
    xy_chart.render_in_browser()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    