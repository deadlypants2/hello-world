#hierbij word de stand op nul gezet
state = 0
#Hierbij word de vraag gesteld of de persoon naar de dierntuin gaat.
vraag = str(input("Gaat u vandaag naar de dierentuin?"))
#hierbij word er gecontroleerd of er ja is beantwoord en word er gevraagt hoeveel mensen naar de dierentuin gaan.
if vraag=="ja":
    ask = int(input("Hoeveel mensen gaan met u meen naar de dierntuin? "))
#dit is de loop waar de state word verhoogd met 1 waarna de status word uitgeprint
    for i in range(ask):
        print("Veel plezier!")
else:
    print("Een fijne dag verderr gewenst.")