a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов: '))
pr =  [a1 + (i - 1) * d for i in range(1, n + 1)]
print(pr)