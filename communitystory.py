def start_game():
    choice = input("Darkness. A stench assaults you. You're bound. Escape (escape) or accept death (accept)?")
    print(choice)
    if choice == "escape":
        cuffs()
    elif choice == "accept":
     print("You close your eye and let stench consume you and you die")  
    else: 
        start_game()
def cuffs():
    print("Struggling free, you see a knife and reach for it reach for it and free yourself")
    choice = input("look for Light (feel) or scream for help (scream)? ").lower()
    if choice == "feel":
        print("A lamp! You light it. The room is dusty, cobwebs hang, furniture covered in sheets. A chest sits in the center.")
        chest_or_exit()

    elif choice == "scream":
        print("The door creaks open. A skeletal hand appears and call you over. A voice rasps, 'Come...'")
        reach_or_slam()
    else:
        cuffs()  
def chest_or_exit():
    print("Chest (chest) or find an exit (exit)?")
    choice = input().lower()

    if choice == "chest":
        chest_exploration()
    elif choice == "exit":
        print("the door is open with tha hand still calling you forth")
        passage_or_search()
    else:
        chest_or_exit()  
def chest_exploration():
    print("You pry open the rusted chest. Inside: a tattered journal and a gleaming key.")
    print("Read journal (journal) or take key (key)?")
    choice = input().lower()
    if choice == "journal":
        print("The journal details failed escapes from the past. The last mentions a hidden passage behind a loose brick in the fireplace.")
        #fireplace_passage()  
    elif choice == "key":
        print("You pocket the key, with flickering hope.")
        chest_or_exit()  
    else:
        chest_exploration()  
def reach_or_slam():
    print("Reach for the hand (reach) or slam the door (slam)?")
    choice = input().lower()

    if choice == "reach":
        print("The hand vanishes. A cold wind extinguishes the lamp, plunging you back into darkness.")
    elif choice == "slam":
        print("Silence. Footsteps shuffle away. You return to explore the room.")
        chest_or_exit()  
        reach_or_slam()  
def passage_or_search():
    print("Descend into the passage (descend) or search the room further (search)?")
    choice = input().lower()

    if choice == "descend":
        print("You climb down. The passage twists and turns into a dark champber with mellow light.")
    elif choice == "search":
        print("You explore the room further.")
        chest_or_exit()  
    else:
        passage_or_search()  
start_game()