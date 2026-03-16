lista = [-6, -7, -8, -654, -4, -52, -123, -56, -4, -235, -75, -4312, -543, -34, -543]


def max(lst):
    liczba = lst[0]
    for n in lista:
        if liczba < n:
            liczba = n
    print("liczba maksymalna: ", liczba)


max(lista)

