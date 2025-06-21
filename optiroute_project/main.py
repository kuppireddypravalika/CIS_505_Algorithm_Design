from src.data_handler import load_data, compute_distance_matrix
from src.visualization import visualize_routes
from src.manual_heuristic_solver import solve_tsp_manual_heuristic
from src.manual_dp_solvers import solve_tsp_dp_recursive, solve_tsp_dp_iterative
from src.manual_bt_solver import solve_tsp_backtracking
from src.manual_bb_solver import solve_tsp_branch_and_bound

def main():
    print("Loading data...")

    filepath = input("Enter CSV file path (or press Enter to use default hardcoded values): ").strip()
    num_locations = input("How many locations to use? (Press Enter for all): ").strip()
    num_locations = int(num_locations) if num_locations.isdigit() else None

    locations = load_data(filepath if filepath else None, num_locations=num_locations)
    distance_matrix = compute_distance_matrix(locations)
    depot_index = 0

    print("\nAvailable Algorithms:")
    print("  1. heuristic   - Nearest Neighbor + 2-Opt")
    print("  2. dp_rec      - Dynamic Programming (Recursive)")
    print("  3. dp_iter     - Dynamic Programming (Iterative)")
    print("  4. bt          - Backtracking")
    print("  5. bb          - Branch and Bound")
    algo = input("Choose algorithm [heuristic/dp_rec/dp_iter/bt/bb]: ").strip().lower()

    if algo == "heuristic":
        routes, dist = solve_tsp_manual_heuristic(distance_matrix, depot_index)
        print(f"Heuristic Distance: {dist:.2f} km")
        map_filename = "heuristic_routes.html"
    elif algo == "dp_rec":
        routes, dist = solve_tsp_dp_recursive(distance_matrix, depot_index)
        print(f"Recursive DP Distance: {dist:.2f} km")
        map_filename = "dp_recursive_routes.html"
    elif algo == "dp_iter":
        routes, dist = solve_tsp_dp_iterative(distance_matrix, depot_index)
        print(f"Iterative DP Distance: {dist:.2f} km")
        map_filename = "dp_iterative_routes.html"
    elif algo == "bt":
        from src.manual_bt_solver import solve_tsp_backtracking
        routes, dist = solve_tsp_backtracking(distance_matrix, depot_index)
        print(f"Backtracking Distance: {dist:.2f} km")
        map_filename = "bt_routes.html"
    elif algo == "bb":
        from src.manual_bb_solver import solve_tsp_branch_and_bound
        routes, dist = solve_tsp_branch_and_bound(distance_matrix, depot_index)
        print(f"Branch and Bound Distance: {dist:.2f} km")
        map_filename = "bb_routes.html"
    else:
        print("Unknown algorithm selected.")
        return

    for i, route in enumerate(routes):
        print(f"Route {i+1}: {route}")
    
    visualize_routes(locations, routes, filename=map_filename)

if __name__ == "__main__":
    main()
