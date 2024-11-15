#hierbij word de stand op nul gezet
state = 0
#hierbij word de aantal herhalingen gevraagd en als int opgeslagen
leeftijd = int(input("Hoe oud word U? "))
#dit is de loop waar de state word verhoogd met 1 waarna de status word uitgeprint
while state < leeftijd:
    state +=1
    print("Hoera")

#hiermee wordt de random functie geïmporteerd en de lijst gemaakt
import random

rand_list=[]
n=15
for i in range(n):
#    rand_list.append(random.randint(1, 10))
    rand_list.append(random.randint(1,9999999))
#hiermee printen wij de lijst uit
print(rand_list)
#hierbij wordt de lijst gesorteerd en opnieuw uitgeprint
rand_list.sort()
print(rand_list)
#hierbij wordt de lijst bij elkaar opgeteld en uitgeprint
print(sum(rand_list))
#hierbij worden de eerste 8 getallen uitgeprint
print(rand_list[0:8])
#hierbij wordt het derde getal verwijdert
rand_list.pop(3)
#hierbij wordt de 100 in de list toegevoegd op de 11ste plaats
rand_list.insert(10, 100)
#hierbij wordt het aantal getallen in de lijst opgeteld en uitgeprint
x = len(rand_list)
print(x)


#de leeftijd van de hond word opgevraagd
hond = float(input("Wat is de leeftijd van uw hond?\n"))

#als de hond 2 jaar of jonger is dan wordt de makkelijke rekensom uitgevoerd.
if hond <= 2:
    leeftijd = hond * 10.5
#zo niet dan wordt de leeftijd berekend op basis van elk jaar als 4 jaar tellen waarna de eerste 2 jaar handmatig worden toegevoegd.
else:
    leeftijd = hond * 4 + 13
#Waarna de leeftijd wordt uitgeprint
print("Uw hond is", leeftijd, "jaar oud.")