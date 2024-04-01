
import login
import register



def services(email, password, phone_num):
    landing = input("""
        1. Login
        2. Register
        0. Stop code
            >>> """)

    if landing == "1":
        return login()

    elif landing == "2":
        return register()
    elif landing == "0":
        print("Good bye")
    else:
        print("Error")
        return services(email, password, phone_num)

if __name__ == "__main__":
    services()