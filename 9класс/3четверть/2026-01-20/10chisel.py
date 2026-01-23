n = []
for i in range(10):
    num = int(input(f"Введите число {i+1}: "))
    n.append(num)
tot = sum(n)
is_ascend = all(n[i] < n[i+1] for i in range(len(n)-1))
print(f"Сумма: {tot}")
print(f"В порядке возрастания: {'Да' if is_ascend else 'Нет'}")
