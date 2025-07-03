import numpy as np

def generate_points(num_clusters, width=4096, height=4096):
    old_points = []
    old_clusters = []

    for _ in range(num_clusters):
        for _ in range(10):
            new_cluster = (np.random.randint(30, width - 30), 
            np.random.randint(30, height - 30))
            for old_cluster_x, old_cluster_y in old_clusters:
                distance_between_clusters = np.sqrt(
                    (new_cluster[0] - old_cluster_x)**2 +
                    (new_cluster[1] - old_cluster_y)**2
                )
                if distance_between_clusters < 120:
                    break
            else:
                old_clusters.append(new_cluster)
                break

    for cluster_center_x, cluster_center_y in old_clusters:
        new_points = []
        future_points = np.random.randint(0, 30)
        for _ in range(future_points):
            generated_point = (cluster_center_x + np.random.randint(-30, 30),
                               cluster_center_y + np.random.randint(-30, 30))
            new_points.append(generated_point)
        old_points.append(new_points)
    return old_points
