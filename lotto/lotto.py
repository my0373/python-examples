import math
import random


def create_ball_set(min=1,max=49):
    """
    Generate a "set" of balls.
    """
    return [x for x in range(min,max +1)]

def pick_balls(num_balls,balls):
    """
    Pick a ball 
    """
    ball_set = []

    # Select a random ball and remove it from the list of available balls
    for ball in range(num_balls):
        tmpball = random.choice(balls)
        ball_set.append(tmpball)
        balls.remove(tmpball)

    # return the sorted
    return sorted(ball_set)


def main():

    # Some defaults for the UK national lottery
    num_std_balls = 6
    num_bonus_balls = 1
    picked_balls = {}


    # Define the dimensions of the ball set
    std_balls = create_ball_set(1,49)
    bonus_balls = create_ball_set(1,49)

    # Store the values in a dictionary of lists.
    # The dictionary has 2 keys
    #
    # picked_balls["standard"] - The normal 6 numbers
    # picked_balls["bonus"] - The bonus number
    picked_balls["standard"] = (pick_balls(num_std_balls,std_balls))
    picked_balls["bonus"] = (pick_balls(num_bonus_balls,bonus_balls))


    return picked_balls


if __name__ == '__main__':

    # Generate a set of balls based on the UK lottery
    balls = main()

    print(balls)