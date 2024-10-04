#vraag de prijs op aan de gebruiker
prijs = float(input("Wat is de totaal prijs van uw bestelling?\n"))

#bereken de korting op basis van het aankoopbedrag
prijs5 = prijs * 0.95
prijs8 = prijs * 0.92
prijs10 = prijs * 0.90

#print de berekende prijs uit
if prijs <= 40: print("uw prijs is €", prijs)
elif prijs >= 40 and prijs < 70: print("uw prijs is €", prijs5)
elif prijs >= 70 and prijs < 100: print("uw prijs is €", prijs8)
elif prijs >= 100: print("uw prijs is €", prijs10)

