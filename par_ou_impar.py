x = input("do you want to play? yes or no")
while (x == "yes"):
	choice = input("even or odd")
	import random
	number_a = random.randrange(1,10)
	number_b = input("type a number")
	print(number_b)
	print(number_a)
	try:
		number = number_a + int(number_b)
	except:
		print("invalid input")
	print("the result is" + " " + str(number))
	if number % 2 == 0 and choice == "even":
		print("you win")
	elif number % 2 != 0 and choice == "odd":
		print("you win")
	elif number % 2 == 0 and choice == "odd":
		print("you lose")
	elif number % 2 != 0 and choice =="even":
		print("you lose")
	else:
		print("invalid input")
	x = input("do you want to play again? yes or no")

