def start_game():
    print("You wake up in tight, dark space, it seems like you are in a locker. What do you do? (type the number to choose)")
    startchoices = input("1. SCREAM | 2. Cry | 3. Thrash around > ")
    print(startchoices)
    if startchoices== "1":
        print("But no one came")
        start_game()
    elif startchoices== "2":
        print("crybaby")
        start_game()
    elif startchoices== "3":
        print("The locker opened and you fall to the ground")
        classroom()
    else:
        print("that was not one of the options")
def classroom():
    print("You stand up and look around, then a loud sound comes from the locker nect to yours. waht do you do")
    startchoices = input("1. run away| 2. do nothing | 3. you open it > ")
    print(startchoices)
    if startchoices== "1":
        print("scaredycat")
        classroom()
    elif startchoices== "2":
        print("um.. you do that... i guess...")
        classroom()
    elif startchoices== "3":
        print("a boy comes out of the locker")
        classroom2()
    else:
        print("that was not one of the options")
def classroom2():
    print("the boy ask you whereare we, what do you say")
    startchoices = input("1. i love you| 2. dont answer him | 3. in hell i guess > ")
    print(startchoices)
    if startchoices== "1":
        print("THIS IS NOT A ROMANCE NOVEL")
        classroom2()
    elif startchoices== "2":
        print("WOW so cool, look at this guy, he thinks he is soooo cool")
        classroom2()
    elif startchoices== "3":
        print("nvm this person is boring let me start again")
        start_game()
    else:
        print("that was not one of the options")

start_game()