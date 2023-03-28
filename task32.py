n = int(input('Количество элементов в массиве: '))
a = []
b = []
count = 0

for i in range(n):
    a.append(int(input()))

d1 = int(input('Введите диапазон от: '))
d2 = int(input('Введите диапазон до: '))

for i in range(n):
    if a[i]>=d1 and a[i]<=d2:
        b.append(f'{i}')

print(b)