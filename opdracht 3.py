#print de opgegeven zin en maak van Naam,salaris en woonplaats variabelen
voornaam="John Doe"
salaris="3000"
woonplaats="Nijmegen"
print("Hallo, ik heet",voornaam,"ik verdien",salaris,"euro en ik woon in het mooie",woonplaats,)


#print met behulp van variable agent 007
agent = "007"
print("agent",agent)

#het vragen van de demensies van de tank
hoogte = float(input("hoe hoog is de tank in cm? "))
breedte = float(input("hoe breed is de tank in cm? "))
lengte = float(input("hoe lang is de tank in cm? "))
#hierbij de berekening van inhoud
inhoud = hoogte*breedte*lengte/1000
print("de inhoud van uw tank bevat",inhoud,"dm³")

#Maak een script dat met de input om de gegevens van de gebruiker vraagt
naam = input("Hallo, Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
mtelefoon = input("Wat voor merk telefoon gebruik je? ")
mlaptop = input("En welk merk is je laptop? ")
plaptop = int(input("Wat heeft je laptop gekost? "))
#de leeftijd en btw berekening
feitleeftijd = leeftijd+10
berekeningbtw = plaptop*0.21
#het uitprinten van de gegevens
print("Hallo",naam,", dus jij bent",leeftijd,"jaar oud en hebt een",mtelefoon,"en een",mlaptop,)
print("wist jij dat je over 10 jaar al",feitleeftijd,"bent!")
print("Wist je ook dat je maar liefst €",berekeningbtw,"aan BTW hebt betaald!")