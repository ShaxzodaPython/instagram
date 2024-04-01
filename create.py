from connect import Database

def create_table():
    users = """CREATE TABLE IF NOT EXISTS users(
            users_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30),
            username VARCHAR(30) NOT NULL,
            phone_num Varchar(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            email VARCHAR(30) NOT NULL,
            create_date TIMESTAMP DEFAULT now())"""

    confirmation = """CREATE TABLE IF NOT EXISTS confirmation(
            confirmation_id SERIAL PRIMARY KEY,
            user_email REERENCES users(email),
            code VARCHAR(15) NOT NULL,
            status BOOLEAN,
            create_date TIMESTAMP DEFAULT now())"""
#statusda tel. raqam tekshiriladi. Ya'ni False bo'lsa karta tel. raqamga ulanmagan, True bo'lsa ulangan

    print(Database.connect(users, 'create'))
    print(Database.connect(confirmation, 'create'))


if __name__ == '__main__':
    create_table()


