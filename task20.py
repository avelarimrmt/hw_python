dictionary = {1:'AEIOULNSTRАВЕИНОРСТ', 
              2:'DGДКЛМПУ',
              3:'BCMPБГЁЬЯ',
              4:'FHVWYЙЫ',
              5:'KЖЗХЦЧ',
              8:'JXШЭЮ',
              10:'QZФЩЪ'}

s = input('Введите слово: ').upper()
sum = 0
for i in range(len(s)):
    for key, value in dictionary.items():
        if s[i] in value:
            sum += int(key)                

print(sum)