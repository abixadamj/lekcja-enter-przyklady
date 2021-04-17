# ile liczb w pliku liczby.txt ma minimum 15 jedynek
with open("kraina.txt") as plik:
    dane = plik.readlines()

dane_czyste = []
for elem in dane:
    dane_czyste.append(elem.strip())

slownik = {}
for elem in dane_czyste[1:]:
    # elem => w50B;2494207;2625207;1796293;1853602
    # lista => ['w50B', '2494207', '2625207', '1796293', '1853602']
    lista = elem.split(sep=";")
    # budowa elementu słownika - klucz to indeks 0 listy
    # generator listowy do zbudowania wartości
    # l1[1:] => ['2494207', '2625207', '1796293', '1853602']
    # int(x) for x in l1[1:] ] => [2494207, 2625207, 1796293, 1853602]
    slownik[lista[0]] = [ int(x) for x in lista[1:] ]

print("które z państw ma największą liczbę mieszkańców?")
mieszkancy = 0
panstwo = None

for elem in slownik:
    # slownik["w50B"] => [2494207, 2625207, 1796293, 1853602]
    # slownik["w50B"][0] => 2494207
    if slownik[elem][0] > mieszkancy:
        panstwo = elem
        mieszkancy = slownik[elem][0]

print(f"Państwo {panstwo} ma max. mieszkańców {mieszkancy}")
    
