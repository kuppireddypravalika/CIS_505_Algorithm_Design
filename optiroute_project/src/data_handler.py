import pandas as pd
from geopy.distance import geodesic

def load_data(filepath=None):
    if filepath and filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
        # Assuming CSV has 'latitude', 'longitude' columns
        return df[["latitude", "longitude"]].values.tolist()
    else:
        # Example hardcoded coordinates (depot first)
        return [
            (34.0522, -118.2437), # Los Angeles (Depot)
            (34.0522, -118.2500), # Customer 1
            (34.0600, -118.2400), # Customer 2
            (34.0400, -118.2600)  # Customer 3
        ]

def compute_distance_matrix(locations):
    num_locations = len(locations)
    distance_matrix = [[0] * num_locations for _ in range(num_locations)]
    for i in range(num_locations):
        for j in range(num_locations):
            if i == j:
                continue
            distance_matrix[i][j] = geodesic(locations[i], locations[j]).km
    return distance_matrix


