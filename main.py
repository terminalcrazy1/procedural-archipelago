import numpy as np

def generate_points(maximum_points, number_of_clusters, screen_x=4096, screen_y=4096):
  all_points = []
  just_clusters = []
  maximum_spread = maximum_points / 4
  maximum_attempts = 1

  for _ in range(number_of_clusters):
    attempts_count = 0
    while attempts_count < maximum_attempts:
      new_cluster_candidate = (np.random.randint(maximum_spread, screen_x - maximum_spread), np.random.randint(maximum_spread, screen_y - maximum_spread))
      for existing_cluster_x, existing_cluster_y in just_clusters:
          distance_between_clusters = np.sqrt((new_cluster_candidate[0] - existing_cluster_x)**2 + (new_cluster_candidate[1] - existing_cluster_y)**2)
          if distance_between_clusters < maximum_spread:
            attempts_count += 1
            break
      else:
        just_clusters.append(new_cluster_candidate)
        break

  for cluster_center_x, cluster_center_y in just_clusters:
      num_points_to_generate = np.random.randint(maximum_points)
      for _ in range(num_points_to_generate):
          offset_x = np.random.randint(-maximum_spread, maximum_spread)
          offset_y = np.random.randint(-maximum_spread, maximum_spread)
          
          generated_point = (cluster_center_x + offset_x, cluster_center_y + offset_y)
          all_points.append(generated_point)
  return all_points
