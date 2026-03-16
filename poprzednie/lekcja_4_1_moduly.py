# import random
#
# liczba_1 = random.randint(1, 10)
# print(liczba_1)

from random import randint, choice

liczba_2 = randint(1, 10)
print(liczba_2)
print("*"*100)

lista_1 = ["kamien", "nozyce", "papier"]
print(choice(lista_1))
print("*"*100)
import poprzednie.lekcja_2_1_typy_danych
print("*"*100)
import poprzednie.lekcja_2_2_funkcja_input
print("*"*100)

print("Nazwa pliku z którego jest uruchammiany", __name__) # Jeżeli plik w ktorym napisane zwróci __main__
if __name__ == "__main__": # Kod w ciele warunku zostanie uruchomiony tylko w tym pliku
    print("Kod który wykona sie tylko w pliku (lekcja_4_1_moduly.py)")
