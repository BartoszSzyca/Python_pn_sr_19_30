stary_slownik = {'policja': 997, "pizza": 467, "numer_alarmowy": 112}

nowy_slownik = {v: k for k, v in stary_slownik.items()}

print(nowy_slownik)

lista_slow = ['ala', 'ola', 'alek', 'mirek', 'ela']

dlugosc_slow = {len(slowo) for slowo in lista_slow}

print(dlugosc_slow)