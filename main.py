import numpy as np

def generate_points(number_of_clusters, screen_width=4096, screen_height=4096):
    """
    Generates clusters of points within a specified screen area.

    Args:
        number_of_clusters (int): The desired number of clusters.
        screen_width (int, optional): The width of the screen. Defaults to 4096.
        screen_height (int, optional): The height of the screen. Defaults to 4096.

    Returns:
        list: A list of lists, where each inner list contains points belonging
              to a single cluster.
    """
    all_points = []
    just_clusters = []
    minimum_distance = 30 * 4

    for _ in range(number_of_clusters):
        attempts_count = 0
        while attempts_count < 1:
            new_cluster_candidate = (np.random.randint(30, screen_witdth - 30),
                                     np.random.randint(30, screen_height - 30))
            for existing_cluster_x, existing_cluster_y in just_clusters:
                distance_between_clusters = np.sqrt(
                    (new_cluster_candidate[0] - existing_cluster_x)**2 +
                    (new_cluster_candidate[1] - existing_cluster_y)**2
                )
                if distance_between_clusters < minimum_distance:
                    attempts_count += 1
                    break
            else:  # No break occurred, meaning candidate is far enough
                just_clusters.append(new_cluster_candidate)
                break

    for cluster_center_x, cluster_center_y in just_clusters:
        new_points = []
        num_points_to_generate = np.random.randint(0, 30)
        for _ in range(num_points_to_generate):
            offset_x = np.random.randint(-30, 30)
            offset_y = np.random.randint(-30, 30)

            generated_point = (cluster_center_x + offset_x,
                               cluster_center_y + offset_y)
            new_points.append(generated_point)
        all_points.append(new_points)
    return all_points
