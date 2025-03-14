#De OS-module word hier geimporteerd.
#Deze is nodig om met bestanden op de computer te werken
import os

#Hierbij worden de hoofd map en de map die aangemaakt moet worden aangegeven
directory = "fruit"

hoofdfolder = "/home/remco/Documents/python/"

#De eerder aangegeven mappen worden hierbij samengevoegd in 1 variabelen
path = os.path.join(hoofdfolder, directory)

#Indien de map /home/remco/Documents/python/fruit niet bestaat word deze aangemaakt.
os.makedirs(path, exist_ok=True)

#Hierbij word de variabele voor het bestand aangemaakt.
bestand = os.path.join(path, "fruitsoorten.txt")

#Indien dit bestand nog niet bestaat dan word deze aangemaakt
if not os.path.exists(bestand):
    with open(bestand, "x"): pass

#Nadat het bestand is aangemaakt wordt deze gevult met de benodigde informatie.
with open(bestand, "w") as f:
    f.write("appel\n"
            "peer\n"
            "kers\n"
            "aardbei\n"
            "mandarijn\n"
            "sinaasappel\n"
            "watermeloen")

#Hierbij word het bestand geopend en de eerste lijn word uitgeprint.
file = open(bestand)
content = file.readlines()
print(content[0])

#Het bestand word geopend en passievrucht word aan het einde van het bestand toegevoegd waarna de inhoud word uitgeprint.
with open(bestand, "a") as fruitsoorten:
    fruitsoorten.write("passievrucht\n")
print(open(bestand).read())

#Alle bestanden van de root folder worden hierbij uitgeprint.
print(os.listdir("/"))
