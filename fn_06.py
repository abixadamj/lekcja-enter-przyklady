def pitagoras(a:float, b:float) -> float:
    """Funkcja oblicza dł. przeciwprostokątnej"""
    c_kw = (a ** 2) + (b ** 2)
    c = c_kw ** (1/2)
    return c
    
def pole_kola(r):
    p = 3.141516 * r ** 2
    return p

def sila(r, m1, m2, g=6.67E-11):
    return g*m1*m2 / (r**2)

def sila_2(r=2, m2=4, g=6.67E-11, m1=150):
    return g*m1*m2 / (r**2)
