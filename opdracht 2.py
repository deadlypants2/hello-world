#print de opgegeven zin maar met aanhalingstekens met blanke regel erna
print('Ik hou van “Python”, maar ook van “Powershell”.\n')

#print de 3 regels binnen 1 coderegel met behulp van \n met blanke regel erachter
print(' "I’m”\n""learning""\n"""Python"""\n')

#hierbij berekenen we de belasting
blp = 0.37
inkb = 3000
ble = inkb*blp
inkn = inkb-ble

#hierbij word de eerdere erkening uitgeprint
print("Uw netto loon bedraacht:\n€",inkn,'\n')

#troubeshooting variabellen
#username = "remco"
#adres = "deurnesewge 142"
#postcode = "5813 AB"
#plaats = "Ysselsteyn"


#hierbij worden voor de inloggegevens gevraagd
username = input("Wat is uw naam? ")
adres = input("Wat is uw huidige adres? ")
postcode = input("Wat is de postcode? ")
plaats = input("Wat is de plaatsnaam? ")

#print de gegevens met netto inkomste
print(" Beste",username,"\n",adres,"\n",postcode,plaats,"\nUw netto inkomen van deze periode bevat",inkn)