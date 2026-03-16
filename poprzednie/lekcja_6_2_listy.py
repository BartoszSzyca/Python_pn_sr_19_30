lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_liczb)
print(f"Watość z listy po indeksie (0): {lista_liczb[0]}")
print(f"Watość z listy po indeksie (6): {lista_liczb[6]}")
print(f"Watość z listy po indeksie (-1): {lista_liczb[-1]}")

# print(f"Watość z listy po indeksie (11): {lista_liczb[11]}")

lista_liczb[4] = "Pięć"

print(lista_liczb)
print("*" * 100)

print(lista_liczb[2:7])
print(lista_liczb[2:6:2])
print(lista_liczb[2:9:2])
print(lista_liczb[-1:-11:-1])
print(lista_liczb[::-1])
print(lista_liczb[2:])
print(lista_liczb[:-2])
print("+" * 100)
lista = ["a", "b", "c"]
dodane_listy = lista_liczb + lista
print(dodane_listy)
print(lista)
print(lista_liczb)
lista.extend(lista_liczb)
print(lista)

liata_1 = ['a', "b", "c", "d", "e"]
lista_2 = ['f', "g", "h", "i", "j"]

liata_1.extend("123")
print(liata_1)
liata_1.append(123)
print(liata_1)
liata_1.append(lista_2)
print(liata_1)
print(liata_1[5])
print(liata_1[-1][2])
print("*" * 100)
liata_1 = ['a', "b", "c", "d", "e"]
lista_2 = ['f', "g", "h", "i", "j"]
liata_1.extend(lista_2)
print(liata_1)

liata_1.pop(4)
print(liata_1)

element = liata_1.pop(-1)
print(liata_1)
print(element)

liata_1 = [0] + liata_1
print(liata_1)

del liata_1[1]
print(liata_1)

liata_1 = liata_1[:-1] + [5] + liata_1[-1:]
print(liata_1)
liata_1 = liata_1[:5] + ["Ala"] + liata_1[5:] # liata_1 = liata_1[:-5] + ["Ala"] + liata_1[-4:]

print(liata_1)



