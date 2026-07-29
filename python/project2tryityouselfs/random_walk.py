from random import choice

class RandomWalk():
    """A class to generate Random Walks"""
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def set_up(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,6,7,8])
        return direction * distance

       

    def fill_walk(self):
            while len(self.x_values) < self.num_points:
                x_step = self.set_up()
                y_step = self.set_up()

                if x_step == 0 and y_step == 0:
                     continue
                new_x = self.x_values[-1] + x_step
                new_y = self.y_values[-1] + y_step

                self.x_values.append(new_x)
                self.y_values.append(new_y)
                