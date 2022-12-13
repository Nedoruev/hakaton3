import sqlite3

db_users = sqlite3.connect('users.db')

cursor = db_users.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
    Логин text UNIQUE,
    Пароль text,
    Роль text
)""")


login = input('Введите логин -> ')
password = input('Введите пароль -> ')

cursor.execute(f"SELECT * FROM Users WHERE Логин = '{login}' AND Пароль = '{password}'")


try:
    checking_list = [cursor.fetchone()]
    login_check = checking_list[0][0]
    password_check = checking_list[0][1]
except:
    print('Вы ввели неверно данные аккаунта или еще не зарегестрировались')
else:
    print('Вы вошли в аккаунт')



db_users.commit()
db_users.close()
