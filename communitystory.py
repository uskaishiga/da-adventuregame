def start_game():
    print("Perhaps the real Git was the friends we made along the way")
start_game()
print("Welcome to Eggland!!! Here, we worship our lord and savior: Egg. Would you like to join us in the Egg shrine?")
startchoices = input("1. I don't want to enter... | 2. I would love to worship the Egg!!! >")
print(startchoices)
if startchoices == "2":
        EggShrine()
else:
        print("HOW DARE YOU?! Let's try that again.")
        start_game()
def EggShrine():
    print("We're so glad you decided to praise Egg with us!")
    shrinechoices = input("1. Fall onto your knees and start praising. | 2. Spit on the giant Egg statue. >")
    print(shrinechoices)
    if shrinechoices == "1":
        EggHeaven()
    elif shrinechoices == "2":
        EggHell()
    EggShrine()
def EggHeaven():
    print("Congratulations!! You have ascended into Egg Heaven. You are the great Chosen One and will takeover the Egg throne after our lord retires. You won the game.")
    start_game()
def EggHell():
    print("You disrespected our Egg lord!!! Now you must pay for your sins in Egg Hell. Get ready for punishment!!")
    hellchoices = input("1. Accept your fate. | 2. Transform into Egg >")
    if hellchoices == "1":
        print("Better luck next time...")
        start_game()
    else:
        print("OH MY EGG!!! YOU ARE THE EGG LORD HIMSELF!! I'M SO SORRY FOR DISRESPECTING YOU! We will worship you forever.")
        start_game()
start_game()