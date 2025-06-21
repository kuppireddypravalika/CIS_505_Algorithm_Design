import csv
import random

def generate_synthetic_coordinates(num_points=10, center=(34.05, -118.25), radius_km=5.0):
    coords = []
    for _ in range(num_points):
        lat_offset = random.uniform(-radius_km, radius_km) / 111  # ~111km per lat
        lon_offset = random.uniform(-radius_km, radius_km) / (111 * abs(center[0]))
        coords.append((center[0] + lat_offset, center[1] + lon_offset))

    with open("data/synthetic_locations.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["latitude", "longitude"])
        writer.writerows(coords)

# Change this to 20, 50, 100 as needed
generate_synthetic_coordinates(num_points=50)
