import itertools

def tsp_brute_force(matrix):
    num_vertices = len(matrix)
    min_distance = float('inf')
    optimal_path = None

    for perm in itertools.permutations(range(1, num_vertices)):
        perm = (0,) + perm + (0,)
        distance = calculate_distance(perm, matrix)
        if distance < min_distance:
            min_distance = distance
            optimal_path = perm

    return optimal_path, min_distance

def calculate_distance(path, matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += matrix[path[i]][path[i+1]]
    return total_distance

def tsp_branch_and_bound(matrix):
    num_vertices = len(matrix)
    optimal_path = None
    min_distance = float('inf')
    visited = [False] * num_vertices
    visited[0] = True

    def tsp_recursive(curr_pos, curr_distance, path):
        nonlocal optimal_path, min_distance

        if len(path) == num_vertices:
            curr_distance += matrix[curr_pos][0]  # Повернутися до початку
            if curr_distance < min_distance:
                min_distance = curr_distance
                optimal_path = path[:]
            return

        for next_pos in range(num_vertices):
            if not visited[next_pos] and matrix[curr_pos][next_pos] != 0:
                visited[next_pos] = True
                tsp_recursive(next_pos, curr_distance + matrix[curr_pos][next_pos], path + [next_pos])
                visited[next_pos] = False

    tsp_recursive(0, 0, [0])

    return optimal_path, min_distance

def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

# Зчитуємо матрицю з файлу
file_path = "D:\diskrete models\input_matrix3.txt"  # Шлях до файлу
matrix = read_matrix_from_file(file_path)

# Розв'язати задачу комівояжера за допомогою алгоритму гілок та границь
path, total_distance = tsp_branch_and_bound(matrix)

# Вивести результат
print("Оптимальний маршрут:", path)
print("Загальна відстань:", total_distance)
