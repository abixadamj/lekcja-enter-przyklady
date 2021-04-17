hasla = [
    [1, 'adasiek', 12345],
    [2, 'rrr', 12345],
    [3, 'Adam', 'erwt']
    ]
dl = len(hasla)
szukany = input("Podaj szukany login: ")

for i in range(dl):
    print(f"Wartość {i} to {hasla[i]}")
    if hasla[i][1] == szukany:
        print("Znalazłem szukany login!")
    elif szukany in hasla[i][1]:
        print("Ale jest podobny do tego....")
    else:
        print("Niestety nijak nie pasuje")
