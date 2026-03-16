lista_1 = [1, 2, 3, 4, 5]
zmienna_1 = 12
zmienna_2 = zmienna_1
print(f"zmienna_2: {zmienna_2}\nzmienna_1: {zmienna_1}")
zmienna_1 = 1
print(f"zmienna_2: {zmienna_2}\nzmienna_1: {zmienna_1}")
print("*" * 50)

lista_2 = lista_1
lista_3 = lista_1.copy()
lista_4 = lista_1[:]
print(f"lista_2: {lista_2}\nlista_1: {lista_1}\nlista_3: {lista_3}\nlista_4: {lista_4}")
lista_1[0] = 6
print(f"lista_2: {lista_2}\nlista_1: {lista_1}\nlista_3: {lista_3}\nlista_4: {lista_4}")
print("*" * 50)

zbior_1 = {1, 2, 3, 4}
print("zbior_1:", zbior_1)
zbior_2 = {4, 1, 2, 3, 4, 3, 4, 2, 3}
print("zbior_2:", zbior_2)
lista = [4, 1, 2, 3, 4, 3, 4, 2, 3]
lista = list(set(lista))
print(lista)
lista.append(6)
print(lista)
print("*" * 50)
print("zbior_1:", zbior_1)
zbior_1.add(5)
zbior_1.add(5)
print("zbior_1:", zbior_1)
zbior_3 = {5, 6, 7}
zbior_1.update(zbior_3)
print("zbior_1:", zbior_1)

lista = []
print(lista)

# zbior = {}
zbior = set()
print(type(zbior))