def projection(a, b):
    d = 0
    normbsq = 0
    for i in range(len(a)):
        d += a[i] * b[i]
        normbsq += b[i] * b[i]
    if normbsq == 0:
        raise ValueError("Вектор b не должен быть нулевым")
    f = d / normbsq
    res = []
    for i in range(len(b)):
        result.append(f * b[i])

    return res


a = [3, 4]
b = [1, 0]

print("Проекция:", projection(a, b))
