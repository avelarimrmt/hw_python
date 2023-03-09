flag = True
while flag:
    num = int(input('Введите номер билета: '))
    if num<=99999 or num>=1000000:
        flag = True
    else :
        flag = False

part1 = num%10 + num//10%10 + num//100%10 
num = num//1000
part2 = num%10 + num//10%10 + num//100%10 
isHappy = part1 == part2
if isHappy:
    print('yes')
else :
    print('no')