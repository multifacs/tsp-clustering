import numpy as np
import tsplib95

def get_dataset(path):
    return np.atleast_2d(list(tsplib95.load(path).node_coords.values()))