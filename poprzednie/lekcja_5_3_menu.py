"""
Stworzcie menu za którego omocą uzytkownik bedzie mógł wywołać funkcje:
 - bmi
 - gra_kamien_papier_nozyce
albo zakończyć działanie programu.

+========+
|  Menu  |
|  1.    |
|  2.    |
|  3.    |
|        |
+========+
"""

# import poprzednie.lekcja_4_4_gra
from lekcja_5_2_bmi import bmi # import lekcja_5_2_bmi
from poprzednie.lekcja_4_4_gra import gra_kamien_papier_nozyce

print("Wybierz opcję z poniższego menu: 2")
print(" 1. Oblicz BMI")
print(" 2. Zagraj w papier-kamień-nożyce")
print(" 3. Zakończ działanie programu")
wybor_uzytkownika = int(input("Wybierz numer opcji, którą chcesz wykonać: "))
if wybor_uzytkownika == 1:
    waga = float(input("Podaj swóją wagę w kg: "))
    wzrost = float(input("Podaj swój wzrost w m: "))
    print(bmi(waga, wzrost))
elif wybor_uzytkownika == 2:
    gra_kamien_papier_nozyce()
else:
    print("Program zakończył działanie")