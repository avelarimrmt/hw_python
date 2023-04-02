def get_op():
    op = int(input("Введите категорию\n 1 - импорт данных\n 2 - экспорт данных\n 3 - изменение данных\n 4 - удаление данных\n 5 - выход\n "))
    return op

def get_data():
    last_name =input("Введите фамилию: ")
    first_name =input("Введите имя: ")
    middle_name =input("Введите отчество: ")
    phone =input("Введите телефон: ")
    data = last_name + " " + first_name + " "+ middle_name + " " + phone + "\n"
    return data

def find_user():
    data_user = input("Введите параметр поиска: ")
    return data_user

def change_user():
    change_parameter = input("Введите один из параметров контакта, который нужно изменить: ")
    return change_parameter

def choose_str():
    numOfLine = int(input("Введите номер строки, которую нужно изменить или удалить: "))
    return numOfLine

def delete_user():
    delete_parameter = input("Введите один из параметров контакта, который нужно удалить: ")
    return delete_parameter