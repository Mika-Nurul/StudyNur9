def insert_sort(arr):
    m = arr.copy()
    for i in range(1, len(m)):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j+1] = m[j]
            j -= 1
        m[j+1] = key
    return m

l = list(map(int, input("Введите числа через пробел: ").split()))
sorted_l = insert_sort(l)
print("Отсортированный массив:", sorted_l)
