import csv
from src.data_handler import load_data, compute_distance_matrix
from src.benchmark_utils import measure_time_and_memory
from src.manual_heuristic_solver import solve_tsp_manual_heuristic
from src.manual_dp_solvers import solve_tsp_dp_recursive, solve_tsp_dp_iterative
from src.manual_bt_solver import solve_tsp_backtracking
from src.manual_bb_solver import solve_tsp_branch_and_bound

ALGORITHMS = {
    "heuristic": solve_tsp_manual_heuristic,
    "dp_rec": solve_tsp_dp_recursive,
    "dp_iter": solve_tsp_dp_iterative,
    "bt": solve_tsp_backtracking,
    "bb": solve_tsp_branch_and_bound
}

INPUT_SIZES = [5, 10, 15]  # Expand this as needed

def benchmark(algorithm_name, num_locations):
    func = ALGORITHMS[algorithm_name]
    locations = load_data("data/synthetic_locations.csv", num_locations=num_locations)
    distance_matrix = compute_distance_matrix(locations)

    try:
        (routes, distance), time_sec, memory_kb = measure_time_and_memory(func, distance_matrix, depot_index=0)
        return {
            "algorithm": algorithm_name,
            "num_locations": num_locations,
            "distance_km": round(distance, 2),
            "time_sec": round(time_sec, 4),
            "memory_kb": round(memory_kb, 2)
        }
    except Exception as e:
        print(f"❌ Failed for {algorithm_name} with {num_locations} nodes: {e}")
        return None

def run_all_benchmarks(output_csv="output/benchmark_results.csv"):
    results = []
    for size in INPUT_SIZES:
        for algo in ALGORITHMS:
            print(f"▶ Running {algo} on {size} locations...")
            result = benchmark(algo, size)
            if result:
                results.append(result)

    if results:
        with open(output_csv, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"\n✅ Results saved to {output_csv}")

if __name__ == "__main__":
    run_all_benchmarks()
