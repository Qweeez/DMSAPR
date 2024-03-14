def tsp_greedy(matrix):
    num_vertices = len(matrix)
    visited = [False] * num_vertices
    path = [0]  # Почати з першого міста
    total_distance = 0

    while len(path) < num_vertices:
        current_vertex = path[-1]
        nearest_neighbor = None
        min_distance = float('inf')

        for neighbor in range(num_vertices):
            if not visited[neighbor] and matrix[current_vertex][neighbor] != 0:
                distance = matrix[current_vertex][neighbor]
                if distance < min_distance:
                    min_distance = distance
                    nearest_neighbor = neighbor

        path.append(nearest_neighbor)
        visited[nearest_neighbor] = True
        total_distance += min_distance

    # Закриваємо цикл, повертаючись до початкового міста
    total_distance += matrix[path[-1]][0]
    path.append(0)

    return path, total_distance

def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

# Зчитуємо матрицю з файлу
file_path = "D:\diskrete models\input_matrix1.txt"  # Шлях до файлу
matrix = read_matrix_from_file(file_path)
# Розв'язати задачу листоноші
path, total_distance = tsp_greedy(matrix)

# Вивести результат
print("Оптимальний маршрут:", path)
print("Загальна відстань:", total_distance)
