import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [ ball_color for ball_color, ball_count in kwargs.items() for _ in range(ball_count) ]

    def draw(self, number_of_balls):
        number_of_balls = min(number_of_balls, len(self.contents))
        return [ self.contents.pop(random.randrange(len(self.contents))) for _ in range(number_of_balls) ]
       
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct_guess = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        picked_balls = hat_copy.draw(num_balls_drawn)
        if all(picked_balls.count(color) >= count for (color, count) in expected_balls.items()):
            correct_guess += 1

    return correct_guess / num_experiments
