def start_game():
    print("You wake up and the first thing you see is space. Just earth and the stars, in a rush you get up and see that you are in a capsule of some sorts. You ask yourself how did you get there are vagely remember being bemed up? Am i in an alien ship? You look ahead and realize you have 3 options in the form of strage looking opening that resembles a door. Type the number of the choice you want.")
    startchoices = input("1. Wait patently to see if any life forms will enter. | 2. investigate around. | 3. Exit the room you find yourself in.  > ")
    print(startchoices)
    if startchoices == "1":
        Patiently()
    elif startchoices == "2":
        investigation() 
    elif startchoices == "3":
        exit()  
    else:
        start_game()
def Patiently():
    print("You wait patiently for what felt like hours and eventually a doors seperated and revealed a strage looking life form")
    livingroomchoices = input("1. attack | 2. Try to communicate | 3. fake uncounssiouness > ")
    print(livingroomchoices)
    if livingroomchoices == "1":
         print("You punched him in the face a knocked him out after that you somehow figured out how to navigate the ship and crashed to earth")
    elif livingroomchoices == "2":
       print("You attempted to communicate and the alien shot you with his laser eyes. Your head melted. You've died.")
    elif livingroomchoices == "3":
        print("You faked being knocked out and the aliens took you and probed you in the ear.")
    else:
        print("That is not a valid option, try again")
        Patiently()
        
def investigation():
        print("You looked around and under the bed there was a strange looking blaster, with this you can defend yourself at range.")
        livingroomchoices = input("1. Leave the room | 2. wait behind the door  | 3. Test shoot it to the wall > ")
        print(livingroomchoices)
        if livingroomchoices == "1":
            print("You leave the room and encounter the alien life form in a Mexican stand of when unowingly it was high noon. DRAW. you missed and got shot in the head. You've died.")
        elif livingroomchoices == "2":
            print("You wait patiently next to the door out of plain sight to any entering person. After 30 minutes the door opened and you threw yourself to the floor at shoot up John Wick style . Lukily you hit him in the head for an instant death.")
        elif livingroomchoices == "3":
            print("When you hold down the trigger the blaster seemed to charge the shoot, so when you realesed the triger a laser KAMEHAMEHA came out and broke the wall and since you are in space you can make out what happened. You've died.")
        else:
            print("That is not a valid option, try again")
            Patiently()
            
def exit():
        print("You exited the room through the door and found three more doors one directly in front, the other to the left, and the other to the right.")
        livingroomchoices = input("1. Go through the door infront of you.  | 2. Go through to the door to the left  | 3. Go through to the right door. > ")
        print(livingroomchoices)
        if livingroomchoices == "1":
            print("You walk to the door but when you are about to pass the door it opens and you come face first with the alien life form without being able to react you are injected with some sort of tranqulizer and the last thing you see inb being taken back to square one.")
        elif livingroomchoices == "2":
            print("When you go through the left door you her something behind you like a door opening. In panick you quickly survey the room and find some sort of virtual data storage. When you open it you find out that there is a bounty on your head and question why. You think about it and find a way to claim the bounty for yourself making you rich. but what the value of wealth when there is alien behind you. SLASH. You've died.")
        elif livingroomchoices == "3":
            print("When you go through the right door you her something behind you like a door opening. In panick you quickly survey the room and find it to be an escape room with one singular escape pod. You quickly figure how to activate it and escape seeing tha face of the alien that almost caught you. You've Escape, For now.....")
        else:
            print("That is not a valid option, try again")
            Patiently()
                
start_game()

