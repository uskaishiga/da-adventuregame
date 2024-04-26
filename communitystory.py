def start_game():
    print("Game loading")
start_game()

def start_game():
    print("You stand outside Nick's childhood mansion")
    startchoices = input("1. Look at the Young family estate | 2. Enter the Young family estate > ")
    print(startchoices)
    if startchoices == "2":
        dumpling()
    else:
        start_game()
def dumpling():
    print("You arrived inside the house. You are invited to make dumplings with the Young family. What will you do?")
    dumplingchoices = input("1. Run away | 2. Fold dumplings beside Astrid > ")
    print(dumplingchoices)
    if dumplingchoices == "1":
        start_game()
    elif dumplingchoices == "2":
        print("You sat down")
        fold_Dumpling()
def fold_Dumpling():
    print("You sit down to learn how to fold dumplings")
    dumplingfold = input("1. you mess up | 2. Fold dumplings correctly> ")
    print(dumplingfold)
    if dumplingfold == "1":
        print("you're incompetent. Start over")
        start_game()
    elif dumplingfold == "2":
        print("You folded it succesfully! Ask around about the family.")
        family_Question()

def family_Question():
    print("Who will you talk to?")
    talkchoices = input("1. Astrid | 2. Nick |3. Aunty 1 |4. Aunty 2> ")
    print(talkchoices)
    if talkchoices == "1":
        print("How did you guys learn?")
        print("We didn't have a choice...")
        rooms()
        start_game()
    elif talkchoices == "2":
        print("How did you guys learn?")
        print("We didn't have a choice...")
        rooms()
    elif talkchoices == "3":
        print("It was for your own good")
        rooms()
    else:
        print("wrong choice")
        start_game()

def rooms():
    print("you leave to the bathroom. You can't find it")
    roomchoices = input("1. Go upstairs | 2. leave the house |3. check the kitchen 1 |4. Aunty 2> ")
    print(roomchoices)
    if roomchoices == "1":
        print("*you see Nick's mother*")
        print("I like how you appreciate our family. But this doesn't just happen. It takes years and sacrifice")
        print("you will never be enough")
        start_game()
    elif roomchoices == "2":
        start_game()
    elif roomchoices == "3":
        print("thats it")
    
    
    

start_game()