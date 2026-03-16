zakres = int(input("Podaj do której liczby mam wyświelić liczby parzyste: "))
liczba = 0

while zakres != liczba:
    liczba += 1
    if liczba % 2 != 0:
        continue
    print("Liczba parzysta:", liczba)

