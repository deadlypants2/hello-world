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
date=date.today()


repeat = 0
dierentuin = int(input("Ga jij Naar de Dierentuin? \n 1 = Ja \n 2 = nee \n: "))


if dierentuin == 1:
    print("Leuk!")
    aantalm = int(input("Met hoeveel mensen ga je\n: "))
    while repeat < aantalm:
        repeat +=1
        print("ticket nummer:","DT -", date,"-", repeat, "\nActief Vanaf : ", date, "\n")
elif dierentuin==2:
    print("Jammer")
elif dierentuin==0:
    print("Niet doen!")
else:
    print("Ongeldig antwoord")
