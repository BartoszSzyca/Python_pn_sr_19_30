stara_lista = [1, 2, 3, 4, 5, 6, 7]

nowa_lista = [x ** 2 for x in stara_lista if not x % 2]

print(nowa_lista)

nowa_lista2 = []

for x in stara_lista:
    if not x % 2:
        nowa_lista2.append(x ** 2)
print(nowa_lista2)