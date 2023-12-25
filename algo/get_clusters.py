# from sklearn.cluster import KMeans
import numpy as np
# from python_tsp.distances.euclidean_distance import euclidean_distance_matrix
# from python_tsp.heuristics.local_search import solve_tsp_local_search

from k_means_constrained import KMeansConstrained

def get_clusters(cities, N_CLUSTERS = 8):
    clf = KMeansConstrained(
        n_clusters=N_CLUSTERS,
        size_min=4
    )
    clf.fit_predict(cities)
    clf.cluster_centers_
    clf.labels_

    # kmeans = KMeans(n_clusters=N_CLUSTERS).fit(cities)
    # print(kmeans.labels_)

    LABELS = np.atleast_1d(clf.labels_)
    CENTROIDS = np.atleast_2d(clf.cluster_centers_)

    CLUSTERS = []

    for i in range(N_CLUSTERS):
        problem = np.atleast_2d([city for idx, city in enumerate(cities) if LABELS[idx] == i])
        CLUSTERS.append(problem)

    # CLUSTERS = []
    # for p in subproblems:
    #     distance_matrix = euclidean_distance_matrix(p)
    #     permutation, distance = solve_tsp_local_search(distance_matrix)
    #     # print(distance)
    #     subset = np.atleast_2d([p[x] for x in permutation])
    #     # print(subset)
    #     CLUSTERS.append(subset)

    return CLUSTERS, CENTROIDS
