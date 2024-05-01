def start_game():
    print("You arrive at 64th South King Drive also known ")
    startchoices = input("1. Keep walking | 2. Go towards them > ")
    print(startchoices)
    if startchoices == "2":
        conflict()
    else:
        start_game()

def conflict():
    print("They feel threatened and start to come towards you with weapons in their hands. What will you do?")
    conflictchoices = input("1. Fight back | 2. Run away | 3. Cry > ")
    print(conflictchoices)
    if conflictchoices == "1":
        print("You get shot 47 times in the chest and die")
        start_game()
    if conflictchoices == "2":
        chase()
    elif conflictchoices == "3":
        print("Crying only makes them happier they kidnap you and ship you to China")
        start_game()
        
def chase():
    print("They start chasing you and then the cops get involved, and now theres a big gunfight. What will you do?")
    chasechoices = input("1. Escape through the sewers | 2. Use a nearby gun and defend yourself | 3. Break into a house to escape >")
    print(chasechoices)

    if chasechoices == "1":
        sewerchoices()
    if chasechoices == "2":
            #issue here
        while True:
            import random
            print("Where do you shoot?")
            gangster=["1","2","3"]
            gangsterchoice = random.choice(gangster)
            userchoice = input("1. Head | 2. Chest | 3. Genitals >")
            if userchoice == gangsterchoice:
                print("You shoot each other and both end up dying in the process")
            if userchoice == "2":
                if gangsterchoice == "3":
                    print("You get shot and die")
            else:
                print("You were able to kill the gangsters, the police award you with a medal and you go back home")    
            if userchoice == "3":
                if gangsterchoice == "1":
                    print("You get shot and die")
            else:
                print("You were able to kill the gangsters, the police award you with a medal and you go back home")    
            if userchoice == "1":
                if gangsterchoice == "2":
                    print("You get shot and die")
            else:
                print("You were able to kill the gangsters, the police award you with a medal and you go back home")
            break
        start_game()
    elif chasechoices == "3":
        print("You find yourself in a broken down house with an old half-blind man with a double barrel, he shoots you thinking you are an enemy spy")
        start_game()

def sewerchoices():
    print("You see three tunnels in front of you which will you choose?")
    sewerdecisions = input("1. Left | 2. Right | 3. Forward >")
    print(sewerdecisions)
    if sewerdecisions == "1":
        print("Its a dead end")
        sewerchoices()
    if sewerdecisions == "2":
        print("Some gang members were abusing of psychadelics and shoot you on sight")
        start_game()
    if sewerdecisions == "3":
        print("You escape from the sewers and find yourself inside of a KFC bathroom. You see an asian man, a white man and a black man nobody says anything for a good minute, how will you respond?")
        bathroom()
            
def bathroom():
    bathroomchoices = input("1. Offer to buy them food | 2. Try making a joke >")
    print(bathroomchoices)
    if bathroomchoices == "1":
        print("All of you eat in peace and live happily ever after")
        start_game()
    elif bathroomchoices == "2":
        print("There is another moment of silence and then they proceed to angrily beat you to death")
        start_game()
start_game()
