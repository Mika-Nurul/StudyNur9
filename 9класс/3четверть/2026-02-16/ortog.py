v = [[1, 0],[0, 1],[1, 1],[2, -2],[3, 0]]

for i in range(len(v)):
    for j in range(i + 1, len(v)):
        d = 0
        for k in range(len(v[i])):
            d += v[i][k] * v[j][k]
        
        if d == 0:
            print(v[i], "и", v[j], "— ортогональны")
