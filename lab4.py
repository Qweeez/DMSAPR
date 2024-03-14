from collections import deque

class EdmondsKarp:
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def bfs(self, s, t, parent):
        visited = [False] * self.rows
        queue = deque()

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v in range(self.rows):
                if visited[v] == False and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return True if visited[t] else False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.rows
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

def read_matrix_from_file(file_path):
    graph = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            graph.append(row)
    return graph

# Зчитуємо матрицю з файлу
file_path = "D:\diskrete models\input_matrix4.txt"  # Шлях до файлу
graph = read_matrix_from_file(file_path)


ek = EdmondsKarp(graph)
source, sink = 0, len(graph) - 1
max_flow = ek.edmonds_karp(source, sink)
print("Максимальний потік:", max_flow)
    