import math
import random as rnd
def generate_points(num_clusters, width=4096, height=4096):
    old_points = []
    old_clusters = []

    for _ in range(num_clusters):
        for _ in range(10):
            new_cluster = (randint(30, width - 30), randint(30, height - 30))
            for old_cluster_x, old_cluster_y in old_clusters:
                distance_between_clusters = sqrt(
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
        old_ray_length = rnd.randint(0, 30)
        for num_point in range(45):
            ray_angle = mth.radians(num_point * 8)
            new_ray_length = rnd.randint(old_ray_length - 2, old_ray_length + 2)
            generated_point_x = (cluster_center_x +
                new_ray_length *
                mth.cos(ray_angle))
            generated_point_y = (cluster_center_y +
                new_ray_length *
                mth.sin(ray_angle))
            old_ray_length = new_ray_length
            generated_point = (generated_point_x, generated_point_y)
            new_points.append(generated_point)
        old_points.append(new_points)
    return old_points
