a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def degree(a, b):
    if b != 1:
        return a * degree(a, b - 1)
    else: 
        return a
    
print('Результат возведения в степень: ', degree(a, b))