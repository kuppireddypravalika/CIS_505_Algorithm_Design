import math

def solve_tsp_backtracking(distance_matrix, depot_index=0):
    n = len(distance_matrix)
    visited = [False] * n
    best_cost = [math.inf]
    best_path = []

    def backtrack(path, cost_so_far):
        current = path[-1]
        if len(path) == n:
            total_cost = cost_so_far + distance_matrix[current][depot_index]
            if total_cost < best_cost[0]:
                best_cost[0] = total_cost
                best_path.clear()
                best_path.extend(path + [depot_index])
            return

        for next_city in range(n):
            if not visited[next_city]:
                new_cost = cost_so_far + distance_matrix[current][next_city]
                if new_cost < best_cost[0]:  # pruning
                    visited[next_city] = True
                    path.append(next_city)
                    backtrack(path, new_cost)
                    path.pop()
                    visited[next_city] = False

    visited[depot_index] = True
    backtrack([depot_index], 0)

    return [best_path], best_cost[0]
