import pandas as pd
from geopy.distance import geodesic

def load_data(filepath=None, num_locations=None):
    if filepath and filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
        coords = df[["latitude", "longitude"]].values.tolist()
        if num_locations:
            return coords[:num_locations]
        return coords
    else:
        hardcoded = [
            (34.0522, -118.2437),  # Depot
            (34.0522, -118.2500),
            (34.0600, -118.2400),
            (34.0400, -118.2600)
        ]
        return hardcoded[:num_locations] if num_locations else hardcoded

def compute_distance_matrix(locations):
    num_locations = len(locations)
    distance_matrix = [[0] * num_locations for _ in range(num_locations)]
    for i in range(num_locations):
        for j in range(num_locations):
            if i == j:
                continue
            distance_matrix[i][j] = geodesic(locations[i], locations[j]).km
    return distance_matrix
