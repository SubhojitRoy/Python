from random import randint

# Subho chooses
Subho = input("rock, paper, or scissors?\n")

# computer chooses
computer = randint(1,3)
if computer == 1:
	computer = "rock"
elif computer == 2:
	computer = "paper"
else:
	computer = "scissors"
print("computer chooses: " + computer)
	
# game logic
if Subho == computer:
	print("tie")
elif (Subho == "rock" and computer == "scissors") or (Subho == "paper" and computer == "rock") or (Subho == "scissors" and computer == "paper"):
	print("Subho wins")
else:
	print("computer wins")
