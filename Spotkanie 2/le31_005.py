imie = input("Podaj mi swoje imię: ")
nazwisko = "Jurkiewicz"
urodzony = int(input("Podaj swój rok urodzenia: "))
print(type(urodzony))
wiek = 2021 - urodzony
print(imie,nazwisko,"urodził się w roku",urodzony)
# F-string
print(f"{imie} {nazwisko} urodził się w roku {urodzony} i ma {wiek} lat")
