#BatobatoPick

score=0
compscore=0
draw=0

from random import choice

game=["BATO", "PAPEL", "GUNTING"]

computer_move=choice(game)

for i in range (5):
    player=input("Choose between PAPEL, GUNTING, BATO (use capital letters only): ")
    print("Computer Move: ", computer_move, "\n")
    if player=="PAPEL" and computer_move=="BATO":
        print("Win")
        score+=1
    if player=="BATO" and computer_move=="PAPEL":
        print("Lose")
        compscore+=1
    if player=="GUNTING" and computer_move=="BATO":
        print("Lose")
        compscore+=1
    if player=="BATO" and computer_move=="GUNTING":
        print("Win")
        score+=1
    if player=="PAPEL" and computer_move=="GUNTING":
        print("Lose")
        compscore+=1
    if player=="GUNTING" and computer_move=="PAPEL":
        print("Win")
        score+=1
    if player==computer_move:
        print("Draw")
        draw+=1

print("\nPlayer score: ", score)
print("Computer score: ", compscore)
print("Number of Draws: ", draw)

if score>compscore:
    print("\nPlayer Wins!")
else:
    print("\nComputer Wins!")