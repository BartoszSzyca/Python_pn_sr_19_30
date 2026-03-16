# lista_1 = [1, 2]
# lista_2 = [4, 6]
# lista_3 = lista_1 + lista_2
# print(lista_3)

wielkosc_listy = int(input("Podaj ile cyfr całkowitych ma posiadać lista: "))
krok = 0
lista_1 = []

while wielkosc_listy != krok:
    lista_1 = lista_1 + [krok]
    print("Krok:", krok, lista_1)
    krok += 1

print(lista_1)