def sortowanie_babelkowe(lista):
    dlugosc_listy = len(lista)
    print("dlugosc_listy:", dlugosc_listy)
    for index_1 in range(dlugosc_listy):
        print("index_1:", index_1)
        print("range(0, dlugosc_listy - index_1 -1):", range(0, dlugosc_listy - index_1 -1))
        for index_2 in range(0, dlugosc_listy - index_1 -1):
            print("index_2:", index_2)
            print(lista)
            if lista[index_2] > lista[index_2+1]:
                lista[index_2], lista[index_2+1] = lista[index_2+1], lista[index_2]


if __name__ == "__main__":
    lista_liczb_3 = [65, 35, 25, 10, 20, 12, 85]
    sortowanie_babelkowe(lista_liczb_3)