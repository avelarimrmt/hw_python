def add_data(data_user):
    with open("task38/file.txt", "a", encoding="UTF-8") as f:
        f.write(data_user)
    
def find_user(parameter):
    with open("task38/file.txt", "r", encoding="UTF-8") as f:
        lst_user = f.readlines()
        for user in lst_user:  
            if parameter in user:
                print(user)
            else: 
                "Такого контакта нет"

def all_user_by_parameters(user_data):
    user_lst_by_prm = []
    with open("task38/file.txt", "r", encoding="UTF-8") as f:
        user_lst = f.readlines()
        for i in user_lst:
            if user_data in i:
                user_lst_by_prm.append(i)
    print(*user_lst_by_prm)
    return user_lst_by_prm, user_lst

def change_user(user_lst_by_prm, user_lst, numOfLine, new_user):
    with open("task38/file.txt", "w", encoding="UTF-8") as f:
        for i in user_lst:
            if user_lst_by_prm[numOfLine - 1] != i:
                f.write(i)
            else:
                f.write(new_user)

def delete_user(user_lst_by_prm, user_lst, numOfLine):
    with open("task38/file.txt", "w", encoding="UTF-8") as f:
        for i in user_lst:
            if user_lst_by_prm[numOfLine - 1] != i:
                f.write(i)
            else:
                continue