flag = True
while flag:
    s = int(input('Общее количество журавликов '))

    p = int(s/6)
    c = p
    k = 2 * (p + c)
    
    if p + k + c != s:
        flag = True
    else :
        print(f"Петя сделал {p} журавликов")
        print(f"Катя сделала {k} журавликов")
        print(f"Сережа сделал {c} журавликов")
        flag = False
    