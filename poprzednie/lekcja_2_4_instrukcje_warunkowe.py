wiek = 16

#   16>=18 => False
if wiek >= 18: # Wykona sie Tylko wtedy gdy wynik warunku bedzie True
    print("Jesteś pełnoletni")
    print("Możesz wyrobić dowód osobisty.")

print("*" * 60)
#   16>=16 => True
if wiek >= 16:
    print("Możesz wyrobić prawojazdy tymczasowe.")

print("*" * 60)
wiek = 19
#   19 >= 18 => True
if wiek >= 18:
    print("Jesteś pełnoletni")
    print("Możesz wyrobić dowód osobisty.")
elif wiek >= 16:
    print("Możesz wyrobić prawojazdy tymczasowe.")

print("Zakończenie kodu.")
