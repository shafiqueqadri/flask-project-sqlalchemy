import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY , username text, password text)"
cursor.execute(create_users)

create_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY , name text, price int)"
cursor.execute(create_items)

connection.commit()
connection.close()