moje_numery = {'policja': 997, "pizza": 467, "numer_alarmowy": 112}

print(moje_numery)
print(moje_numery["pizza"])
moje_numery['Mama'] = 123987456
print(moje_numery)
del moje_numery["pizza"]
print(moje_numery)
moje_numery['Mama'] = "656123857"
print(moje_numery)
print("+" * 70)
# print(moje_numery['mama'])
wartosc = moje_numery.get('Błędny klucz', "Domyślna wartość")
print(wartosc)
wartosc = moje_numery.get('Mama', "Domyślna wartość")
print(wartosc)
print("+" * 70)
print(list(moje_numery.keys()))
print(list(moje_numery.values()))
print(list(moje_numery.items()))
print("+" * 70)
for klucz in moje_numery:
    print(klucz)

print("klucz" in moje_numery)

for wartosc in moje_numery.values():
    print(wartosc)

for klucz, wartosc in moje_numery.items():
    print(klucz, wartosc)
