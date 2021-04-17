def pitagoras(a, b):
    c_kw = (a ** 2) + (b ** 2)
    c = c_kw ** (1/2)
    return c
    
def pole_kola(r):
    p = 3.141516 * r ** 2
    return p

print(f"Pole koła to {pole_kola(3)}.   ")
