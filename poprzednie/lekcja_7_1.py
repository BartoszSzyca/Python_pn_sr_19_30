from lekcja_6_4_zad import funkcja_min

lista_liczb_3 = [5, 17, -5, 7, 12, 32, 17]

print(f"Indeks liczby_min z funkcji: {funkcja_min(lista_liczb_3)}")
print(f"Indeks z liczby -5 z metody: {lista_liczb_3.index(-5)}")
print(f"Indeks liczby_min z funkcji min: {lista_liczb_3.index(min(lista_liczb_3))}")
print("*" * 120)
print(range(10))
lista_liczby_range = list(range(10))
print(lista_liczby_range)

print(list(range(5,12)))