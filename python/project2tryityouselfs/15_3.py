import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize = (10,6))
    plt.plot(rw.x_values, rw.y_values, linewidth = 1)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    