"""Zadanie 1 - Izogram
Stwórzcie program izogram który prosi użytkownika o podanie słowa
i napisze czy dane słowo jest izogramem lub nie.

Izogram jest sołowem , w którym żadna litera sie nie powtarza.

Przykład: Skrzynia
"""
def czy_izogram(slowo):
    slowo = slowo.lower()
    return len(set(slowo)) == len(slowo)


if __name__ == "__main__":
    slowo = input("podaj slowo:")
    print(czy_izogram(slowo))
    print("*" * 50)

    while True:
        slowo_uzytkownika = input("Podaj słowo: ")
        odpowiedz = 'jest' if czy_izogram(slowo_uzytkownika) else "nie jest"
        print(f"Słowo '{slowo_uzytkownika}' {odpowiedz} izogramem\n")
        czy_kontynuowac = input("Czy chcesz kontyuować? (T/N): ")
        if czy_kontynuowac.lower() != 't':
            break