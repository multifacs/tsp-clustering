import numpy as np
from algo.get_clusters import get_clusters
from algo.concatenate_all import concatenate_all
from python_tsp.distances.euclidean_distance import euclidean_distance_matrix
from python_tsp.heuristics.local_search import solve_tsp_local_search

def solve_cluster_tsp(nodes, n_clusters = 8, MIN_SIZE = 50, concat_alg = "one"):

    if len(nodes) <= n_clusters * 4:
        distance_matrix = euclidean_distance_matrix(nodes)
        permutation, _ = solve_tsp_local_search(distance_matrix)
        final_cluster = np.atleast_2d([nodes[x] for x in permutation])
        print(f"Final cluster size: {len(final_cluster)}")
        return final_cluster, np.mean(nodes, axis=0)


    clusters, centroids = get_clusters(nodes, n_clusters)
    solved_clusters = []
    for cluster in clusters:
        solved_clusters.append(solve_cluster_tsp(cluster, n_clusters - 1, MIN_SIZE)[0])

    return concatenate_all(solved_clusters, centroids, concat_alg)