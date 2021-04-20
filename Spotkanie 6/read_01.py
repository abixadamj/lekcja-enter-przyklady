with open("dane.txt") as plik:
    dane = plik.readlines()

dane_czyste = []
for elem in dane:
    dane_czyste.append(elem.strip())
