'''#hier zet ik de staat van repeat standaard op 0
repeat = 0
#hier vraag ik om het aantal keren dat het herhaald moet worden
ask = int(input("Hoe vaak wilt u de zin herhalen? "))

# Hier begint de while loop waarin hij repeat verglijkt met ask dus 0 verglijkt met het opgegeven getal
while repeat < ask:
    repeat +=1
    print("dit word", repeat, "x" ,"keer Herhaald")

'''

from datetime import date
from time import sleep

date = date.today()
from datetime import date as DateClass, timedelta

# Huidige datum
vandaag = DateClass.today()
repeat = 0
dierentuin = input("Ga jij Naar de Dierentuin?: ")

if dierentuin == "ja" or dierentuin == "Ja":
    sleep(1)
    print("Leuk!")
    aantalm = int(input("Met hoeveel mensen ga je\n: "))
    dagen = int(input("Over hoeveel dagen ga je?: "))
    tijdsdelta = timedelta(days=dagen)
    ticketdatum = vandaag + tijdsdelta

    while repeat < aantalm:
        sleep(1)
        repeat += 1
        print("ticket nummer: DT-{}_{}\nActief Vanaf: {}\n".format(vandaag.strftime("%Y-%m-%d"), repeat, ticketdatum.strftime("%Y-%m-%d")))
elif dierentuin == "nee" or dierentuin == "Nee":
    print("Jammer")


else:
    print("Ongeldig antwoord. Voer 1 of 2 in:")

