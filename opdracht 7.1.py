state = 1
#Hierbij word de vraag gesteld welke tafel weergeven moet worden
cijfer = int(input("Van welk cijfer wilt u de tafel zien?"))
antwoord = state * cijfer
while state < 11:
    print(state,"*",cijfer,"=",antwoord)
    state +=1