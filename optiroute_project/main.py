from src.data_handler import load_data, compute_distance_matrix
from src.solvers import solve_vrp_ortools, solve_vrp_heuristic
from src.visualization import visualize_routes
from src.dp_solvers import solve_tsp_dp_recursive, solve_tsp_dp_iterative  # Updated import

def main():
    print("Loading data...")
    locations = load_data(filepath=None)  # Use hardcoded data by default
    distance_matrix = compute_distance_matrix(locations)

    num_vehicles = 1
    depot_index = 0

    print("Available Algorithms:")
    print("  1. ortools        - Google OR-Tools Solver")
    print("  2. heuristic      - Nearest Neighbor + 2-Opt")
    print("  3. dp_recursive   - Held-Karp Recursive DP")
    print("  4. dp_iterative   - Bottom-Up Iterative DP")
    selected_algorithm = input("Choose algorithm [ortools/heuristic/dp_recursive/dp_iterative]: ").strip().lower()

    if selected_algorithm == "ortools":
        print("\nSolving with OR-Tools...")
        ortools_routes, ortools_distance = solve_vrp_ortools(distance_matrix, num_vehicles, depot_index)
        if ortools_routes:
            print(f"OR-Tools Total Distance: {ortools_distance:.2f} km")
            for i, route in enumerate(ortools_routes):
                print(f"  Vehicle {i+1} Route: {route}")
            visualize_routes(locations, ortools_routes, filename="ortools_routes.html")
        else:
            print("OR-Tools solution not found.")

    elif selected_algorithm == "heuristic":
        print("\nSolving with Heuristic (Nearest Neighbor + 2-Opt)...")
        heuristic_routes, heuristic_distance = solve_vrp_heuristic(distance_matrix, depot_index)
        if heuristic_routes:
            print(f"Heuristic Total Distance: {heuristic_distance:.2f} km")
            for i, route in enumerate(heuristic_routes):
                print(f"  Vehicle {i+1} Route: {route}")
            visualize_routes(locations, heuristic_routes, filename="heuristic_routes.html")
        else:
            print("Heuristic solution not found.")

    elif selected_algorithm == "dp_recursive":
        print("\nSolving with Recursive DP (Held-Karp)...")
        dp_routes, dp_distance = solve_tsp_dp_recursive(distance_matrix, depot_index)
        if dp_routes:
            print(f"Recursive DP Total Distance: {dp_distance:.2f} km")
            for i, route in enumerate(dp_routes):
                print(f"  Vehicle {i+1} Route: {route}")
            visualize_routes(locations, dp_routes, filename="dp_recursive_routes.html")
        else:
            print("Recursive DP solution not found.")

    elif selected_algorithm == "dp_iterative":
        print("\nSolving with Iterative DP (Bottom-Up)...")
        dp_routes, dp_distance = solve_tsp_dp_iterative(distance_matrix, depot_index)
        if dp_routes:
            print(f"Iterative DP Total Distance: {dp_distance:.2f} km")
            for i, route in enumerate(dp_routes):
                print(f"  Vehicle {i+1} Route: {route}")
            visualize_routes(locations, dp_routes, filename="dp_iterative_routes.html")
        else:
            print("Iterative DP solution not found.")

    else:
        print(f"Unknown algorithm '{selected_algorithm}'. Please choose one of: ortools, heuristic, dp_recursive, dp_iterative.")

if __name__ == "__main__":
    main()
