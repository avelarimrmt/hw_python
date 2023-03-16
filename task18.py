n = int(input('Количество элементов в массиве: '))
a = []


for i in range(n):
    a.append(int(input()))
    
x = a[-1]
res = a[0]

for i in range(n-1):
    if x-a[i]<x-res:
        res=a[i]

print(f"Ближайшее к {x} число: {res}")