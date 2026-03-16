print("Jakiś początkowy tekst")
print(1, 2, 3, "Ala", "ma", "kota")
print(1, 2, 3, "Ala", "ma", "kota", sep="++")
print(1, 2, 3, "Ala", "ma", "kota", end="\t")
print(1, 2, 3, "Ala", "ma", "kota")
print("Jakiś końcowy tekst".upper())
print("=" * 120)
teskt = "Kot ma Ale"
print(teskt.lower())
print(teskt)

teskt = teskt.upper()
print(teskt)

print("=" * 120)

tekst_1 = f"Ala ma kota, {teskt}. {3}"
print(tekst_1)
print(type(tekst_1))

print("To jest {} który {}.".format("tekst", "modyfikujemy"))
print("To jest {x} który {y}.".format(x="modyfikujemy", y="tekst"))
print("To jest {0} który {1}.".format("tekst", "modyfikujemy"))

print(f"Ala ma kota, {teskt}. {3}".lower())

print("To jest {x} który {x}.".format(x="tekst", y="tekst"))