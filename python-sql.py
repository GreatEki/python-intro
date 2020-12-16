import mysql.connector
from difflib import get_close_matches

connection = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'test'
)

cursor = connection.cursor()

theWord =  input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression =  '%s'" % theWord)
results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else: 
    print("Sorry, word not found")

    