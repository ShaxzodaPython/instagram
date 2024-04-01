from connect import Database
import main

def login(query, status):
    print(">>>>>>>>>>>>>> Login Page <<<<<<<<<<<<<<<")
    email = input("E-mail: ")
    phone_num = input("Phone number: ")
    password = input("Password: ")

    data = Database.connect(query, "select")

    for i in data:
        if i[6] == email and i[5] == password and phone_num == i[4]:
            print("Xush kelibsiz😊")
            return main.services(email, password, phone_num)
        else:
            print("email or password is incorrect")
            return login(query, status)



