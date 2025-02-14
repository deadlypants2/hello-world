#hierbij wordt gevraagd hoeveel zinnen nodig zijn.
#count = int(input("Typ een getal"))
#Hierbij wordt de stand van het variabele number op 1 gezet. Hier is specifiek voor 1 gekozen zodat de eerste zin met 1 begint.
#number = 1
#zolang de variabele number lager of gelijkt blijft aan het gevraagde aantal zinnen wordt de print statement uitgevoerd met de number variable die aangeeft hoeveel zinnen er al zijn uitgeprint.
#while number <= count:
#    print("Print deze regel", number, "keer uit")
#    number += 1

#hierbij maak je een lijst aan
#my_list = []
#zolang deze lijst geen 15 characters heeft wordt de volgende code uitgevoerd
#for i in range(15):
#binnen deze lijst wordt een character erachter aan geplaatst die het vorig character is +1
#    my_list.append(i + 1)
#Als laatste wordt de lijst uitgeprint
#print(my_list)

#Hier worden 2 variabele aangegeven
namen = []
stop = ["q", "Q"]
#zolang de characters binnen de stop variabelen niet gebruikt worden zal het script telkens opnieuw naar een naam vragen.
while True:
    naam = input("Voer een naam in (of typ 'q/Q' om te stoppen): ")
    if naam in stop:
        break
    if naam != "":
        namen.append(naam)
#nadat een stop character gegeven wordt zullen alle aangegeven namen uitgeprint worden
print("De ingevoerde lijst is:", namen)