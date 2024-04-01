from connect import Database
import main

def login(query, status):
    print(">>>>>>>>>>>>>> Login Page <<<<<<<<<<<<<<<")
    card_num = input("Card number: ")
    password = input("Password: ")

    data = Database.connect(query, "select")

    for i in data:
        if i[3] == card_num and i[4] == password:
            return main.services(card_num, password)
        else:
            print("Karta nomeri yoki password xato kiritilgan")
            return login(query, status)



