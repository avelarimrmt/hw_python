import view
import db

def main():
    while True:
        op = view.get_op()
        if op == 1:
            data_user = view.get_data()
            db.add_data(data_user)
        if op == 2:
            find_user = view.find_user()
            db.find_user(find_user)
        if op == 3:
            change_user = view.change_user()
            user_lst_by_prm, user_lst = db.all_user_by_parameters(change_user)
            numOfLine = view.choose_str()
            print("Введи новые данные контакта")
            new_user = view.get_data()
            db.change_user(user_lst_by_prm, user_lst, numOfLine, new_user)
        if op == 4:
            delete_user = view.delete_user()
            user_lst_by_prm, user_lst = db.all_user_by_parameters(delete_user)
            numOfLine = view.choose_str()
            db.delete_user(user_lst_by_prm, user_lst, numOfLine)
        if op == 5:
            break