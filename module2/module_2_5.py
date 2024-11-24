#"Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        for j in range(m):
            list_.append(value)
        matrix.append(list)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# Вывод на консоль:
# [[10, 10], [10, 10]]
# [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
# [[13, 13], [13, 13], [13, 13], [13, 13]]