waga = float(input('Podaj swoją wagę w kg: '))
# waga = float(waga)
wzrost = float(input('Podaj swój wzrot w metrach:'))

bmi = waga/wzrost ** 2

if bmi <= 18.5:
    wynik = "Nie dowaga"
    # print("Nie dowaga")
elif bmi >= 25:
    wynik = "Nadwaga"
    # print("Nadwaga")
else:
    wynik = "W normie"
    # print("W normie")

print("Twoje BMI:", bmi, wynik)