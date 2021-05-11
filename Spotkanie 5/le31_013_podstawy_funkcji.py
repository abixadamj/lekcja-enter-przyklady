def pierwsza():
    """Tutaj będzie nasz opis"""
    imie = input("Podaj swoje imię: ")
    print(f"Cześć {imie} - tu Python.")

def druga(powitanie):
    """Witam się z userem
powitanie - string do wypisania"""
    imie = input("Podaj swoje imię: ")
    print(f"Cześć {imie} - tu {powitanie}.")
#############################################

def miejsca_w_samolocie(rz1, rz2):
    """obliczamy ilość miejsc w samolocie"""
    ile_miejsc = rz1 * 2 + rz2 * 4
    print(f"Nasz samolot dla {rz1} 1kl i {rz2} 2 kl ma {ile_miejsc} miejsc dla pasażerów.")

def miejsca_w_samolocie_2(rz1, rz2):
    """obliczamy ilość miejsc w samolocie"""
    ile_miejsc = rz1 * 2 + rz2 * 4
    return ile_miejsc

def cena_biletu(wartosc, miejsc):
    """cena biletu dla liczby miejsc"""
    return round(wartosc/miejsc, 2)
