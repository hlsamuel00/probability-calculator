from copy import deepcopy
from random import randrange, seed
from collections import defaultdict

class Hat:
    # Initialize the Hat class with an empty list. Iterate over the values entered as keyword arguments dictionary and add each color of the ball the respective number of times. Utilizing the list will provide the accurate probability of obtaining each respective ball later on.
    def __init__(self, **balls) -> None:
        self.contents = []

        for ball_color, ball_count in balls.items():
            for _ in range(ball_count):
                self.contents.append(ball_color)

    # The draw method completes the specified number of pulls from the hat and returns a list of picked balls.
    def draw(self, number_of_picks: int) -> list[str]:
        number_of_picks = min(number_of_picks, len(self.contents))
        picked_balls = []

        # Iterate the specified number of picks. On each iteration, obtain a random index, swap the last value in the list with the random index of the contents list, pop off the last item in the list, and add it to the picked_ball list. 
        for _ in range(number_of_picks):
            idx = randrange(len(self.contents))
            self.contents[-1], self.contents[idx] = self.contents[idx], self.contents[-1]
            picked_balls.append(self.contents.pop())
        
        # Return the count of picked balls
        return picked_balls 
    
# The experiment method calculates the number of correct guesses made out of all of the experiments performed.
def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    # Initialize the number of correct guesses
    correct_guess = 0

    # Iterate the specified number of experiments. On each iteration, create a copy of the hat provided and draw the specified number of balls.
    for _ in range(num_experiments):
        picked_balls = deepcopy(hat).draw(num_balls_drawn)
        
        # Compare the values of expected balls compared to the picked balls. If each picked ball color is greater than or equal to the expected ball count for that color, increase the count of correct guesses by one
        if _validate_experiment(picked_balls, expected_balls):
            correct_guess += 1

    # Return the ratio of correct guesses out of the number of experiments. 
    return correct_guess / num_experiments

# This helper method determines if the expected prediction was correct based on the balls picked. 
def _validate_experiment(picked_balls: list[str], expected_balls: dict[str, int]) -> bool:
    picked_ball_count = defaultdict(int)
    for picked_ball_color in picked_balls:
        picked_ball_count[picked_ball_color] += 1

    for exp_ball_color, exp_ball_count in expected_balls.items():
        if picked_ball_count[exp_ball_color] < exp_ball_count:
            return False
            
    return True
