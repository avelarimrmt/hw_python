n = int(input('Введите количество монеток n: '))
heads = 0
tails = 0

for i in range(n):
    k = int(input('Введите сторону монетки: 0 - орел, 1 - решка: '))
    if k == 1:
        tails += 1
    else:
        heads += 1

if tails > heads:
    print(heads)
else: 
    print(tails)
