"""Zadanie 2 - Scrabble

 W grze Scrabble każda litera ma swoją wartość punktową.

Należy napisać program, który poprosi użytkownika o słowo i wyliczy jego wartość punktową na podstawie wartości każdej z
liter (pomijamy premie).
"""

def scrable(slowo):

    suma = 0
    punkty = {"a": 1, "b": 2, "c" :3, "d":4, "e":5}
    for i in slowo:
        suma += punkty.get(i,0)
    return suma


slowo = input("Podaj słowo: ").lower()
print(scrable(slowo))

punkty = {
    "A": 1, "E": 1, "I": 1, "N": 1, "O": 1, "R": 1, "S": 1, "W": 1, "Z": 1,
    "C": 2, "D": 2, "K": 2, "L": 2, "M": 2, "P": 2, "T": 2, "Y": 2,
    "B": 3, "G": 3, "H": 3, "J": 3, "Ł": 3, "U": 3,
    "Ą": 5, "Ę": 5, "F": 5, "Ó": 5, "Ś": 5, "Ż": 5,
    "Ć": 6,
    "Ń": 7,
    "Ź": 9
}
slowo_uzytkownika = input("Wpisz slowo: ").upper()
suma = 0
for s in slowo_uzytkownika:
    if s in punkty:
        suma += punkty[s]
print("Liczba punktów:", suma)