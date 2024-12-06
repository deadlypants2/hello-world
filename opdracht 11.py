#schaakboard layout: start
board = [["t", "k", "b", "q", "k", "b", "k", "t"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["-", "-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-", "-"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["t", "k", "b", "q", "k", "b", "k", "t"]]
#Om de rijen van het schaakbord onder elkaar te plaatsen.
for x in board:
    print(x)
#dit is om een scheiding te maken tussen de schaakborden en is enkel voor de sier.
print("\n", "---------------------------------------","\n")

#verplaatsen eerste pion
board[6][5] = "-"
board[5][5] = "p"
#Hierbij word het schaakbord nogmaals uitgeprint. Echter, het is ditmaal nadat de pion is verzet.
for x in board:
    print(x)