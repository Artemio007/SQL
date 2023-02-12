import sqlite3
import datetime
from datetime import datetime
from datetime import date
from less31.homework.task_4.bd_command import create, register_new_user, searcher


base_name = "users.db"


class User:
    def __init__(self, exist_sql_base, email_address):
        self.exist_sql_base = exist_sql_base
        self.email_address = email_address

    def __str__(self):
        connect_users = sqlite3.connect(self.exist_sql_base)
        cursor_users = connect_users.cursor()
        get_date = cursor_users.execute(
            f"SELECT full_name, birthday FROM users WHERE (email = '{self.email_address}'); ").fetchall()
        print(f"{get_date[0][0]} was born {get_date[0][1]}")
        cursor_users.close()

    def get_full_name(self):
        connect_users = sqlite3.connect(self.exist_sql_base)
        cursor_users = connect_users.cursor()
        get_full = cursor_users.execute(f"SELECT full_name FROM users WHERE (email = '{self.email_address}'); ").fetchall()
        print(get_full[0][0])
        cursor_users.close()
        return get_full

    def get_short_name(self):
        connect_users = sqlite3.connect(self.exist_sql_base)
        cursor_users = connect_users.cursor()
        get_short = cursor_users.execute(f"SELECT short_name FROM users WHERE (email = '{self.email_address}'); ").fetchall()
        print(get_short[0][0])
        cursor_users.close()
        return get_short

    def get_age(self):
        connect_users = sqlite3.connect(self.exist_sql_base)
        cursor_users = connect_users.cursor()
        get_date = cursor_users.execute(
            f"SELECT birthday FROM users WHERE (email = '{self.email_address}'); ").fetchall()
        birth = date.fromisoformat(get_date[0][0])
        print(f"{round((datetime.now().date() - birth).days / 365, 1)} years")
        cursor_users.close()


if __name__ == "__main__":
    register_new_user("Artem Mozalev Vitaliewich", "1998-06-24", "sireartem@gmail.com")
    register_new_user("Artemio Mozalev Vitaliewich", "1998-06-24", "mvamvh@gmail.com")
    searcher('name', 'Artem')
    searcher('email', 'sireartem@gmail.com')
    searcher('last_name', 'Mozalev')
    u = User(base_name, "sireartem@gmail.com")
    u.get_full_name()
    u.get_short_name()
    u.__str__()
    u.get_age()