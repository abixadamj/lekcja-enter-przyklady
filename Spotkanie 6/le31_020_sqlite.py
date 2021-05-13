import sqlite3
import os
from sys import exit

# plik bazy
database = "baza_le31.db"
table_name = "Users"
field_1 = "Username"
field_2 = "Password"

if os.path.exists(database):
    connection = sqlite3.connect(database)
else:
    print("Brak pliku!!!!")
    exit(0)

print("OK - działamy dalej")
cursor = connection.cursor()

while True:
    print("END - koniec wprowadzania.")
    login = input("Podaj login: ")
    if login == "END":
        connection.close()
        exit(0)
        
    passw = input("Podaj hasło: ")
        
    values = (login, passw)
    try:
        cursor.execute('INSERT INTO Users ("Username","Password") VALUES (?,?)', values)
        connection.commit()
        print(f"Login {login} dodany poprawnie")
    except Exception as e:
        print(f"Wystąpił błąd dodania - {e}.")
        
