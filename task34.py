line = input('Введите стихотворение')
lines = line.split()

print(lines)

lst = [sum(x in 'уеыаоэяию' for x in lin)
for lin in lines]

if len(set(lst)) == 1 :
    result = "Парам пам-пам"
else: result = "Пам парам"

print(result)