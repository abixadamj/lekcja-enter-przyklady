hasla = [
    [1, 'adasiek', 12345],
    [2, 'rrr', 12345],
    [3, 'Adam', 'erwt']
    ]

szukany = input("Podaj szukany login: ")

for element in hasla:
    print(f"Wartość {element}")
    if element[1] == szukany:
        print("Znalazłem szukany login!")
    elif szukany in element[1]:
        print("Ale jest podobny do tego....")
    else:
        print("Niestety nijak nie pasuje")

