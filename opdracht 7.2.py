#we gaan met een # een pyramide maken in python
symbool = str(input("welk symbool wilt u gebruiken voor de pyramide?"))
symboolp = symbool
state = 0
lagen = int(input("hoeveel lagen moet de pyramide krijgen?"))
while state < lagen:
    print(symboolp)
    symboolp = symboolp + symbool
    state +=1