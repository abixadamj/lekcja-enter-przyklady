# program całościowy dla haseł i bazy SQLite
import sqlite3
from Crypto.Hash import HMAC, SHA256

def get_password(login):
    connection = sqlite3.connect('hasla.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Hasla where Username=:name",{"name": login})
        wynik = cursor.fetchall()
        if wynik:
            retval = wynik[0][2]
        else:
            retval = False
    except:
        retval = False

    connection.commit()
    connection.close()
    return retval


def set_password(login, digest):
    connection = sqlite3.connect('hasla.sqlite')
    cursor = connection.cursor()
    vals = (login, digest)
    try:
        cursor.execute('INSERT INTO Hasla ("Username","Password") VALUES (?,?)', vals)
        retval = True
    except:
        retval = False

    connection.commit()
    connection.close()
    return retval

def szyfruj():
    haslo = input("Podaj hasło:")
    bhaslo = str.encode(haslo)
    h = HMAC.new(bhaslo, digestmod=SHA256)
    dg = h.hexdigest()
    return dg


# pętla główna programu
login = input("Podaj swój login: ")
haslo = szyfruj()

d = get_password(login)
if not d:
    print("Błędny login!")

if haslo == d:
    print(f"Hello! Witaj {login} w aplikacji!")
else:
    print(f"Niestety, złe hasło dla {login} - Error!")
