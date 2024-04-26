print("You were day dreaming, someone woke you up, you're in a McDonalds.")
def start_game():
    print("They're calling you to pick up your Big Mac.")
    startchoices = input("1. Stay sitting down | 2. Go get your Big Mac | 3. Leave the restaurant >")
    print(startchoices)
    if startchoices == "1":
        Path1()
    elif startchoices == "2":
        Path2()
    elif startchoices == "3":
        Path3()
    else:
        start_game()
def Path1():
    print("They are yelling at you to pick it up.")
    path1choices = input("1. Go get your Big Mac  | 2. Leave the restaurant | 3. Stay sitting down (bad idea) >")
    print(path1choices)
    if path1choices == "1":
        Path2()
    elif path1choices == "2":
        print("You left the restaurant, douche.")
    elif path1choices == "3":
        print("They cursed at you and threw the Big Mac at you. You left out of shame.")
        exit()
    else:
        print("You should probably do something")
        Path1()
def Path2():
    print("You get up from your seat with the intention to grab your Big Mac, along the way you step on a grasshopper.")
    path2choices = input("1. Move on | 2. Mourn. | 3. Leave the restaurant >")
    print (path2choices)
    if path2choices == "1":
        print("You ignore the murder you've committed, after all, it's just a grasshopper.")
        Path4()
    elif path2choices == "2":
        print("You mourn the loss of innocent wild life, how compassionate. You move on to get your Big Mac.")
        Path4()
    elif path2choices == "3":
        Path3()
    else:
        print("You were thinking about something and forgot what it was. The dead grasshopper is still in front of you.")
        Path2()
def Path3():
    print("You left the restaurant without picking up your Big Mac. Don't worry they'll probably eat it or give it away, whether or not you think you're a philanthropist and not entitled isn't up to me.")
    exit()
def Path4():
    print("You arrived at the counter.")
    path4choices = input("1. Take your Big Mac and leave | 2. Thank the worker and leave with your Big Mac | 3. Throw the Big Mac at the worker >")
    print(path4choices)
    if path4choices == "1":
        print("Enjoy.")
        exit()
    elif path4choices == "2":
        print("They reply with gratitude, you can feel the increase in your karma. Now eat the damn Big Mac.")
        exit()
    elif path4choices == "3":
        print("You throw the burger at the worker.")
        print("They respond by beating the hell out of you, making you black out.")
        print(" ")
        print("You wake up in terror, must've been a bad dream.")
        print(" ")
        start_game()
    else:
        print("Don't go shy now, do something.")
        Path4()
start_game()