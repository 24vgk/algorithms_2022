"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
import sqlite3


def hash_password(user_pas, users_name):
    """Хэшируем  пароль и солим его"""
    user_pas = bytes(user_pas, encoding='utf-8')
    salt = bytes(users_name, encoding='utf-8')
    res = hashlib.sha256(salt + user_pas).hexdigest()
    return res


def sql_add(user_pas, users_name):
    """Подключаемся к БД и добавляем данные"""
    try:
        con = sqlite3.connect('password.sqlite')
        with con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS PASS (
                    name TEXT UNIQUE,
                    password TEXT
                );
            """)
        sql = 'INSERT INTO PASS (name, password) values(?, ?)'
        data = (users_name, hash_password(user_pas, users_name))
        with con:
            con.execute(sql, data)
        with con:
            data = con.execute("SELECT * FROM PASS")
            for row in data:
                print(f'В базе данных хранится строка: {row}, Вы успешно зарегистрировались')
                return row
    except sqlite3.IntegrityError:
        print('Попльзователь с таким логином уже существует, пройдите Авторизацию!')


def sql_select(users_name):
    """Подключаемся к БД и выбираем данные"""
    con1 = sqlite3.connect('password.sqlite')
    sql1 = "SELECT password FROM PASS WHERE name = ?"
    data1 = (users_name,)
    with con1:
        result = con1.execute(sql1, data1)
        for row in result:
            return row[0]


if __name__ == '__main__':
    user_password = input('Введите пароль: ')
    user_name = input('Введите логин: ')
    password_add = sql_add(user_password, user_name)
    user_name_check = input('Введите логин: ')
    user_password_check = input('Введите пароль: ')
    password_check = sql_select(user_name_check)
    if hash_password(user_password_check, user_name_check) == password_check:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели Не правильный пароль')
