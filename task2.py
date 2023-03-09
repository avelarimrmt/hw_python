flag = True
while flag:
    num = int(input('Введите трехзначное число '))
    if num<=99 or num>=1000:
        flag = True
    else :
        flag = False

sum = 0
while num != 0:
    sum += num%10
    num = num//10

print(sum)