n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Введите k - количество долек: '))

if k%n == 0 or k%m == 0:
    print('yes')
else :
    print('no')