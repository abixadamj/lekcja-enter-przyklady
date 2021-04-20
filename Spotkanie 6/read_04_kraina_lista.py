# ile liczb w pliku liczby.txt ma minimum 15 jedynek
with open("kraina.txt") as plik:
    dane = plik.readlines()

dane_czyste = []
for elem in dane:
    dane_czyste.append(elem.strip())

print("które z państw ma największą liczbę mieszkańców?")
mieszkancy = 0
panstwo = None

for elem in dane_czyste[1:]:
    # elem => w50B;2494207;2625207;1796293;1853602
    # lista => ['w50B', '2494207', '2625207', '1796293', '1853602']
    lista = elem.split(sep=";")
    if int(lista[1]) > mieszkancy:
        panstwo = lista[0]
        mieszkancy = int(lista[1])

print(f"Państwo {panstwo} ma max. mieszkańców {mieszkancy}")
    
