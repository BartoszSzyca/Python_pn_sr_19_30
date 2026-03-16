lista_imion = ["Anna", "Bartek", "Rafał", "Łukasz", "Patrycja"]
szukane_imie = "Łukasz"

for imie in lista_imion:
    if imie == szukane_imie:
        print("Znaleziono osobe:", imie)
        print("Witaj", imie, "!")
        break
    print("Przetwarzanie listy imion:", imie)

print("Koniec pętli for")