import sqlite3
from random import randint


connection = sqlite3.connect('hasla.sqlite')
cursor = connection.cursor()

# dane do login i hasło wczytamy z pliku txt

with open("kraina.txt") as plik:
    dane = plik.readlines()

dane_czyste = []
for elem in dane:
    dane_czyste.append(elem.strip())

for elem in dane_czyste[1:]:
    lista = elem.split(sep=";")
    vals = ( lista[0], lista[1] )

    try:
        cursor.execute('INSERT INTO Hasla ("Username","Password") VALUES (?,?)', vals)
        print("Udało się dodać do bazy", vals)
    except:
        print("Error -", vals)

connection.commit()
connection.close()
print("Koniec")
