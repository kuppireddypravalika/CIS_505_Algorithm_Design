from src.data_handler import load_data, compute_distance_matrix
from src.visualization_real_roads import visualize_routes_real_roads as visualize_routes  # use real road version
from src.manual_heuristic_solver import solve_tsp_manual_heuristic
from src.manual_dp_solvers import solve_tsp_dp_recursive, solve_tsp_dp_iterative
from src.manual_bt_solver import solve_tsp_backtracking
from src.manual_bb_solver import solve_tsp_branch_and_bound
from src.benchmark_utils import measure_time_and_memory

def main():
    print("🚦 Smart Cities TSP Solver using Real-World Road Distances")

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

    func_map = {
        "heuristic": solve_tsp_manual_heuristic,
        "dp_rec": solve_tsp_dp_recursive,
        "dp_iter": solve_tsp_dp_iterative,
        "bt": solve_tsp_backtracking,
        "bb": solve_tsp_branch_and_bound
    }

    if algo not in func_map:
        print(" Unknown algorithm selected.")
        return

    func = func_map[algo]
    (routes, dist), time_taken, memory_kb = measure_time_and_memory(func, distance_matrix, depot_index)

    print(f"\n✅ {algo.upper()} Algorithm Results:")
    print(f"  Total Distance : {dist:.2f} km")
    print(f"  Time Taken     : {time_taken:.4f} seconds")
    print(f"  Peak Memory    : {memory_kb:.2f} KB")

    for i, route in enumerate(routes):
        print(f"Route {i+1}: {route}")

    map_filename = f"output/maps/{algo}_real_road_routes.html"

    visualize_routes(locations, routes, filename=map_filename)

if __name__ == "__main__":
    main()
