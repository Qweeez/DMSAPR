def boruvka_minimum_spanning_tree(matrix):
    num_vertices = len(matrix)
    mst = []  # Мінімальне остове дерево
    mst_weight = 0  # Вага мінімального остового дерева

    # Ініціалізуємо масив, що вказує на приналежність вершини до компоненту
    components = [i for i in range(num_vertices)]

    while len(set(components)) > 1:
        cheapest = [-1] * num_vertices  # найдешевший ребро для кожної компоненти
        for i in range(num_vertices):
            min_weight = float('inf')
            for j in range(num_vertices):
                if matrix[i][j] != 0:
                    if matrix[i][j] < min_weight and components[i] != components[j]:
                        min_weight = matrix[i][j]
                        cheapest[i] = j

        for i in range(num_vertices):
            if cheapest[i] != -1:
                u, v = i, cheapest[i]
                if components[u] != components[v]:
                    mst.append((u, v, matrix[u][v]))
                    mst_weight += matrix[u][v]
                    old_component = components[u]
                    new_component = components[v]
                    for j in range(num_vertices):
                        if components[j] == old_component:
                            components[j] = new_component

    return mst, mst_weight

def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

# Зчитуємо матрицю з файлу
file_path = "D:\diskrete models\input_matrix.txt"  # Шлях до файлу
matrix = read_matrix_from_file(file_path)


# Знайдемо мінімальне остове дерево методом Бруковки
mst, mst_weight = boruvka_minimum_spanning_tree(matrix)

print("Мінімальне остове дерево:")
for edge in mst:
    print(edge)
print("Вага мінімального остового дерева:", mst_weight)
