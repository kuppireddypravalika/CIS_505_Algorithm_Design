
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def solve_vrp_ortools(distance_matrix, num_vehicles, depot_index):
    # Scale to integers (meters) for OR-Tools
    scaled_matrix = [[int(d * 1000) for d in row] for row in distance_matrix]

    manager = pywrapcp.RoutingIndexManager(len(scaled_matrix), num_vehicles, depot_index)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return scaled_matrix[from_node][to_node]  # Integer distances (in meters)

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        routes = []
        total_cost = 0
        for vehicle_id in range(num_vehicles):
            index = routing.Start(vehicle_id)
            route = []
            while not routing.IsEnd(index):
                route.append(manager.IndexToNode(index))
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                total_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route.append(manager.IndexToNode(index))
            routes.append(route)

        return routes, total_cost / 1000.0  # Convert meters back to km

    return None, None

def two_opt(route, dist_func):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                # Ensure j is not out of bounds and i < j
                if j + 1 >= len(route):
                    continue

                current_dist = dist_func(route[i-1], route[i]) + \
                               dist_func(route[j], route[j+1])
                new_dist = dist_func(route[i-1], route[j]) + \
                           dist_func(route[i], route[j+1])

                if new_dist < current_dist:
                    new_route = route[:i] + route[j:i-1:-1] + route[j+1:]
                    route[:] = new_route # Modify in place
                    improved = True
                    break
            if improved:
                break
    return route

def solve_vrp_heuristic(distance_matrix, depot_index):
    num_locations = len(distance_matrix)
    unvisited = set(range(num_locations))
    unvisited.remove(depot_index)
    
    current_node = depot_index
    route = [current_node]
    
    while unvisited:
        next_node = -1
        min_dist = float("inf")
        for neighbor in unvisited:
            if distance_matrix[current_node][neighbor] < min_dist:
                min_dist = distance_matrix[current_node][neighbor]
                next_node = neighbor
        
        route.append(next_node)
        current_node = next_node
        unvisited.remove(next_node)
    
    route.append(depot_index) # Return to depot

    # Apply 2-Opt
    def dist_func(node1_idx, node2_idx):
        return distance_matrix[node1_idx][node2_idx]

    optimized_route = two_opt(route, dist_func)

    total_distance = 0
    for i in range(len(optimized_route) - 1):
        total_distance += distance_matrix[optimized_route[i]][optimized_route[i+1]]

    return [optimized_route], total_distance


