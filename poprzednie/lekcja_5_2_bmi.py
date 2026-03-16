def bmi(waga, wzrost):
    wynik =  waga / wzrost ** 2
    if wynik > 25:
        print("Wysokie BMI. Otyłość")
        return wynik
    elif wynik < 18.5:
        print("Niskie BMI. Niedowaga")
        return wynik
    else:
        print("BMI w Normie.")
        return wynik


def bmi(waga, wzrost):
    wynik =  waga / wzrost ** 2
    if wynik > 25:
        print("Wysokie BMI. Otyłość")
    elif wynik < 18.5:
        print("Niskie BMI. Niedowaga")
    else:
        print("BMI w Normie.")
    return wynik

if __name__ == "__main__":
    wynik_bmi = bmi(80, 2)
    print(wynik_bmi)
    wynik_bmi = bmi(wzrost=2, waga=80)
    print(wynik_bmi)

    waga_uzytkownika = float(input("Podaj swoją wagę w kg: "))
    wzrost_uzytkownika = float(input("Podaj swój wzrost w m: "))

    print(bmi(waga_uzytkownika, wzrost_uzytkownika))