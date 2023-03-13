import math
s = int(input('Введите сумму чисел S: '))
p = int(input('Введите произведение чисел P: '))


a = 1
b = -s
c = p
dis = b*b - 4*a*c

if dis < 0:
    x = int(-b / 2*a)
else:
    x = int((-b + math.sqrt(dis)) / (2*a))

y = s - x

print(x, y)
