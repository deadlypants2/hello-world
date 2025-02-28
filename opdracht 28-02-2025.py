#Hierbij word de adresgegevens gevraagd van de klant en daarna opnieuw uitgeprint.
def adresgegevens():
    voornaam = input("wat is uw voornaam? ")
    achternaam = input("wat is uw achternaam? ")
    adres = input("wat is uw adres? ")
    postcode = input("wat is uw postcode? ")
    woonplaats = input("wat is uw woonplaats? ")
    print(voornaam, achternaam)
    print(adres)
    print(postcode)
    print(woonplaats)

adresgegevens()

#Hierbij worden de dimensies van de balk opvraagt en daarna berkent naar de inhoud.
#Deze wordt daarna uitgeprint.

def inhoud():
    lengte = float(input("wat is de lengte? "))
    breedte = float(input("wat is de breedte? "))
    hoogte = float(input("wat is de hoogte? "))
    floatinhoud = lengte * breedte * hoogte
    print("de inhoud is", floatinhoud)

inhoud()

#De rechthoek word berekend door de functie die 2 variabelen als invoer nodig heeft.
#wanner de deze vanuit externe variabelen toevoegt dan word de oppervlakte berekent en dit word hierna uitgeprint.

lengte = float(15)
breedte = float(15)

def rechthoek(lengte, breedte):
    oppervlakte = lengte * breedte
    print("de rechthoek is", oppervlakte,"m²")

rechthoek(lengte, breedte)

#Een willekeurige lijst word aangemaakt waarna deze van hoog na laag gesorteerd word.
#Hierna word het eerste getal van de lijst uitgeprint.

import random

n = 50  # Aantal willekeuringe nummers
my_list = random.sample(range(1, 101), n)
my_list.sort(reverse=True)
print(my_list[0:1])