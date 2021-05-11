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


while True:
    opcja = menu()
    if opcja == 1:
        pass
    elif opcja == 2:
        pass
    elif opcja == 3:
        pass
    elif opcja == 4:
        print("OK - koniec")
        break
    else:
        print(f"Niestety, nie znam opcji {opcja}.")
