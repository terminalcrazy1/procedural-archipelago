import numpy as np
def gen_clusters(center_distance=10, max_attempts=1, num_clusters=1677, screen_x=4096, screen_y=4096):
    just_clusters = []
    for _ in range(num_clusters):
        attempts = 0
        while attempts < max_attempts:
            new_cluster = (np.random.randint(screen_x), np.random.randint(screen_y))
            for old_cluster_x, old_cluster_y in just_clusters:
                distance = np.sqrt((new_cluster[0] - old_cluster_x)^2 + (new_cluster[1] - old_cluster_y)^2)
                if distance < center_distance:
                    attempts += 1
                    break
            else:
                just_clusters.append(new_cluster)
                break
    return just_clusters
