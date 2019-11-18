def main ():
	welcome_message = "Welcome to Hallmarklabs' Lunch and Learn!"
	subject = "Let's talk about your favorite food!"
	question(subject)

def question(subject):
	print(subject)

	#Ask user questions and assign responses to vars
	user_name = input("What's your name, weirdo?")
	favorite_food=input("What's your favorite food? Wormmmssss?")

	#conditional logic
	if favorite_food == "Worms":
		print("Hey, "+user_name+", you DO like worms!")
	else:
		print("Oh, sorry! I totally thought you'd like worms and not "+favorite_food+", haaaaahahahha. You're full of surprises, "+user_name+"!")

if __name__=="__main__":
	main()
