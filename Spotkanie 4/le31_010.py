hasla = [
    [1, 'adasiek', 12345],
    [2, 'rrr', 12345],
    [3, '33rrr', "haslo"],
    [4, 'Adam', 'erwt']
    ]
dlugosc = len(hasla)

for x in range(dlugosc):
    print(f"1 - Iteracja nr {x} -> {hasla[x]} -> {hasla[x][2]}")

print("-------")

for x in range(len(hasla)):
    print(f"2 - Iteracja nr {x} -> {hasla[x]} -> {hasla[x][2]}")

print("-------")

for elem in hasla:
    print(f"3 - Iteracja -> {elem} -> {elem[1]}")

print("--- ENUMERATE ----")

for ind , elem in enumerate(hasla):
    print(f"4 - Iteracja {ind} -> {elem} -> {elem[1]} - {hasla[ind]}")
