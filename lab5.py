def isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False

    # Функція для знаходження сусідніх вершин
    def get_neighbors(graph, vertex):
        return [i for i, v in enumerate(graph[vertex]) if v]

    def check_isomorphism(mapping):
        for v1, v2 in mapping.items():
            neighbors1 = get_neighbors(graph1, v1)
            neighbors2 = get_neighbors(graph2, v2)
            if len(neighbors1) != len(neighbors2):
                return False
            for n1 in neighbors1:
                n2 = mapping.get(n1, None)
                if n2 is None or n2 not in neighbors2:
                    return False
        return True

    def dfs(mapping, visited):
        if len(mapping) == len(graph1):
            return check_isomorphism(mapping)
        for v1 in range(len(graph1)):
            if v1 not in mapping:
                for v2 in range(len(graph2)):
                    if v2 not in mapping.values():
                        mapping[v1] = v2
                        if dfs(mapping, visited):
                            return True
                        del mapping[v1]
        return False

    return dfs({}, set())

# Графи
graph1 = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

graph2 = [
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

if isomorphic(graph1, graph2) == True:
    print('Графи ізоморфні')
else:
    print('Графи не ізоморфні')

