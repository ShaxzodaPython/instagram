import random
from connect import Database
import login


def register():
    print(">>>>>>>>>>>>>> Register <<<<<<<<<<<<<<<")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone_num = input("Phone number: ")
    random_num = random.randint(999,10000)
    print(random_num)
    code = input("Tasdiqlash kodini kiriting: ")
    while code == random_num:
        print("Reply enter code: ")
        code = input("Tasdiqlash kodini kiriting: ")
    password_1 = input("Password: ")
    password_2 = input("Reply enter password: ")
    while password_1 != password_2:
        password_1 = input("Password: ")
        password_2 = input("Reply enter password: ")



    query = f"""INSERT INTO users(first_name, last_name, email, phone_num, password)
            VALUES('{first_name}', '{last_name}', '{email}', '{phone_num}','{password_1}')"""


    print(Database.connect(query, "insert"))
    return login()

