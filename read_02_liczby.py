# ile liczb w pliku liczby.txt ma minimum 15 jedynek
with open("liczby.txt") as plik:
    dane = plik.readlines()

dane_czyste = []
for elem in dane:
    dane_czyste.append(elem.strip())

# ile liczb ma min. 15 jedynek
wynik = 0
for liczba in dane_czyste:
    if liczba.count("1") > 14:
        wynik += 1

print(f"W pliku jest {wynik} liczb z min. 15 jedynkami.")
