# 🚦 OptiRoute – Solving the Traveling Salesman Problem (TSP)

**OptiRoute** is a Python-based project for solving the **Traveling Salesman Problem (TSP)** using real-world or synthetic location data. It supports multiple algorithms, interactive map visualization, and benchmarking of time and memory usage.

---

##  Features

- Load coordinates from a CSV file
- Compute real-world road distances (via OSMnx)
- Solve TSP using multiple algorithms:
  - Nearest Neighbor + 2-Opt Heuristic
  - Dynamic Programming (Recursive / Iterative)
  - Backtracking with DFS
  - Branch and Bound (Best-First + bounding)
- Visualize routes on **interactive Folium maps**
- Compare time and memory usage per algorithm

---

##  Project Structure

```
optiroute_project/
├── data/
│   ├── road_connected_locations.csv
│   └── road_distance_matrix_km.csv
├── output/
│   ├── benchmark_results.csv
│   └── maps/
│       ├── heuristic_real_road_routes.html
│       └── dp_iter_real_road_routes.html
├── src/
│   ├── data_handler.py
│   ├── manual_heuristic_solver.py
│   ├── manual_dp_solvers.py
│   ├── manual_bt_solver.py
│   ├── manual_bb_solver.py
│   ├── benchmark_utils.py
│   └── visualization_real_roads.py
├── main.py
├── benchmark_runner.py
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

1. **Clone and enter the repo:**
   ```bash
   git clone <repo_url>
   cd optiroute_project
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

##  Running the Project

### Interactive CLI Mode

```bash
python main.py
```

You will be prompted to:
- Enter a CSV file path (e.g., `data/road_connected_locations.csv`)
- Choose how many locations to use (e.g., 10, 15, etc.)
- Select an algorithm (`heuristic`, `dp_rec`, `dp_iter`, `bt`, `bb`)

It will then:
- Solve TSP using real road distances
- Print route and cost in the terminal
- Save an interactive map to `output/maps/`

---

##  Benchmarking All Algorithms

To benchmark all solvers across different input sizes:

```bash
python benchmark_runner.py
```

This generates:
- Route solutions for each algorithm
- Runtime, memory, and distance measurements
- Output saved to:

```
output/benchmark_results.csv
```

Maps are saved to `output/maps/`.

---

##  Algorithm Overview

| Algorithm             | Type       | Optimal? | Time Complexity    | Space Complexity | Notes                          |
|-----------------------|------------|----------|--------------------|------------------|--------------------------------|
| Heuristic (2-Opt + NN)| Approximate| ❌       | O(n²)              | O(n)             | Fast and scalable              |
| DP Recursive          | Exact      | ✅       | O(n² · 2ⁿ)         | O(n · 2ⁿ)        | Held-Karp, top-down            |
| DP Iterative          | Exact      | ✅       | O(n² · 2ⁿ)         | O(n · 2ⁿ)        | Held-Karp, bottom-up           |
| Backtracking          | Exact      | ✅       | O(n!)              | O(n)             | DFS with pruning               |
| Branch and Bound      | Exact      | ✅       | ≤ O(n!)            | O(n²)            | Best-First with lower bounds   |

---

##  Input Format

The input CSV must follow:

```csv
latitude,longitude
42.2957645,-83.712076
42.290783,-83.755797
...
```

- The **first point is the depot** (start and end).
- For testing, `data/road_connected_locations.csv` is provided (30 real road-connected coordinates).

---

## 🌍 Visual Output

- An interactive `.html` map is generated for each route
- Saved under: `output/maps/algorithm_name_real_road_routes.html`
- Markers are labeled: **Start, 1, 2, ...**
- Lines follow **actual road paths**

Example console output:

```
Route 1: [0, 4, 5, 3, 1, 6, 2, 7, 0]
Distance: 33.22 km
```

---

##  Algorithm Recommendations

| Algorithm     | Recommended Input Size | Use Case                        |
|---------------|------------------------|---------------------------------|
| `heuristic`   | ✅ 2–50+                | Fast, scalable, non-optimal     |
| `dp_rec`      | ⚠️ 2–15                | Small inputs only               |
| `dp_iter`     | ⚠️ 2–20                | Better memory vs dp_rec         |
| `bt`          | ❌ 2–10                | Very slow beyond 10 nodes       |
| `bb`          | ⚠️ 2–18                | Slower, but good for optimality |

---



Final project uses static 30 road-connected coordinates (`data/road_connected_locations.csv`).

---

## 📈 Sample Benchmark CSV

```csv
algorithm,num_locations,distance_km,time_sec,memory_kb
heuristic,10,33.2,0.0021,24.3
dp_iter,10,33.2,0.0148,180.3
```

---

## 📌 Tip

For better visuals:
- See numbered markers
- Color-coded solid road paths
- All saved maps are under `output/maps/`

Explore in your browser for step-by-step routes using real driving paths.

---

Happy Routing! 🚗🗺️
