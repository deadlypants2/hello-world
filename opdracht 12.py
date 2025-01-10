voldoende = input("Heb jij een voldeonde gehaald voor de toets?")
#Hierbij word gevraagd of de student een voldoende heeft behaald voor de toets.
if voldoende == "ja":
    cijfer = float(input("Wat is het cijfer wat je voor de toets hebt gehaald?"))
    print("Wow, heb jij een",cijfer, "Gehaald?!")
    # In het geval dat de student een voldoende heeft behaald wordt er ook gevraagd welk punt hij heeft.
    # Dit wordt dan als positieve feedback aan de student teruggestuurd.
elif voldoende == "nee":
    print("Ah jammer, volgende keer beter.")
    #In het geval dat de student geen voldoende heeft gehaald krijgt de student de melding dat wij hem succes melden bij de volgende poging.
else:
    print("Voer A.U.B. een geldig antwoord in")
    #in het geval dat de student een ongeldig antwoord invult vragen wij of hij een geldig antwoord invult.


my_list = [1, 4, 12, 168, 7, 59, 24, 5]
my_list.sort()
#De lijst word aangegeven en gesorteerd.
print(my_list[2:7])
#hier wordt middels slices alleen de laatste 5 elementen weergegeven.

del my_list[0:2]
print(len(my_list))
#met deze slices worden de eerste 3 elementen weg gehaald.

print(sum(my_list))
#hier wordt opgeteld hoeveel elementen er in de list zitten.

avg = sum(my_list) / len(my_list)
print(avg)
#Hier wordt het gemeelde berekent en uitgeprint.