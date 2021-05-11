# budujemy listę znajomych na urodziny jako program z funkcjami
# kończymy wpisująć opcję 4

# typ mutable - zmienialny w miejscu - list, dict, class
lista_znajomych = []
#

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
    ### DODAJEMY DO LISTY
    lista_znajomych.append(zaproszona_osoba)
    ####
    print(lista_znajomych)

def pokaz_liste():
    if not lista_znajomych:
        print("Niestety nie masz żadnych zaproszonych gości")
    else:
        print(lista_znajomych)

while True:
    opcja = menu()
    if opcja == 1:
        dodaj_osobe()
    elif opcja == 2:
        pass
    elif opcja == 3:
        pokaz_liste()
    elif opcja == 4:
        print("OK - koniec")
        break
    else:
        print(f"Niestety, nie znam opcji {opcja}.")
