import sqlite3
import datetime

db_campus_1 = sqlite3.connect('campus_1.db')

cursor = db_campus_1.cursor()

# создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS Комната_1 (
    Фамилия text,
    Имя text,
    Факультет text,
    Специальность text,
    Группа text,
    Ремонт text,
    Дата_последнего_ремонта text
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Комната_2 (
    Фамилия text,
    Имя text,
    Факультет text,
    Специальность text,
    Группа text,
    Ремонт text,
    Дата_последнего_ремонта text
)""")

'''
# создание таблиц в цикле (таким же способом можно реализовать заполнение, поиск и обновление данных по всем таблицам и по всем бд сразу)
for i in range(7):
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS Комната_{i+1} (
        Фамилия text,
        Имя text,
        Факультет text,
        Специальность text,
        Группа text,
        Ремонт text,
        Дата_последнего_ремонта text
    )""")
'''



# заполнение полей
cursor.execute("INSERT INTO Комната_1 VALUES('Рамазанов', 'Рамин', 'ФПМ', '121', 'ПЗ-22-3', 'Ремонт сделан', '2021-11-5')")
cursor.execute("INSERT INTO Комната_1 VALUES('Макаров', 'Сергей', 'ФПМ', '124', 'ФП-22у-2', 'Ремонт сделан', '2015-1-26')")
cursor.execute("INSERT INTO Комната_1 VALUES('Соболева', 'Ксения', 'ФПМ', '121', 'ФП-22-3', 'Ремонт сделан', '1999-8-17')")
cursor.execute("INSERT INTO Комната_1 VALUES('Монгол', 'Олег', 'ФПМ', '113', 'ПТ-22у-1', 'Ремонт сделан', '2021-9-16')")
cursor.execute("INSERT INTO Комната_2 VALUES('Иванов', 'Иван', 'ФПМ', '113', 'ПТ-22-1', 'Ремонт сделан', '2021-7-30')")

'''
# получение количесвтва людей в комнате
cursor.execute("SELECT Count() FROM Комната_1")
numberOfRows = cursor.fetchone()[0]
print(numberOfRows)



# проверка на свободные места в комнате
if numberOfRows < 4:
    cursor.execute("INSERT INTO Комната_1 VALUES('Чёрный', 'Негр', 'ФПМ', '123', 'ПЗ-22-1')")
else:
    print('Комната полностью занята')


print(cursor.fetchall())
'''

# поиск по фамилии, по аналогии по другим параметрам (можно со все кроме даты потому, что ее придется форматировать в дату для удобства.
# просто вместо *, фамилия и остальных параметров поиска вставить переменную, изменяемые данные)
# search = input('Введите фамилию для поиска по фамилии -> ')
# cursor.execute(f"SELECT * FROM Комната_1 WHERE Фамилия LIKE '%{search}%'")
# print(cursor.fetchall())





db_campus_1.commit()
db_campus_1.close()
