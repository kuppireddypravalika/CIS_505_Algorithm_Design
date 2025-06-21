def solve_tsp_manual_heuristic(distance_matrix, depot_index=0):
    import math

    def nearest_neighbor():
        n = len(distance_matrix)
        unvisited = set(range(n))
        unvisited.remove(depot_index)
        route = [depot_index]
        current = depot_index
        while unvisited:
            next_node = min(unvisited, key=lambda x: distance_matrix[current][x])
            route.append(next_node)
            unvisited.remove(next_node)
            current = next_node
        route.append(depot_index)
        return route

    def two_opt(route):
        def total_distance(r):
            return sum(distance_matrix[r[i]][r[i+1]] for i in range(len(r)-1))

        improved = True
        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route) - 1):
                    if j - i == 1:
                        continue
                    new_route = route[:i] + route[i:j][::-1] + route[j:]
                    if total_distance(new_route) < total_distance(route):
                        route = new_route
                        improved = True
        return route

    nn_route = nearest_neighbor()
    optimized_route = two_opt(nn_route)
    total_dist = sum(distance_matrix[optimized_route[i]][optimized_route[i+1]] for i in range(len(optimized_route)-1))
    return [optimized_route], total_dist
