import sqlite3
import datetime 


with sqlite3.connect('D/IT/Github/Projects/Dictionary/database.db') as db:  # db, db3, sqlite, sqlite3
    cursor = db.cursor()
    
    # query_create = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT) """
    # cursor.execute(query_create)
    
    query1 = """ INSERT INTO expenses (id, name) VALUES(1, 'Комуналка'); """
    query2 = """ INSERT INTO expenses (name, id) VALUES('Бензин', 2); """
    query3 = """ INSERT INTO expenses VALUES(3, 'Інтернет'); """
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()




def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))


def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


insert_payments = [
    (1, 120, get_timestamp(2020, 9, 1), 1)
    (2, 12, get_timestamp(2020, 9, 1), 3)
    (3, 20, get_timestamp(2020, 9, 1), 2)
    (4, 20, get_timestamp(2020, 9, 2), 2)
    (5, 20, get_timestamp(2020, 9, 3), 2)
]


with sqlite3.connect('D/IT/Github/Projects/Dictionary/database.db') as db:  # db, db3, sqlite, sqlite3
    cursor = db.cursor()
    
    # query_create = """ CREATE TABLE IF NOT EXISTS expenses(
    #     id INTEGER,
    #     amount REAL,
    #     payment_data INTEGER,
    #     expense_id INTEGER
    # ) """
    # cursor.execute(query_create)
    
    query = """ INSERT INTO payments(id, amount, payment_date, expense_id)
                            VALUES(?,?,?,?);  """
 
    cursor.executemany(query, insert_payments)
    db.commit()
    print(cursor.rowcount, "Строк добавлено")
    
    
    
    
    
# 2) Отримання інформації з БД
with sqlite3.connect('D/IT/Github/Projects/Dictionary/database.db') as db:  # db, db3, sqlite, sqlite3
    cursor = db.cursor()

    query = """ SELECT * FROM payments """
 
    cursor.execute(query)
    suma = 0
    for res in cursor:
        suma += res[1]
        print(res)
    print('TOTAL:' ,suma)
    
    
    
    
with sqlite3.connect('D/IT/Github/Projects/Dictionary/database.db') as db:  # db, db3, sqlite, sqlite3
    cursor = db.cursor()

    query = """ SELECT amount, payment_data, name FROM payments JOIN expenses
                ON expenses.id = payments.expense_id WHERE expense_id = 2 """
 
    cursor.execute(query)
    suma = 0
    for res in cursor:
        suma += res[0]
        print(res[0], get_date(res[1]), res[2])
    print('TOTAL:' ,suma)