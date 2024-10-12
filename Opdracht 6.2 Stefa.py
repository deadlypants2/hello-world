def start_script():
    state = 0

    while True: # blijft het lopen todat er een geldig antwoord wordt gegeven
        keuze = input("Wil je naar de dierentuin?\n\n1. Ja\n2. Nee\nKies 1 of 2: ")

        if keuze == "1":
            aantal = int(input("Met hoeveel personen wilt u komen? "))
            while state < aantal:
                state += 1
                print("Veel plezier!")

            opnieuw = input("Wil je opnieuw beginnen? (ja/nee): ")
            if opnieuw.lower() == "ja":
                start_script()  # opnieuw het script starten
            else:
                print("Programma beëindigd.")
                break  # stopt loop
        elif keuze == "2":
            print("Oke doei doei")
            break  # stopt de loop
        else:
            print("Ongeldige invoer, probeer opnieuw.")  # promt verbetering

# Start the script
start_script()
