"""
Stwórz funkcję przyjmującą listę liczb całkowitych, a zwracającą informację,
na której pozycji znajduje się najmniejsza liczba.

Nie korzystaj z wbudowanych funkcji.

np. dla listy [42, 13, 56, 7, 12, 3, 85] funkcja powinna zwrócić 5,
ponieważ pod tym indeksem w tej liście znajduje się element najmniejszy.
"""


def funkcja_min(lista):
    najmniejsza_liczba = lista[0]
    krok = 0
    minimalny_indeks = krok
    for liczba in lista:
        if liczba < najmniejsza_liczba:
            minimalny_indeks = krok
            najmniejsza_liczba = liczba
        krok += 1  # indeks = indeks + 1
    return minimalny_indeks


if __name__ == "__main__":
    lista_liczb = [42, 13, 56, 7, 12, 3, 85]
    lista_liczb_2 = [25, 17, 1, 7, 12, 3, 85]

    indeks_min = funkcja_min(lista_liczb)
    print("Indeks najmniejsze liczby z listy:", indeks_min)