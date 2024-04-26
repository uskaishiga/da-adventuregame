def start_game():
    print("You're at your grandparents' house and you find yourself bored. What do you do?")
    startchoices = input("1. Open the fridge | 2. Visit the dusty library| 3. Take a nap >")
    print(startchoices)
    if startchoices == "1":
        fridge()
    elif startchoices == "2":
        library()
    elif startchoices == "3":
        nap()
def fridge():
    print("You open the fridge and find nothing appetizing. Same as the last time you opened it 5 minutes ago. There is, however, something you did not remember seeing behind the milk. Do you check what it might be or do you leave?")
    fridgechoices = input("1. Check | 2. Leave >")
    print(fridgechoices)
    if fridgechoices == "1":
        check()
    else:
        start_game()
def check():
    print("You push around the stale bread and cheese and reach for the milk. Behind it you see a golden truffle. Your mouth waters at the sight of it. Do you eat it or resist taking it for yourself?")
    checkchoices = input("1. Eat it | 2. Resist >")
    print(checkchoices)
    if checkchoices == "1":
        eat()
    else:
        start_game()
def eat():
    print("With delight, you take the treat and eat it in one bite. Every munch is flavorful and delicious; however, you begin feeling a bit strange.")
    print("Perhaps you should lie down.")
    eatchoices = input(" 1. Lie down | 2. Other option >")
    print(eatchoices)
    if eatchoices == "1":
        Narnia()
    else:
        no_lie_down()
def no_lie_down():
    print("I suggested you lie down. ")
    no_lie_downchoices = input("1. Lie down | 2. Other option >")
    print(no_lie_downchoices)
    if no_lie_downchoices == "1":
        Narnia()
    else:
        print("I see. Let’s try this again.")
        start_game()
def library():
    print("You walk down the hall and enter a room filled with tilted bookshelves toppled with random antiques and objects. The carpet’s once intricate design is blurred with dust and grime. Yet amidst the mess and the stuffy ambience, there is something about this room that draws you in. Do you look through the shelves or check the window?")
    librarychoices = input("1. Shelves | 2. Check window >")
    print(librarychoices)
    if librarychoices == "1":
        shelves()
    else:
        window()
def shelves():
    print("You look through the shelves and piles of books. Most are worn and tattered. Although, you can imagine that under all the dust, this room would have been grand long ago. Strangely, a flash of gold catches your eye. Do you check it out or leave the room?")
    shelveschoices = input("1. Check | 2. Leave >")
    print(shelveschoices)
    if shelveschoices == "1":
        magic_book()
    else:
        start_game()
def magic_book():
    print("You follow your gaze in the direction where you saw something shine. Deep in a pile of books you see a leatherbound book gilded with gold designs peeking through. Suddenly there is a loud knock at the door. Did you look through the window? I told you shouldn’t have tried. It doesn’t matter. Quickly now, do you take and open the book, or do you stare and wait to see who is at the door?")
    magic_bookchoices = input("1. Open the book | 2. Wait >")
    print(magic_bookchoices)
    if magic_bookchoices == "1":
        open_book()
    else:
        wait()
def open_book():
    print("You've opened the book just in time. It appears that the book is not only inlaid in gold, but that the very pages are gold. You are blinded by the sheer shine of it all.")
    Narnia()
def wait():
    print("You should have followed my advice.")
    start_game()
def window():
    print("There is no window. Don't look outside.")
    shelves()
def nap():
    print(": You find yourself bored enough that you've become a bit sleepy. Maybe you should lie down. Where would you like to nap?")
    napchoices = input("1. Master bedroom | 2. Sofa | 3. Attic >")
    print(napchoices)
    if napchoices == "1":
        bedroom()
    elif napchoices == "2":
        sofa()
    else:
        attic()
def bedroom():
    print(": You yawn as you head towards the master bedroom. It smells a bit funky, but everything in this house does so you don't think much of it. Do you lie down immediately or look around?")
    bedroomchoices = input("1. Lie down | 2. Look around >")
    print(bedroomchoices)
    if bedroomchoices == "1":
        print("Right away you jump into the bed, softer and more comfortable than it looks. You instantly feel like sleep is calling out to you. Take the nap, you deserve it.")
        Narnia()
    else:
        look_bedroom()
def look_bedroom():
    print("Although you feel sleepy, you get a sudden pang of curiosity and decide to look around. The vanity is slightly disorganized, some things crooked or slightly out of place. The whole theme of the room resembles the 1950s, or maybe the Renaissance? No it's probably 1880s Victorian. You begin to have a headache, these slight inconsistencies worrying your mind more than they should. However, you find two objects that caught your eye. Which one do you take?")
    look_bedroomchoices = input("1. A lighter | 2. Old carnival tickets >")
    print(look_bedroomchoices)
    if look_bedroomchoices == "1":
        any_object()
    else:
        any_object()
def any_object():
    print("You yawn once more, feeling truly exhausted. You head to bed, placing the object in your pocket and lie down, feeling the darkness engulfing you.")
    Narnia()
def sofa():
    print(" You head to the couch, not bothering with somewhere else. The couch is filled with dust, so as you plop down, a cloud of dust engulfs you. However, this movement has caused some weird crinkly noise to happen. Do you check what it might be or do you decide to head upstairs?")
    sofachoices = input("1. Check | 2. Head upstairs >")
    print(sofachoices)
    if sofachoices == "1":
        print(" You shift your hand around the surface of the sofa and find that you had sat on an old looking, wrinkly paper. Just as you're about to unfold it and see what might be written inside, you hear footsteps coming your way. Quick!  Put it away and pretend you're asleep.")
        Narnia()
    else:
        upstairs()
def upstairs():
    print("Maybe the couch isn't the best place to rest. Well, if you're still sleepy you could always go to the bedroom, or do you wish to check out the attic?")
    upstairschoices = input("1. Bedroom | 2. Attic >")
    print(upstairschoices)
    if upstairschoices == "1":
        bedroom()
    else:
        attic()
def attic():
    print("For some reason, you decide to go to the attic. You climb up the creaking stairs. You reach what looks like to be a door. Once you open it, you peek into the room. It's pitch dark. You walk in and fumble through the cluttered space until you find the light switch. The attic is now mostly illuminated. Do you walk deeper into the room, or stay near the door?")
    atticchoices = input("1. Walk deeper into the room | 2. Stay near >")
    print(atticchoices)
    if atticchoices == "1":
        explore()
    else:
        stay_near()
def explore():
    print("You step into the room and look around. There are boxes, different sorts of objects covered in white sheets. Like most in the house, all is covered in dust. As you keep walking there seems to be a small clearing from all the clutter. There you see a polished, deep mahogany wooden dresser. It looks out of place, not only because of its grandeur but because of its cleanliness. Do you decide to open it or do you decide to leave?")
    explorechoices = input("1. Open it | 2. Leave >")
    print(explorechoices)
    if explorechoices == "1":
        Narnia()
    else:
        nap()
def stay_near():
    print(" You decide to stay near the door just in case you wish to leave. However, the door is now shut. Do you wish to leave or explore further?")
    stay_nearchoices = input("1. Leave | 2. Explore >")
    print(stay_nearchoices)
    if stay_nearchoices == "1":
       print("You pull hard on the door. You don't think it's locked. Finally, it budges open.")
       start_game()
    else:
        explore()
def Narnia():
    print("You find yourself cold and disoriented. You open your eyes to find your surroundings completely white! You blink a couple of times in confusion as your vision begins to clear up. Your surroundings are in fact, not completely white, but covered in snow. You find your surroundings to be huge. Looming trees above you and light coming from seemingly nowhere but everywhere at once. You lift up your head to contemplate your surroundings. A snowflake falls on your nose which makes you shiver slightly. You reach up to wipe the coldness of your nose but find your hand to be a paw instead of a hand. You've now become a cat!")
start_game()