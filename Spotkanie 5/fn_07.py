def wyswietl(lista):
    if type(lista) is not list:
        return False

    for elem in lista:
        print(elem)

    el = len(lista)
    ost = lista[el-1]
    # wycinek listy - slice
    osu = lista[-1:]

    return el, ost
