#Hier word er voor je naam gevraagt waarna deze 100 keer word geprint
name = input("wat is jouw naam? ")
print(name*100)

#hier vragen wij naar het level waarna je in de juiste tier word geplaatst
level = int(input("wat is jouw huidige level? "))
if 0 < level <= 19:
    print("jij bent brons!")
elif 20 <= level <= 39:
    print("jij bent silver!")
elif 40 <= level <= 59:
    print("jij bent gold!")
elif 60 <= level <= 79:
    print("jij bent platinum!")
elif 80 <= level <= 100:
    print("jij bent diamond!")
#waneer het level niet word ondersteund komt er een foutcode uit
else:
    print("Dit level word niet ondersteund(404)")

#hierbij word er naar de hoogte en lengte gevraagt en berekent
lengte = float(input("wat is je lengte in meters? "))
gewicht = float(input("wat is je gewicht in kilo's "))
lengte2 = lengte * lengte
bmi = gewicht / lengte2

#hierbij word het juiste antwoord gegeven met een mogelijke foutstand
if 10 < bmi < 18.5:
    print("Je mag best wat vaker naar de snackbar")
elif 18.5 <= bmi < 25:
    print("Goed bezig!")
elif 25 <= bmi <= 50:
    print("wat vaker naar de sportschool zou misschien wel goed voor je zijn")
else:
    print("de opgegeven informatie is incorect.\nProbeer het opnieuw")

