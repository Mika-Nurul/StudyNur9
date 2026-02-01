def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    if cols_a != rows_b:
        raise ValueError("Умножение невозможно: число столбцов не равно числу строк")
    
    res = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                res[i][j] += a[i][k] * b[k][j]
    
    return res
a = [[1, 2, 3],
     [4, 5, 6]]
b = [[7, 8],
     [9, 10],
     [11, 12]]
c = matrix_multiply(a, b)
print("Результат умножения:")
for row in c:
    print(row)
