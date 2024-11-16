def get_matrix(n, m, value):
    # Если количество строк или столбцов меньше или равно 0, возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем матрицу из n строк и m столбцов, заполненную значением value
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)

    return matrix


# Пример вызова функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)