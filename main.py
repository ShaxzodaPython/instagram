
import login
import register
import query


def main():
    landing = input("""
        1. Login
        2. Register
        0. Stop code
            >>> """)

    if landing == "1":
        return login.login()

    elif landing == "2":
        return register.register()
    elif landing == "0":
        print("Good bye")
    else:
        print("Error")
        return main()