import matplotlib.pyplot as plt

def plot_path(points):
    
    x_min, x_max = points[:, 0].min() - 1, points[:, 0].max() + 1
    y_min, y_max = points[:, 1].min() - 1, points[:, 1].max() + 1

    plt.plot(points[:, 0], points[:, 1], "k.", markersize=2)

    for i in range(len(points) - 1):
        plt.plot(points[[i, i+1], 0], points[[i, i+1], 1], c="k")
    plt.plot(points[[len(points) - 1, 0], 0], points[[len(points) - 1, 0], 1], c="k")

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()