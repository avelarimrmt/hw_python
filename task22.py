n = int(input('Количество элементов в массиве 1: '))
m = int(input('Количество элементов в массиве 2: '))

a = [int(input('Введите числа массива 1: ')) for i in range(n)]
b = [int(input('Введите числа массива 2: ')) for i in range(m)]

c = list(set(a+b))
c.sort()
print(c)
    
