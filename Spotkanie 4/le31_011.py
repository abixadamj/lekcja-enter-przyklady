from math import sin, radians

#for i in range(100):
#    r = radians(i)
#    # print(f" sinus z {i} = {sin(i)}")
#    print(f" sinus z {r} = {sin(r)}")

x = 0
i = 0
while x < 1:
    i = i + 1
    r = radians(i)
    x = sin(r)

print(i,r,x)

x = 0
i = 0

while True:
    i = i + 1
    r = radians(i)
    x = sin(r)
    if i > 360:
        break

print("Koniec",i,r,x)
