"""Zadanie 1

Wydrukuj liczby wypełnione gwiazdkami. Zaimplementuj okno dialogowe z użytkownikiem za pomocą menu.

a)
* * * * *
  * * * *
    * * *
      * *
        *
"""
print("""
* * * * *
  * * * *
    * * *
      * *
        *
        """)
"""
b)
*
* *
* * *
* * * *
* * * * *
"""
rozmiar = 5
krok = 1
symbol = "* "
while krok <= rozmiar:
    print(symbol * krok)
    krok += 1

"""
f)
*       *
* *   * *
* * * * *
* *   * *
*       *
"""
