import copy
import random

class Hat:
    def __init__(self, **balls):
      # Initialize the Hat object with the specified balls and their counts
        self.contents = []
      # Add each ball color to the contents list as per its count
        for color, count in balls.items():
            self.contents.extend([color] * count)

    # Draw a specified number of balls from the hat without replacement
    def draw(self, num_balls):
        # If the number of balls to draw exceeds the available quantity,
        # return all the balls in the hat
        if num_balls >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls)
        # Randomly select balls from the hat and remove them from contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # Run experiments to estimate the probability of drawing expected balls
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        
      # Check if the drawn balls match the expected balls
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_dict.get(color, 0) < count:
                success = False
                break
        if success:
            successful_experiments += 1
    return successful_experiments / num_experiments


