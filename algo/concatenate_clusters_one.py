from math import dist
import numpy as np

def get_closest_points_to_centroid(cluster, centroid):

    distances = []
    for point in cluster:
        distances.append((point, dist(point, centroid)))
    distances.sort(key=lambda x: x[1])
    p1 = distances[0][0]

    idx1 = [idx for idx, x in enumerate(cluster) if x[0] == p1[0] and x[1] == p1[1]][0]

    forward = idx1 + 1
    if forward >= len(cluster):
        forward = 0
    backward = idx1 - 1

    new_perm = list(cluster)

    if dist(cluster[forward], centroid) < dist(cluster[backward], centroid):
        p2 = cluster[forward]
        idx2 = forward
        new_perm = new_perm[idx1::-1] + new_perm[:idx2 - 1:-1]
    else:
        p2 = cluster[backward]
        idx2 = backward
        new_perm = new_perm[idx1:] + new_perm[:idx2 + 1]

    return p1, p2, np.atleast_2d(new_perm)

def get_closest_points_to_points(cluster, p1, p2):

    distances = []
    for point in cluster:
        distances.append((point, dist(point, p1)))
    distances.sort(key=lambda x: x[1])
    p3 = distances[0][0]

    distances = []
    for point in cluster:
        if point[0] != p3[0] and point[1] != p3[1]:
            distances.append((point, dist(point, p2)))
    distances.sort(key=lambda x: x[1])
    p4 = 0
    try:
        p4 = distances[0][0]
    except Exception:
        print(distances)

    idx1 = [idx for idx, x in enumerate(cluster) if x[0] == p3[0] and x[1] == p3[1]][0]

    forward = idx1 + 1
    if forward >= len(cluster):
        forward = 0
    backward = idx1 - 1

    new_perm = list(cluster)

    if dist(cluster[forward], p2) < dist(cluster[backward], p2):
        p4 = cluster[forward]
        idx2 = forward
        new_perm = new_perm[idx1::-1] + new_perm[:idx2 - 1:-1]
    else:
        p4 = cluster[backward]
        idx2 = backward
        new_perm = new_perm[idx1:] + new_perm[:idx2 + 1]

    return p3, p4, np.atleast_2d(new_perm)

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def get_centeroid(arr):
    x = np.mean(arr[:, 0])
    y = np.mean(arr[:, 1])
    return np.atleast_1d([x, y])

def get_cost(result):
    cost = 0
    for i in range(len(result) - 1):
        cost += dist(result[i], result[i + 1])
    cost += dist(result[-1], result[0])

    return cost

def concatenate_clusters_one(cluster_a: np.ndarray, cluster_b: np.ndarray, centroid_a: np.ndarray, centroid_b: np.ndarray) -> (np.ndarray, np.ndarray):
    
    p1, p2, new_cluster_a = get_closest_points_to_centroid(cluster_a, centroid_b)
    p3, p4, new_cluster_b = get_closest_points_to_points(cluster_b, p1, p2)
    
    result_a = new_cluster_a

    if intersect(p1, p3, p2, p4):
        result_a = np.concatenate((result_a, new_cluster_b), axis=0)
    else:
        result_a = np.concatenate((result_a, np.flip(new_cluster_b, 0)), axis=0)

    points_a = (p1, p2, p3, p4)

    p1, p2, new_cluster_b = get_closest_points_to_centroid(cluster_b, centroid_a)
    p3, p4, new_cluster_a = get_closest_points_to_points(cluster_a, p1, p2)
    
    result_b = new_cluster_a

    if intersect(p1, p3, p2, p4):
        result_b = np.concatenate((result_b, new_cluster_b), axis=0)
    else:
        result_b = np.concatenate((result_b, np.flip(new_cluster_b, 0)), axis=0)

    points_b = (p1, p2, p3, p4)

    cost_a = get_cost(result_a)
    cost_b = get_cost(result_b)

    if cost_a < cost_b:
        return result_a, get_centeroid(result_a), points_a
    
    return result_b, get_centeroid(result_b), points_b
