#De OS-module wordt hier geïmporteerd.
#Deze is nodig om met bestanden op de computer te werken
import os

from datetime import datetime

#Hierbij wordt de hoofdmap en de onderliggende bestanden aangegeven.
#Deze zal door alle bestanden gebruikt worden waardoor een variabele in plaats van het pad fijner is.
#Deze zijn zowel als windows als linux variant te zien
hoofdmap_linux = "/home/remco/Documents/python/FietsBV/Nijmegen/Administratie"
onderdelen_linux = os.path.join(hoofdmap_linux, "fietsonderdelen.csv")
klanten_linux = os.path.join(hoofdmap_linux, "klanten.csv")

hoofdmap_windows = "C://FietsBV/Nijmegen/Administratie"
onderdelen_windows = os.path.join(hoofdmap_windows, "fietsonerdelen.csv")
klanten_windows = os.path.join(hoofdmap_windows, "klanten.csv")

#Het bestand klanten.csv en onderdelen.csv worden geopend, uitgeprint en direct erna weer gesloten.

print(open(klanten_linux).read())
print(open(onderdelen_linux).read())

#De module Datetime word geïmporteerd en deze wordt gebruikt om de huidige tijd op te halen.
#De huidige tijd wordt in de variable now geplaatst
now = datetime.now()

#Door middel van de functie strftime wordt de huidige tijd in een string geplaatst en daarna uitgeprint.
currentTime = now.strftime("%H:%M:%S")
print("Current Time =", currentTime)

#Hierbij is een list met namen die gesorteerd worden en daarna weer uitgeprint worden.

names = ["Anna", "Bob", "Charlie", "David", "Emma"]
print(sorted(names))

#Een nieuwe naam wordt achter aan de lijst toegevoegd waarna de lijst wordt gesorteerd en uitgeprint

new_name = input("Voer een naam in om toe te voegen aan de lijst:")
names.append(new_name)
print(sorted(names))

#Een naam moet ingevoerd worden en deze wordt uit de lijst gehaald.
#Hierna wordt de lijst nogmaals gesorteerd en uitgeprint.

del_name = input("Voer een naam in om te verwijderen uit de lijst: ")
names.remove(del_name)
print(sorted(names))