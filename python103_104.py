def days():
	day = int(input("Enter a day using a number(0-6): "))
	if day == 0:
		print("Sunday")
	elif day == 1:
		print("Monday")	
	elif day == 2:
		print("Tuesday")	
	elif day == 3:
		print("Wednesday")	
	elif day == 4:
		print("Thursday")	
	elif day == 5:
		print("Friday")	
	elif day == 6:
		print("Saturday")
	else:
		print("Invalid number")	



def w_s():
	work_or_sleep = int(input("Enter a day using a number(0-6): "))
	if work_or_sleep == 1:
		print("Go to work")
	elif work_or_sleep == 2:
		print("Go to work")
	elif work_or_sleep == 3:
		print("Go to work")
	elif work_or_sleep == 4:
		print("Go to work")
	elif work_or_sleep == 5:
		print("Go to work")
	else:
		print("Sleep in")

# #Conversion calc 



def converter():
	celsius = float(input("Please type in a degree in celsius: "))
	conversion = celsius * 1.8 + 32
	print(round(conversion, 2))





# #Tip calculator 1 and 2


def tipcalc():
	check = float(input("How much is the check?: "))
	service = input("How good was the service? (Good, Fair, Poor: ")
	split = int(input("Split how many ways?: "))
	service = service.lower()
	if service == "good":
		goods = (check * .2) + check
		final1 = round(goods/split, 2)
		print("Each person owes $" + str(final1))
	elif service == "fair":
		fairs = (check * .15) + check
		final2 = round(fairs/split, 2)
		print("Each person owes $" + str(final2))
	elif service == "poor":
		poors = (check * .10) + check
		final3 = round(poors/split, 2)
		print("Each person owes $" + str(final3))
	else:
		print("Invalid response")


# for loop

def forloop():
	for i in range(1, 11):
		print(i)

# while loop

def whileloop():
	count = 1
	while count <= 10:
		print(count)
		count = count + 1

# for loop

def start_end():
	start = int(input("Please enter a start number: "))
	end = int(input("Please enter a ending number: "))

	for i in range(start, end):
		print(i)

# while loop


def start_end2():
	start = int(input("Please enter a start number: "))
	end = int(input("Please enter a ending number: "))

	count = start
	while count <= end:
		print(count)
		count = count + 1


#odd numbers

def onlyodds(): 
	odd = []

	for i in range(1, 11):
		if i % 2 != 0:
			odd.append(i)
	print(odd)


def onlyodds2():

	odd1 = []
	count1 = 0

	while count1 < 10:
		count1 = count1 + 1
		if count1 % 2 != 0:
			odd1.append(count1)
	print(odd1)


# Coins

def coins1():
	
	coins = 0

	while True:
		
		question = input("Do you want a coin? ")
		question = question.lower()
		if question == "yes":
			coins = coins + 1
			print("You have " + str(coins) + " coins")
		elif question == "no":
			print("Bye")
			break

def coin_question():
	return input("Do you want a coin? ")

def to_lower_case(n):
	return n.lower()

def if_statement_for_coin(question):
	if question == "yes":
		coins = coins + 1
		print("You have " + str(coins) + " coins")
	elif question == "no":
		print("Bye")
		


def main():
	coins = 0
	coin = coin_question()
	coin = to_lower_case(coin)
	if_statement_for_coin(coin)
	




#Square

def square():
	x = "*****"
	for i in x:
		print(x)




def square2():
	answer = int(input("How big is the square? "))
	for i in range(answer):
		print(str(answer * "*")) 


def square3():

	width = int(input("Please enter width: "))
	height = int(input("Please enter height: "))
	print(width * "*" + "**")
	for i in range(height): 
		print(str("*" + width * " " + "*"))
	print(width * "*" + "**")



#i = 0
# height = 5
# while i < height:
# 	i = i + 1

# 	j = 0
# 	while j < width:
# 		j = j + 1



# Triangle
# for i in range(8):
# 	if i % 2 != 0:
# 		print(i * "*")


# count = 0
# while count < 10:
# 	count = count + 1
# 	if count % 2 != 0:
# 		print(count * "*")

 
# count = 5
# counter = 0

# while count > 0:
# 	print(count * " " + "*")
# 	count2 = count + counter
# 	count3 = count2 * "*"
# 	count = count - 1
	






# Multiplication table


def multi_table():

	for i in range(1, 11):
		for j in range(1, 11):
			print(str(i) + " X " + str(j) + " = " + str(i * j))








#Header


def header(): 
	header = input("Write a header: ")
	headerlen = len(header)
	width1 = headerlen * "*"
	print(width1 + "***")
	print("*" + " " + header + "*")
	print(width1 + "***")


# factor number



def factnum(n):
	
	list2 = []
	count = 0

	while count < n:
		count = count + 1
		if n % count == 0:
			list2.append(count)
	print(list2)

factnum(144)
factnum(200)












# Guess the number


def numbergame():

	import random 

	guess_remain = 10
	guesses = 0
	secret_num = random.randint(1, 101)
	play = True

	while play:
		

		number = int(input("I am thinking of a number between 1 and 100. Try to guess it. "))
		guesses = guesses + 1
		guess_remain = 10 - guesses 
		if number < 0 or number > 100:
			print("invalid number")
			print("The number was " + str(secret_num))
			again = input("Do you want to play again?: Y or N ")
			again = again.lower()
			if again == "y":
				guess_remain = 10
				guesses = 0
				secret_num = random.randint(1, 101)
				play = True
			elif again == "n":
				play = False
		elif number < secret_num:
			print("Too low. You have " + str(guess_remain) + " guesses remaining.")
			if guess_remain == 0:
				print("The number was " + str(secret_num))
				again = input("Do you want to play again?: Y or N ")
				again = again.lower()
				if again == "y":
					guess_remain = 10
					guesses = 0
					secret_num = random.randint(1, 101)
					play = True
				elif again == "n":
					play = False
		elif number > secret_num:
			print("Too high. You have " + str(guess_remain) + " guesses remaining.")
			if guess_remain == 0:
				print("The number was " + str(secret_num))
				again = input("Do you want to play again? Y or N: ")
				again = again.lower()
				if again == "y":
					guess_remain = 10
					guesses = 0
					play = True
					secret_num = random.randint(1, 101)
				elif again == "n":
					play = False
		
		else:
			print("You got it in " + str(guesses) + " tries")
			again = input("Do you want to play again? Y or N: ")
			again = again.lower()
			if again == "y":
				secret_num = random.randint(1, 101)
				guess_remain = 10
				guesses = 0
				play = True
			elif again == "n":
				play = False
















