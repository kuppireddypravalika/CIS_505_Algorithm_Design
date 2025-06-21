
#  OptiRoute – Solving the Traveling Salesman Problem (TSP)

**OptiRoute** is a Python-based project that provides multiple algorithms to solve the **Traveling Salesman Problem (TSP)** using real or synthetic geolocation data. The project supports **interactive route visualization**, **performance benchmarking**, and **flexible data input**.

---

##  Features

- Load locations from a CSV or use default coordinates
- Compute real-world distance matrices (via `geopy`)
- Solve TSP using multiple algorithms:
  - Nearest Neighbor + 2-Opt Heuristic
  - Dynamic Programming (Recursive & Iterative Held-Karp)
  - Backtracking (DFS with pruning)
  - Branch and Bound (Best-First Search with bounding)
- Visualize routes on interactive maps using Folium
- Benchmark algorithms by runtime and memory usage

---

## 📁 Project Structure

```
optiroute_project/
├── data/                   # CSV files for location input
├── output/                 # Benchmark results and HTML maps
├── src/                    # Source code
│   ├── data_handler.py     # CSV loading and distance matrix computation
│   ├── manual_heuristic_solver.py
│   ├── manual_dp_solvers.py
│   ├── manual_bt_solver.py
│   ├── manual_bb_solver.py
│   ├── visualization.py    # Folium map generator
│   └── benchmark_utils.py  # Time and memory measurement wrapper
├── main.py                 # Interactive CLI runner for TSP solvers
├── benchmark_runner.py     # Automated benchmarking for time/memory
└── requirements.txt        # Dependencies
```

---

##  Setup Instructions

1. **Clone and navigate to the project:**
   ```bash
   git clone <repo_url>
   cd optiroute_project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Project

### Interactive Mode (Visual + Prompted)
```bash
python main.py
```

You’ll be prompted to:
- Choose a CSV file or use default coordinates
- Select how many locations to use
- Choose an algorithm

It will then:
- Solve the TSP
- Print distance and route
- Save an interactive HTML map (e.g., `dp_iter_routes.html`)

---

##  Benchmarking Multiple Algorithms

To test all algorithms across different input sizes and save performance metrics:

```bash
python benchmark_runner.py
```

This will:
- Run all algorithms on input sizes (e.g., 5, 10, 15, all)
- Record execution time, memory usage, and route distance
- Save results to:
  ```
  output/benchmark_results.csv
  ```

> Optional: Enable route maps for each run inside `benchmark_runner.py`.

---

##  Algorithm Overview

| Algorithm       | Type      | Optimal? | Time Complexity      | Space Complexity | Notes |
|----------------|-----------|----------|----------------------|------------------|-------|
| Heuristic (NN + 2-Opt) | Approximate | ❌ | O(n²) + O(n² * passes) | O(n) | Fast, scalable |
| DP Recursive    | Exact     | ✅ | O(n² * 2ⁿ)             | O(n * 2ⁿ)         | Held-Karp, top-down |
| DP Iterative    | Exact     | ✅ | O(n² * 2ⁿ)             | O(n * 2ⁿ)         | Bottom-up Held-Karp |
| Backtracking    | Exact     | ✅ | O(n!)                  | O(n)              | DFS + pruning |
| Branch & Bound  | Exact     | ✅ | ≤ O(n!) (varies)       | O(n²)             | Best-First + bounds |

---

##  Benchmark Example

Sample CSV output from `benchmark_runner.py`:

```csv
algorithm,num_locations,distance_km,time_sec,memory_kb
heuristic,10,132.5,0.0021,24.3
dp_rec,10,132.5,0.3112,210.0
dp_iter,10,132.5,0.0148,180.3
bt,10,132.5,4.204,234.6
bb,10,132.5,0.8823,154.7
```

---

## Input Format

CSV must contain:
```csv
latitude,longitude
34.0522,-118.2437
34.0600,-118.2500
...
```

- The first point is the **depot** (starting and ending node).
- Use `generate_synthetic_coords.py` to create test data if needed.

---

##  Visual Output

Each route is saved as an interactive HTML map. Example:
```
Route 1: [0, 3, 1, 2, 4, 0]
Distance: 12.76 km
Map saved to dp_iter_routes.html
```

Open in browser to explore.

---

##  Extending the Project

You can:
- Add more heuristics (e.g., Christofides, Genetic Algorithm)
- Visualize benchmarking results via Matplotlib
- Benchmark scalability (10–50 nodes)
- Replace air distances with road network using OSMnx
