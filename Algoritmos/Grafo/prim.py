import heapq

class Graph:
    def __init__(self, size):
        self.adj_list = [[] for _ in range(size)]
        self.size = size

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((weight, v))
        self.adj_list[v].append((weight, u))

    def prims_algorithm(self):
        visited = [False] * self.size
        min_heap = [(0, 0)]
        total = 0

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            total += weight

            for edge_weight, v in self.adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (edge_weight, v))

        return total


g = Graph(8)

g.add_edge(0, 1, 4)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 6)
g.add_edge(2, 4, 4)
g.add_edge(2, 7, 2)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 4)
g.add_edge(4, 5, 5)
g.add_edge(4, 6, 3)
g.add_edge(5, 6, 7)
g.add_edge(6, 7, 5)

print(f"Resultado do Prim: {g.prims_algorithm()}")
