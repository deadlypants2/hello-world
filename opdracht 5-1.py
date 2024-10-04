#de vraag wat u wilt bestellen
bestelling = str(input("wat zou u willen drinken? \n1. Bier\n2. Fris\n3. Wijn\n4. Mineraalwater\n"))
#de berekening van invoer naar een string zodat alles gelijk is met foutcode.
if bestelling.lower() == "1" or bestelling.lower() == "bier":
    bestellingstr = "bier"
elif bestelling.lower() == "2" or bestelling.lower() == "fris":
    bestellingstr = "fris"
elif bestelling.lower() == "3" or bestelling.lower() == "wijn":
    bestellingstr = "wijn"
elif bestelling.lower() == "4" or bestelling.lower() == "mineraalwater":
    bestellingstr = "mineraalwater"
else:
    print("voer een geldig item in")
    bestellingstr = ""
#hierbij word gecontroleerd of er een alcohollitisch drankje word besteld. Is dit het geval dan word de leeftijd gevraagd waarna de bestelling word uitgeprint.
if bestellingstr == "fris" or bestellingstr == "mineraalwater": print("uw", bestellingstr, "komt eraan")
elif bestellingstr == "bier" or bestellingstr == "wijn":
    leeftijd = int(input("wat is uw leeftijd? "));
    if leeftijd >= 18: print("Uw", bestellingstr, "komt eraan")
    elif leeftijd <= 17: print("u bent te jong om deze bestelling te plaatsen")


