import random
print("Welkom bij het Avonturenspel!")

# Introductie
print("Je bent een avonturier op zoek naar een verborgen schat.")
print("Je begint je reis in een donker bos.")
# Variabelen
geld = 0
schatten = 0
zwaard = True
toverstok = True
leven = 100

# functie voor gevecht
def vecht_tegen_monster():
    global leven
    monster_leven = 50
    while monster_leven > 0:
        keuze = input("Wat wil je doen? (vecht, vlucht) ")
        if keuze == "vecht":
            if zwaard:
                schade = random.randint(10, 20)
                monster_leven -= schade
                print("Je veroorzaakt " + str(schade) + " schade aan het monster.")
                if monster_leven <= 0:
                    print("Je hebt het monster verslagen!")
                    return True
            else:
                print("Je hebt geen zwaard om tegen het monster te vechten.")
                return False
        elif keuze == "vlucht":
            (kans) = random.randint(1, 2)
            if kans == 1:
                print("Je ontsnapt aan het monster.")
                return False
            else:
                print("Je kon niet ontsnappen.")
                schade = random.randint(5, 10)
                leven -= schade
                print("Het monster veroorzaakt " + str(schade) + " schade aan jou.")
                if leven <= 0:
                    print("Je bent overleden.")
                    return False
                else:
                    print("Ongeldige keuze, probeer het opnieuw.")


# Loop
while True:
    if leven <= 0:
        print("Je bent overleden.")
        break


# Keuze
    keuze = input("Wat wil je doen? (ga verder, zoek schat, check inventory, vecht tegen een monster, gebruik magische voorwerp) ")
    if keuze == "ga verder":
        print("Je gaat verder door het bos.")
    elif keuze == "zoek schat":
        print("Je begint te zoeken naar een schat.")
        schatten += 1
        print("Je hebt nu " + str(schatten) + " schatten gevonden.")
    elif keuze == "check inventory":
        print("Je hebt " + str(geld) + " geld, " + str(schatten) + " schatten, " + str(zwaard) + " zwaard, " + str(toverstok) + " toverstok.")
    elif keuze == "vecht tegen een monster":
        if keuze == "vecht tegen een monster":
            if vecht_tegen_monster():
                geld += random.randint(10, 50)
                print("Je hebt " + str(geld) + " geld verdiend door het monster te verslaan.")
    elif keuze == "gebruik magisch voorwerp":
        if toverstok:
            leven += random.randint(10, 30)
            print("Je hebt je levensenergie opgevuld met de toverstok. Je huidige levensenergie is " + str(leven) + ".")
        else:
            print("Je hebt geen toverstok in je inventory.")
    else:
        print("Ongeldige keuze, probeer het opnieuw.")
    print("Bedankt voor het spelen van het Avonturenspel!")