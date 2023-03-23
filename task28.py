a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))

def sum(a, b):
    if a < 0 or b < 0:
        print('Введено не вврное число')
    else:
        if b > 0:
            return sum(a + 1, b - 1)
        else: 
            return a
    
print('Результат суммы чисел: ', sum(a, b))