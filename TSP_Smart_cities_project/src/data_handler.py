import pandas as pd

def load_data(filepath=None, num_locations=None):
    """
    Load fixed lat/lon coordinates from CSV for visualization.
    """
    df = pd.read_csv("data/road_connected_locations.csv")
    coords = df[["latitude", "longitude"]].values.tolist()
    return coords[:num_locations] if num_locations else coords

def compute_distance_matrix(locations):
    df = pd.read_csv("data/road_distance_matrix_km.csv")
    matrix = df.values.tolist()

    
    n = len(locations)
    trimmed = [row[:n] for row in matrix[:n]]
    return trimmed
