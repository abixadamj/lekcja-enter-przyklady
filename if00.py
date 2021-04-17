# Tutaj pisz swój kod, młody padawanie ;-)
print("Hej")
liczba = input("Podaj liczbę: ")

if liczba.replace('.', '', 1).isdigit():
    print("OK, liczba poprawna")
    print(f"Typ to: {type(liczba)}.")

print(f"Wartość to: {liczba}")
