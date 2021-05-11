# budujemy listę znajomych na urodziny jako program z funkcjami
# kończymy wpisująć opcję 4

lista_znajomych = []

def menu():
    menu_str = """MENU:
==============
1 - Dodaj osobę do listy.
2 - Szukaj osoby w liście.
3 - Wypisz całą listę.
4 - KONIEC"""
    print(menu_str)
    wybor = int(input("Podaj nr opcji :"))
    return wybor

def plec(zaproszona_osoba):
    if zaproszona_osoba[-1:] == "a":
        return f"{zaproszona_osoba} to kobieta."
    else:
        return f"{zaproszona_osoba} to mężczyzna."
    
    
def dodaj_osobe():
    zaproszona_osoba = input("Podaj imię zapraszanej osoby: ")
    print(plec(zaproszona_osoba))


while True:
    opcja = menu()
    if opcja == 1:
        dodaj_osobe()
    elif opcja == 2:
        pass
    elif opcja == 3:
        pass
    elif opcja == 4:
        print("OK - koniec")
        break
    else:
        print(f"Niestety, nie znam opcji {opcja}.")
