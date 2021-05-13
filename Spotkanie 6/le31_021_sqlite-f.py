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
    print(f"Brak pliku - {database} !!!!")
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
        cursor.execute(f'INSERT INTO Users ({field_1},{field_2}) VALUES (?,?)', values)
        connection.commit()
        print(f"Login {login} dodany poprawnie")
    except Exception as e:
        print(f"Wystąpił błąd dodania - {e}.")
        
#### [ WYNIK DZIAŁANIA] #########
# =============== RESTART: /home/adasiek/le31/le31_021_sqlite-f.py ===============
# OK - działamy dalej
# END - koniec wprowadzania.
# Podaj login: adasiek
# Podaj hasło: sfd
# Wystąpił błąd dodania - UNIQUE constraint failed: Users.Username.
# END - koniec wprowadzania.
# Podaj login: adasiek3456
# Podaj hasło: dsfasd
# Login adasiek3456 dodany poprawnie
# END - koniec wprowadzania.
# Podaj login: END
