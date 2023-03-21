n = int(input('Количество кустов: '))
a = [int(input(f'Количество ягод на {i+1} кусте: ')) for i in range(n)]

maxY = 0

for i in range(n):
    if i != 0 and i != n-1:
        col = a[i - 1] + a[i] + a[i + 1]
    else:
        if i == 0:
            col = a[n-1] + a[i] + a[i + 1]
        else:
            col = a[i - 1] + a[i] + a[0]

    if maxY < col:
        maxY = col

print(maxY)