#lengte = input("Hoe lang is je zwembad? (in meters")
#breedte = input("Hoe breed is je zwembad? (in meters")
#diepte = input("Hoe diep is je zwembad? (in meters")
#inhoud = lengte * breedte * diepte
#print("Jouw zwembad heeft als hij helemaal vol is", inhoud, "m3 water")

#de juiste code is:

#lengte = float(input("Hoe lang is je zwembad? (in meters"))
#breedte = float(input("Hoe breed is je zwembad? (in meters"))
#diepte = float(input("Hoe diep is je zwembad? (in meters"))
#inhoud = lengte * breedte * diepte
#print("Jouw zwembad heeft als hij helemaal vol is", inhoud, "m3 water")


#foute code:

#naam = input("Wat is je voornaam? ")
#lengte = int(input("Hoe lang ben je ? (in meters)"))
#print("Hallo", naam, "je bent", lengte, "meters")

#de int moet een float zijn. Goede code:

#naam = input("Wat is je voornaam? ")
#lengte = float(input("Hoe lang ben je ? (in meters)"))
#print("Hallo", naam, "je bent", lengte, "meters")

#hierbij kanabaliseer ik de vorig opdracht:

#vraag de aantal GPU's op aan de gebruiker en zet de int variablele op nul zodat deze gedifineerd is.
aantalint = int(0)
aantal = str(input("Hoeveel videokaarten zijn besteld?\n"))

#controleer of er een goed getal is ingevuld.

if aantal.isdigit():
    aantalint = int(aantal)

#print de levertijd en geef aan waneer er geen GPU besteld is.
if aantalint > 0:
    if aantalint < 10: print("De levertijd van uw bestelling bevat 3 dagen.")
    elif 10 <= aantalint < 20: print("De levertijd van uw bestelling bevat 1 week.")
    elif 21 <= aantalint < 50: print("De levertijd van uw bestelling bevat 2 weken.")
    elif aantalint >= 50: print("Neem a.u.b. contact op met Nvidia voor uw bestelling.")
else:
    print("Voer het juiste aantal in a.u.b.")


