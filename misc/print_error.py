from math import dist
import numpy as np
from data.answers import get_answer

def print_error(result, dataset):
    cost = 0
    for i in range(len(result) - 1):
        cost += dist(result[i], result[i + 1])
    cost += dist(result[-1], result[0])
    print(cost)

    perc = cost / get_answer(dataset) * 100 - 100
    rounded = np.round((perc) * 1000)
    restored = rounded / 1000

    print("Final error: {}%".format(restored))