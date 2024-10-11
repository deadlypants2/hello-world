#hierbij word de stand op nul gezet
state = 0
#hierbij word de aantal herhalingen gevraagd en als int opgeslagen
ask = int(input("Hoe vaak wilt u de zin herhalen? "))
#dit is de loop waar de state word verhoogd met 1 waarna de status word uitgeprint
while state < ask:
    state +=1
    print("Count is =", state)