import heapq

def solve_tsp_branch_and_bound(distance_matrix, depot_index=0):
    n = len(distance_matrix)
    visited_all = (1 << n) - 1
    best_cost = float('inf')
    best_path = []

    class Node:
        def __init__(self, level, path, cost, bound, visited_mask):
            self.level = level
            self.path = path
            self.cost = cost
            self.bound = bound
            self.visited_mask = visited_mask

        def __lt__(self, other):
            return self.bound < other.bound

    def calculate_bound(curr_node):
        bound = curr_node.cost
        unvisited = [i for i in range(n) if not (curr_node.visited_mask & (1 << i))]

        # Add minimum outgoing edge from last node
        if unvisited:
            min_out = min([distance_matrix[curr_node.path[-1]][j] for j in unvisited])
            bound += min_out

        # Add minimal outgoing edge for all unvisited nodes
        for i in unvisited:
            min_edge = float('inf')
            for j in range(n):
                if i != j and not (curr_node.visited_mask & (1 << j)):
                    min_edge = min(min_edge, distance_matrix[i][j])
            if min_edge != float('inf'):
                bound += min_edge
        return bound

    pq = []
    start_node = Node(1, [depot_index], 0, 0, 1 << depot_index)
    start_node.bound = calculate_bound(start_node)
    heapq.heappush(pq, start_node)

    while pq:
        node = heapq.heappop(pq)

        if node.bound >= best_cost:
            continue

        if node.level == n:
            final_cost = node.cost + distance_matrix[node.path[-1]][depot_index]
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = node.path + [depot_index]
            continue

        for i in range(n):
            if node.visited_mask & (1 << i):
                continue
            new_path = node.path + [i]
            new_cost = node.cost + distance_matrix[node.path[-1]][i]
            new_visited = node.visited_mask | (1 << i)
            child_node = Node(node.level + 1, new_path, new_cost, 0, new_visited)
            child_node.bound = calculate_bound(child_node)
            if child_node.bound < best_cost:
                heapq.heappush(pq, child_node)

    return [best_path], best_cost if best_path else ([], float('inf'))
