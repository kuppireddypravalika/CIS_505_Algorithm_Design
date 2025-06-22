def solve_tsp_dp_recursive(distance_matrix, depot_index=0):
    import math

    n = len(distance_matrix)
    memo = {}

    def tsp(pos, visited):
        if visited == (1 << n) - 1:
            return distance_matrix[pos][depot_index]
        key = (pos, visited)
        if key in memo:
            return memo[key]
        min_cost = math.inf
        for city in range(n):
            if not (visited >> city) & 1:
                cost = distance_matrix[pos][city] + tsp(city, visited | (1 << city))
                min_cost = min(min_cost, cost)
        memo[key] = min_cost
        return min_cost

    def get_path():
        visited = 1 << depot_index
        pos = depot_index
        path = [depot_index]
        for _ in range(n - 1):
            best = -1
            best_cost = math.inf
            for city in range(n):
                if not (visited >> city) & 1:
                    cost = distance_matrix[pos][city] + tsp(city, visited | (1 << city))
                    if cost < best_cost:
                        best_cost = cost
                        best = city
            path.append(best)
            visited |= 1 << best
            pos = best
        path.append(depot_index)
        return path

    total_cost = tsp(depot_index, 1 << depot_index)
    route = get_path()
    return [route], total_cost

def solve_tsp_dp_iterative(distance_matrix, depot_index=0):
    import math

    n = len(distance_matrix)
    dp = [[math.inf] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]  

    dp[1 << depot_index][depot_index] = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or u == v:
                    continue
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + distance_matrix[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    parent[new_mask][v] = u

    
    full_mask = (1 << n) - 1
    min_cost = math.inf
    last_city = -1

    for i in range(n):
        cost = dp[full_mask][i] + distance_matrix[i][depot_index]
        if cost < min_cost:
            min_cost = cost
            last_city = i

    path = [depot_index]  
    mask = full_mask
    current_city = last_city

    while current_city != depot_index:
        path.append(current_city)
        prev_city = parent[mask][current_city]
        mask = mask ^ (1 << current_city)
        current_city = prev_city

    path.append(depot_index)
    path.reverse()
    return [path], min_cost
