import sqlite3
connection = sqlite3.connect('hasla.sqlite')
cursor = connection.cursor()
vals = ("abc122x3", 45332434)

try:
    cursor.execute('INSERT INTO Hasla ("Username","Password") VALUES (?,?)', vals)
    print("Udało się dodać do bazy")
except:
    print("Error ;-)")

connection.commit()
connection.close()
print("Koniec")
