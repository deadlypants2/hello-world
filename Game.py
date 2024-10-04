import random

# Speler attributen
player_health = 100
player_attack = 10
inventory = []


# Functie om een willekeurige vijand te genereren
def generate_enemy():
    enemies = {
        "Goblin": {"health": 30, "attack": 5},
        "Tovenaar": {"health": 40, "attack": 8},
        "Troll": {"health": 50, "attack": 12}
    }
    enemy_name = random.choice(list(enemies.keys()))
    return enemy_name, enemies[enemy_name]


# Functie om de speler een wapen of potion te laten vinden
def find_item():
    items = ["zwaard", "schild", "potion", "sleutel"]
    found_item = random.choice(items)
    print(f"\nJe hebt een {found_item} gevonden!")
    inventory.append(found_item)

    if found_item == "zwaard":
        print("Je aanvalskracht is verhoogd!")
    elif found_item == "schild":
        print("Je verdediging is verbeterd!")
    elif found_item == "potion":
        print("Je hebt een potion die je later kunt gebruiken om je gezondheid te herstellen.")
    elif found_item == "sleutel":
        print("Je hebt een mysterieuze sleutel gevonden. Wie weet welke deur deze opent?")


# Functie voor gevecht
def fight(enemy_name, enemy_stats):
    global player_health
    print(f"\nJe komt een {enemy_name} tegen! Klaar voor de strijd!")

    while enemy_stats['health'] > 0 and player_health > 0:
        print(f"\n{enemy_name} HP: {enemy_stats['health']}")
        print(f"Jouw HP: {player_health}")

        action = input("Kies een actie: [A]anvallen, [V]luchten, [I]nventaris bekijken: ").lower()

        if action == 'a':
            # Speler valt aan
            damage = random.randint(5, player_attack)
            print(f"Je valt de {enemy_name} aan en doet {damage} schade!")
            enemy_stats['health'] -= damage
        elif action == 'v':
            # Kans om te vluchten
            if random.random() < 0.5:
                print(f"Je ontsnapt van de {enemy_name}!")
                return False
            else:
                print(f"De {enemy_name} blokkeert je vlucht!")
        elif action == 'i':
            # Speler bekijkt inventaris
            print(f"\nJouw inventaris: {inventory}")
            if "potion" in inventory:
                use_potion = input("Wil je een potion gebruiken? (ja/nee): ").lower()
                if use_potion == "ja":
                    print("Je gebruikt een potion en herstelt 20 HP!")
                    player_health += 20
                    inventory.remove("potion")
            continue
        else:
            print("Ongeldige keuze, probeer opnieuw.")
            continue

        # Vijand valt aan
        if enemy_stats['health'] > 0:
            damage = random.randint(1, enemy_stats['attack'])
            print(f"De {enemy_name} valt aan en doet {damage} schade!")
            player_health -= damage

        if player_health <= 0:
            print("Je bent verslagen... GAME OVER")
            return True

    print(f"Je hebt de {enemy_name} verslagen!")
    return False

#1Linkerpad
def linkerpad():
    print("\nJe hebt het linkerpad gekozen. Het pad is kronkelig en gevuld met spinnenwebben. Na enkele minuten bereik je een kruispunt.")
    print("1. Neem de trap naar beneden")
    print("2. Ga rechtdoor")
    choice = input("Wat wil je doen? Kies 1 of 2: ")

    if choice == "1":
        print("\nJe daalt de trap af, het wordt kouder en donkerder.")
        print("Op de bodem van de trap zie je een mysterieuze deur.")
        if "sleutel" in inventory:
            print("De deur opent met de sleutel die je eerder hebt gevonden. Je betreedt een kamer vol magische artefacten.")
            print("Plotseling verschijnt een oude magiër voor je. 'Alleen de waardige mag de schat nemen,' zegt hij.")
            if fight("Tovenaar", {"health": 40, "attack": 8}):
                return
            print("\nJe verslaat de tovenaar en vindt een legendarisch zwaard. Je aanvalskracht is permanent verhoogd!\n\nGEFELICITEERD!")
        else:
            print("De deur is op slot, en je hebt geen sleutel om hem te openen.")
            print("Je besluit terug te keren naar het kruispunt.")
            return start_kruispunt()  # Stuur de speler terug naar het kruispunt
    elif choice == "2":
        print("\nJe gaat rechtdoor en merkt een kist op. Wanneer je hem opent, springt een goblin naar voren!")
        if fight("Goblin", {"health": 30, "attack": 5}):
            return
        print("Na het verslaan van de goblin vind je een potion in de kist.")
        find_item()
    else:
        print("Ongeldige keuze, probeer opnieuw.")
        linkerpad()

# Nieuwe functie voor het kruispunt
def start_kruispunt():
    print("\nJe bent terug bij het kruispunt.")
    print("1. Neem het linkerpad")
    print("2. Ga het middelste pad in")
    print("3. Neem het rechterpad")
    choice = input("Welke gang besluit je in te gaan? Kies 1, 2 of 3: ")

    if choice == "1":
        linkerpad()
    elif choice == "2":
        middelste_pad()
    elif choice == "3":
        rechterpad()
    else:
        print("Ongeldige keuze, probeer opnieuw.")
        start_kruispunt()

    print(
        "\nJe hebt het linkerpad gekozen. Het pad is kronkelig en gevuld met spinnenwebben. Na enkele minuten bereik je een kruispunt.")
    print("1. Neem de trap naar beneden")
    print("2. Ga rechtdoor")
    choice = input("Wat wil je doen? Kies 1 of 2: ")

    if choice == "1":
        print("\nJe daalt de trap af, het wordt kouder en donkerder.")
        print("Op de bodem van de trap zie je een mysterieuze deur.")
        if "sleutel" in inventory:
            print(
                "De deur opent met de sleutel die je eerder hebt gevonden. Je betreedt een kamer vol magische artefacten.")
            print("Plotseling verschijnt een oude magiër voor je. 'Alleen de waardige mag de schat nemen,' zegt hij.")
            if fight("Tovenaar", {"health": 40, "attack": 8}):
                return
            print(
                "\nJe verslaat de tovenaar en vindt een legendarisch zwaard. Je aanvalskracht is permanent verhoogd!\n\nGEFELICITEERD!")
        else:
            print("De deur is op slot, en je hebt geen sleutel om hem te openen. Je besluit om terug te keren.")
    elif choice == "2":
        print("\nJe gaat rechtdoor en merkt een kist op. Wanneer je hem opent, springt een goblin naar voren!")
        if fight("Goblin", {"health": 30, "attack": 5}):
            return
        print("Na het verslaan van de goblin vind je een potion in de kist.")
        find_item()
    else:
        print("Ongeldige keuze, probeer opnieuw.")
        linkerpad()


# Rechterpad met vijanden en items
def rechterpad():
    print(
        "\nJe hebt het rechterpad gekozen. Het is smal en de lucht wordt zwaar. Je hoort vreemde geluiden in de verte.")
    print("1. Loop snel verder")
    print("2. Draai om en ga terug")
    choice = input("Wat wil je doen? Kies 1 of 2: ")

    if choice == "1":
        print("\nJe besluit om snel verder te lopen...")
        if random.random() < 0.5:
            print("\nEen troll komt uit de schaduwen en valt je aan!")
            if fight("Troll", {"health": 50, "attack": 12}):
                return
        else:
            print("\nJe vindt een oude kist, verborgen onder een steen. Wat zou erin zitten?")
            find_item()
    elif choice == "2":
        print(
            "\nJe besluit om terug te keren naar de tunnel ingang, maar het pad is afgesloten...\n\nJe zit vast en er is geen uitweg.\n\n\nGAME OVER")
    else:
        print("Ongeldige keuze, probeer opnieuw.")
        rechterpad()


# Middelste pad met een val
def middelste_pad():
    print(
        "\nJe besluit het middelste pad in te gaan. Het is zo donker dat je de grond niet eens kunt zien.\nPlotseling voel je de grond onder je verdwijnen!")
    print("\nJe valt in een diepe kuil gevuld met scherpe stenen.\n\nJe hebt het niet overleefd...\n\nGAME OVER")


# Start het spel met introductie en verhaal
def start_game():
    print(
        "Welkom in de Vervloekte Kerker. Jouw missie is om een oud artefact te vinden dat diep in de kerker verborgen ligt.")
    print(
        "De legende zegt dat degenen die het vinden, rijkdom en macht zullen ontvangen. Maar de weg ernaartoe zit vol gevaren.")
    print("\nJe staat aan de ingang van de kerker en ziet drie donkere gangen voor je:")
    print("1. Linkerpad")
    print("2. Middelste pad")
    print("3. Rechterpad")
    choice = input("Welke gang besluit je in te gaan? Kies 1, 2 of 3: ")

    if choice == "1":
        linkerpad()
    elif choice == "2":
        middelste_pad()
    elif choice == "3":
        rechterpad()
    else:
        print("Ongeldige keuze, probeer opnieuw.")
        start_game()


# Start het spel
start_game()
