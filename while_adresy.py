hasla = [
    [1, 'beatka', 12345],
    [2, 'rrr', 12345],
    [3, 'szymon', 'erwt']
    ]

for elem in hasla:
    print(elem)

print("------------")

i = 0
dl = len(hasla)
while True:
    print(hasla[i])
    i += 1
    if i == dl:
        break
    
