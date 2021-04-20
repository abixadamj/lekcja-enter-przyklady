import sqlite3
from random import randint


connection = sqlite3.connect('hasla.sqlite')
cursor = connection.cursor()
vals = ("login_"+str(randint(1,500)), randint(100,1000) )

try:
    cursor.execute('INSERT INTO Hasla ("Username","Password") VALUES (?,?)', vals)
    print("Udało się dodać do bazy", vals)
except:
    print("Error ;-)")

connection.commit()
connection.close()
print("Koniec")
