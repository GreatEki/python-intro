import sqlite3

def create_table():
    connection = sqlite3.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute(" CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL) ")

    cursor.execute(" INSERT INTO store VALUES ('Wine Glass', 8, 10.5) ")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute(" INSERT INTO store VALUES (?,?,?) ", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM store ")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute(" DELETE FROM store WHERE item=?", (item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute(" UPDATE store SET quantity=?, price=? WHERE item=? ", (quantity, price, item))
    connection.commit()
    connection.close()

# update(11, 6, 'Water Glass')
# delete('Wine Glass')
# print(view())
# insert("Coffee Cup", 10, 5)