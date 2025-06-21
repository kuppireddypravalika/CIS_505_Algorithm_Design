def solve_vrp_manual_savings(distance_matrix, num_vehicles=1, depot_index=0):
    import heapq

    n = len(distance_matrix)
    if n <= 2:
        return [[depot_index, depot_index]], 0.0

    # Step 1: Initialize each customer in its own route [depot, i, depot]
    routes = []
    route_map = {}
    for i in range(n):
        if i != depot_index:
            routes.append([depot_index, i, depot_index])
            route_map[i] = len(routes) - 1

    # Step 2: Compute savings
    savings = []
    for i in range(n):
        for j in range(i + 1, n):
            if i == depot_index or j == depot_index:
                continue
            save = distance_matrix[i][depot_index] + distance_matrix[depot_index][j] - distance_matrix[i][j]
            savings.append((save, i, j))
    savings.sort(reverse=True)

    # Step 3: Merge routes based on savings
    for _, i, j in savings:
        ri = route_map.get(i)
        rj = route_map.get(j)

        # Skip if same route, or either has been merged already
        if ri is None or rj is None or ri == rj:
            continue
        if ri >= len(routes) or rj >= len(routes):
            continue
        route_i = routes[ri]
        route_j = routes[rj]

        if not route_i or not route_j:
            continue

        # Only merge if i is at end of route_i and j is at start of route_j
        if route_i[-2] == i and route_j[1] == j:
            merged = route_i[:-1] + route_j[1:]
            routes[ri] = merged
            routes[rj] = []  # mark as merged
            for customer in route_j[1:-1]:
                route_map[customer] = ri

    # Remove empty routes
    routes = [r for r in routes if r]

    # Combine into a single route if only one vehicle
    if num_vehicles == 1:
        final_route = []
        for r in routes:
            for customer in r[1:-1]:  # skip repeated depot
                final_route.append(customer)
        route = [depot_index] + final_route + [depot_index]
        total_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        return [route], total_distance

    # Multi-vehicle support (optional)
    all_routes = []
    total_distance = 0.0
    for r in routes:
        total_distance += sum(distance_matrix[r[i]][r[i+1]] for i in range(len(r)-1))
        all_routes.append(r)
    return all_routes, total_distance
