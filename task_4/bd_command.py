import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os.path


base_name = "users.db"
file_path = r"D:\Study\Platforms\ItStep\less31\homework\task_4\users.db"


def create(db_name):
    with sqlite3.connect(db_name) as users_connect:
        users_connect.execute("""
        CREATE TABLE IF NOT EXISTS users
        (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(50),
            short_name VARCHAR(30),
            birthday DATA,
            email VARCHAR(60) UNIQUE
            
            );
        """)
        users_connect.execute("""CREATE UNIQUE INDEX users_connect ON users(email);""")
        users_connect.commit()


def register_new_user(*user_data, base_n="users.db"):

    """
    :param user_data: keep this order full_name(first middle last names), birthday(YYYY-MM-DD), email
    :param base_n: base_n: str, if you want to change directory - input full adress
    :return: this function will add user data in base_n.bd

    """

    if not os.path.exists(file_path):
        create(base_n)
    else:
        print(f"File {file_path} already exist")

    short_name = f"{user_data[0].split()[1]} {user_data[0].split()[0][0]}.{user_data[0].split()[2][0]}."
    connect_db = sqlite3.connect(base_n)
    cursor_db = connect_db.cursor()
    try:
        cursor_db.execute(f"INSERT INTO users "
                          f"VALUES(NULL, '{user_data[0]}', '{short_name}', '{user_data[1]}', '{user_data[2]}'); ")
        connect_db.commit()

        msg = MIMEMultipart()
        message = f"Thank you for registration {user_data[0]}!!!"
        password = 'bexmumhiiuwqvviu'
        msg['From'] = 'diandrey16@gmail.com'
        msg['To'] = f"{user_data[2]}"
        msg['Subject'] = "Thanks!"
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

    except sqlite3.IntegrityError:
        print("this email already exists")
    finally:
        connect_db.close()


def searcher(search_in, word, base_n="users.db"):
    connect_db = sqlite3.connect(base_n)
    cursor_db = connect_db.cursor()

    try:
        if search_in == "name":
            search = cursor_db.execute(f"""SELECT user_id, full_name, short_name, birthday, email FROM users WHERE full_name 
            LIKE '{word} % %';""").fetchall()
            print(search)
        elif search_in == "email":
            search = cursor_db.execute(f"""SELECT user_id, full_name, short_name, birthday, email FROM users WHERE email 
            LIKE '{word}';""").fetchall()
            print(search)
        elif search_in == "last_name":
            search = cursor_db.execute(f"""SELECT user_id, full_name, short_name, birthday, email FROM users WHERE full_name
            LIKE '% {word} %';""").fetchall()
            print(search)

    except sqlite3.IntegrityError:
        print("Error")
    finally:
        connect_db.close()
