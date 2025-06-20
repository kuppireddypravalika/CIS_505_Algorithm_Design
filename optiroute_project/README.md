# OptiRoute – Efficient Vehicle Routing with Exact & Heuristic Algorithms

This project provides a prototype for solving Vehicle Routing Problems (VRP) using both exact (Google OR-Tools) and heuristic (Nearest Neighbor + 2-Opt) algorithms. The goal is to find optimal delivery routes for a fleet of vehicles from a central depot to multiple customer locations, minimizing total distance or travel time.

## Project Structure

```
optiroute_project/
├── data/                 # Placeholder for data files (e.g., customer locations CSV)
├── notebooks/            # Placeholder for Jupyter notebooks for analysis or experimentation
├── src/                  # Source code for the OptiRoute project
│   ├── __init__.py       # Makes `src` a Python package
│   ├── data_handler.py   # Handles data loading and distance matrix computation
│   ├── solvers.py        # Contains OR-Tools and heuristic VRP solvers
│   └── visualization.py  # Handles route visualization using Folium
├── main.py               # Main script to run the VRP solvers and generate visualizations
└── requirements.txt      # Lists Python dependencies
```

## Setup Instructions

To set up and run this project, follow these steps:

1.  **Navigate to the project directory:**

    ```bash
    cd optiroute_project
    ```

2.  **Install dependencies:**

    It is highly recommended to use a virtual environment to manage project dependencies. If you don't have `venv` installed, you might need to install it first (`sudo apt-get install python3.11-venv` on Ubuntu).

    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

    If you are on Windows, use `venv\Scripts\activate` instead of `source venv/bin/activate`.

## How to Run the Project

After setting up the environment and installing dependencies, you can run the main script:

```bash
python main.py
```

This script will:
*   Load dummy location data (or from a CSV if specified).
*   Compute the distance matrix between locations.
*   Solve the VRP using Google OR-Tools (exact solver).
*   Solve the VRP using the Nearest Neighbor + 2-Opt heuristic solver.
*   Generate interactive HTML maps (`ortools_routes.html` and `heuristic_routes.html`) in the project root directory, visualizing the routes found by each solver.
*   Print the total distance for the routes found by each solver to the console.

## Making Changes and Customization

### Data Input (`src/data_handler.py`)

The `load_data` function currently uses hardcoded example coordinates. To use your own data:

1.  **Prepare your data:** Create a CSV file (e.g., `my_locations.csv`) with at least `latitude` and `longitude` columns. You can place this file in the `data/` directory.

    Example `my_locations.csv`:
    ```csv
    latitude,longitude
    34.0522,-118.2437
    34.0550,-118.2500
    34.0600,-118.2400
    34.0400,-118.2600
    ```

2.  **Update `main.py`:** Modify the `main.py` file to point to your CSV file:

    ```python
    # In main.py
    locations = load_data(filepath="data/my_locations.csv") # Update this line
    ```

### Solver Parameters (`main.py`)

You can adjust parameters like the number of vehicles or the depot index in `main.py`:

```python
# In main.py
num_vehicles = 2 # Change this to the desired number of vehicles
depot_index = 0  # Change this if your depot is at a different index in your locations list
```

### Heuristic Algorithm (`src/solvers.py`)

The `two_opt` function implements a basic 2-Opt local search. For more advanced heuristics or different initial tour constructions, you would modify `src/solvers.py`.

### Visualization (`src/visualization.py`)

To customize the map visualization (e.g., colors, markers, popups), edit `src/visualization.py`.

## Expected Output

Upon successful execution, you will see console output similar to this:

```
Loading data...

Solving with OR-Tools...
OR-Tools Total Distance: XX.XX km
  Vehicle 1 Route: [0, 2, 1, 3, 0]
Map saved to ortools_routes.html

Solving with Heuristic (Nearest Neighbor + 2-Opt)...
Heuristic Total Distance: YY.YY km
  Vehicle 1 Route: [0, 1, 2, 3, 0]
Map saved to heuristic_routes.html
```

Two HTML files (`ortools_routes.html` and `heuristic_routes.html`) will be generated in the `optiroute_project` directory. Open these files in a web browser to view the interactive maps with the calculated routes.


