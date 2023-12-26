from math import dist
import numpy as np
from algo.concatenate_clusters_one import concatenate_clusters_one
from algo.concatenate_clusters_two import concatenate_clusters_two
from plotting.plot_clusters import plot_clusters

def concatenate_all(clusters, centroids, alg="one"):

    t_clusters = list(clusters)
    t_centroids = list(centroids)

    while len(t_clusters) > 1:
        A = 0
        B = 1

        for i in range(1, len(t_centroids)):
            if (dist(t_centroids[i], t_centroids[A]) < dist(t_centroids[B], t_centroids[A])):
                B = i
        # print(A, B)

        new_cluster, new_centroid, connection_points = 1, 2, 3

        if alg == "one":
            new_cluster, new_centroid, connection_points = concatenate_clusters_one(t_clusters[A], t_clusters[B], t_centroids[A], t_centroids[B])
        if alg == "two":
            new_cluster, new_centroid, connection_points = concatenate_clusters_two(t_clusters[A], t_clusters[B], t_centroids[A], t_centroids[B])

        t_clusters = [np.atleast_2d(x) for idx, x in enumerate(t_clusters) if idx != A and idx != B]
        t_centroids = [x for idx, x in enumerate(t_centroids) if idx != A and idx != B]

        t_clusters.append(new_cluster)
        t_centroids.append(new_centroid)
        t_centroids = np.atleast_2d(t_centroids)
        # plot_clusters(cities, t_clusters, t_centroids, cp)

    return t_clusters[0], t_centroids[0]