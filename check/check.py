import sqlite3

#Connect to the database (replace 'your_database.db' with your actual database file)


connetion = sqlite3.connect('mydatabase.db')
cursor = connetion.cursor()
print(cursor.execute(f'''
                               SELECT*FROM credentials;
                         ''').fetchall())


