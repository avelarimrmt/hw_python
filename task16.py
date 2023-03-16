n = int(input('Количество элементов в массиве: '))
a = []
count = 0

for i in range(n):
    a.append(int(input()))
    
x = a[-1]

for i in range(n):
    if (a[i] == x):
        count +=1

print(f"Цифра {x} встречается {count} раз.")