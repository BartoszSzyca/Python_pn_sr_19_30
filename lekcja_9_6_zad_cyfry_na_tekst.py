"""Zadanie : Cyfry na Teskt

Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową, np.:

112 - > "jeden jeden dwa"
9973 -> "dziewięć dziewięć siedem trzy"

Podpowiedź:
potrzebujesz funkcji input(), słownika oraz pętli.
"""

def cyfry_na_slowa(tekst):
    slownik = {
        '0': 'zero', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery',
        '5': 'pięć', '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć'
    }
    wynik = []
    for znak in tekst:
        wynik.append(slownik.get(znak, znak))
    return " ".join(wynik)
tekst=input("podaj liczbe: ")
print(cyfry_na_slowa(tekst))