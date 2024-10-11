# Ik defineer de stand naar 0
state = 0
# Geef de klanten een keuze tussen 2 opties
def start_vraag():
    keuze = input("wil je naar de dierentuin ?\n\n1.Ja\n2.Nee\nKies 1 of 2")

# Voor keuze 1 word per persoon veel plezier geprint

if keuze == "1":
    aantal = int(input("met hoeveel personen wilt u komen?"))
    while state < aantal:
        state +=1
        print("Veel plezier!")

# Keuze 2 eindigd met een bericht

elif keuze == "2":
    print("Oke doei doei")

else:
    print("Ongeldige invoer")
    start_vraag()


