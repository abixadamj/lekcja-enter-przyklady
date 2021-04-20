birth = int(input("Podaj rok urodzenia: "))
age = 2021 - birth
if age % 2 == 0:
    print("Twój wiek jest parzysty.")
else:
    print("twój wiek jest nieparzysty.")

if age > 60:
    print("Możesz się szczepić Pfizerem.")
elif age > 70:
    print("Astra jest dla ciebie")
elif age > 18:
    print("W ogóle to Sputnik 8")
else:
    print(f"Jeszcze {18-age} lat do szczepienia")

print(f"Masz {age} lat.")





