from random import randint

secret = 100
guess = int(input("What is your guess?\n"))

if guess == secret:
	print("correct")

elif guess > secret:
	print("too big")
	guess = int(input("What is your guess?\n"))
	
	if guess == secret:
		print("correct")
	
	elif guess > secret:
		print("too big")
		guess = int(input("What is your guess?\n"))
		
		if guess == secret:
			print("correct")
		else:
			print("game over")
	else: 
		print("too small")
		guess = int(input("What is your guess?\n"))
		
		if guess == secret:
			print("correct")
		else:
			print("game over")
		
else:
	print("too small")
	guess = int(input("What is your guess?\n"))
	
	if guess == secret:
		print("correct")
	
	elif guess > secret:
		print("too big")
		guess = int(input("What is your guess?\n"))
		
		if guess == secret:
			print("correct")
		else:
			print("game over")
	else: 
		print("too small")
		guess = int(input("What is your guess?\n"))
		
		if guess == secret:
			print("correct")
		else:
			print("game over")
