#Deze functie print de gegevens van de school uit op het moment dat deze wordt opgeroepen.

def gegevensschool():
    print("ROC Nijmegen\nTechnovium Heyendaalseweg 98\n6525 EE Nijmegen")

#hier wordt de eerdere defenitie opgeroepen die de schoolgegevens uitprint.

gegevensschool()

#Hier wordt de voor en achternaam gevraagd van de persoon die jarig is.

voornaam = input("wat is uw voornaam? ")
achternaam = input("wat is uw achternaam? ")

#Hier wordt de defentie gemaakt die happy birthday zingt.

def happybirthday(voornaam,achternaam):
    print("Happy birthday to you!\nHappy birthday to you!\nHappy birthday to", voornaam, achternaam, "\nHappy birthday to you!")

#hier wordt de functie opgeroepen en de 2 eerdere aangevraagde variabeleln worden hierbij opgegeven

happybirthday(voornaam,achternaam)

#opvragen data voor breedte en lengte.

lengte = float(input("wat is de lengte? "))
breedte = float(input("wat is breedte? "))

#Hier word de defenitie oppervlakte gemaakt.
#Dit is enkel een lengte keer breedte berekening met een print van de uitkomst

def Oppervlakte(lengte,breedte):
    oppervlakte = lengte * breedte
    print("De oppervlakte is",oppervlakte)

#Hier word de defenitie opgeroepen met de eerder aangegeven variabelen

Oppervlakte(lengte,breedte)

#hier word er naar het aantal mps gevraagd wat moet worden omgerekend.
snelheid = float(input("wat is mps? "))

#onderstaand word de ingevoerde snelheid omgerekend naar kilometers per uur.
def mps(snelheid):
    kmpu = snelheid * 3.6
    print("De snelheid is",kmpu)

#Hier word de defenitie opgeroepen met de eerder aangegeven variabelen

mps(snelheid)

