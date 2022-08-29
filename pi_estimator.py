import random


def estimate_pi(n):
    num_circle_points = 0
    num_total_points = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_circle_points += 1
        num_total_points += 1
    return 4 * num_circle_points/num_total_points

estimate_pi(10000)
