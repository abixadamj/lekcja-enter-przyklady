# Dane są liczby w formacie 01. Podaj, jaka liczba ma największą ilość cyfr 1
# i w którym wierszu w pliku się znajduje.

with open("liczby.txt", mode="r") as pl:
    dane = pl.readlines()

# print(dane) - to lista
max_liczba = ""
max_jedynek = 0
nr_wiersza = 0

for ind, liczba in enumerate(dane):
    liczba_czysta = liczba.strip()
    if liczba_czysta.count('1') > max_jedynek:
        max_liczba = liczba_czysta
        max_jedynek = liczba_czysta.count('1')
        nr_wiersza = ind

print(f"Najwięcej znaków 1 (Ilość={max_jedynek}) jest w liczbie {max_liczba}, w wierszu o numerze {nr_wiersza+1}")
