#hierbij word de stand op nul gezet
state = 0
#Hierbij word de vraag gesteld of de persoon naar de dierntuin gaat.
vraag = str(input("Gaat u vandaag naar de dierentuin?"))
#hierbij word er gecontroleerd of er ja is beantwoord en word er gevraagthoeveel mensen naar de dierentuin gaan.
if vraag=="ja":
    ask = int(input("Hoeveel mensen gaan met u meen naar de dierntuin? "))
#dit is de loop waar de state word verhoogd met 1 waarna de status word uitgeprint
    while state < ask:
        state +=1
        print("Veel plezier!")
else:
    print("Een fijne dag verderr gewenst.")