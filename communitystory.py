def start_game():
    print("Game starting")
start_game()
print("You awake in a pod, it is wet, sticky, slimy, and overall uncomfortable.")
print("Your head throbs as you exit the pod, you have only that throb in your head. No memories, no thoughts. Only this ache in your head.")
print("You parse your surroundings to find you are in a hospital room infested with black vine. There are two doors on either side of your view.")
print("What do you do? Walk left or right? Type in lowercase.")
choice1 = input("> ")

if choice1 == "left":
    print("You enter the room on the left.")
    print("Before you is an entity cloaked in shadow. The room smells of rot and decay.")
    
    print("Do you run away?")
    shadow_choice = input("> ")
    if shadow_choice == "yes":
        print("You try to run away.")
        print("You run as hard as your legs can carry you, you do not look back.")
        print("When you think you are safe, your breath hitches for just a moment and, in that moment, this life is forfeit.")
        print("Game Over.")
        start_game()
    elif shadow_choice == "no":
        print("You attempt to investigate the entity, only to capture its attention.")
        print("Before you is a being of unpercievable light, your vision fades and this life is forefeit.")
        print("Game Over.")
        start_game()
    else:
        print("Invalid Choice. Type yes or no.")

elif choice1 == "right":
    print("You enter the room on the right.")
    print("Within it, you see a single lecturn in an expansive space.")
    print("Emptiness for what appears to be miles.")
    print("Do you look at the book? Or ignore it?")

    book_choice = input("> ")
    if book_choice == "look at the book":
        print("You creep toward the book and, peering at the cover, it is labelled: Secure Contain and Protect.")
        print("Within the book, you realize it is a record kept about something matching your description. It states that you are what is called a creature labelled 177636: The Immortal Amnesiac.")
        print("A truly immortal being that loses their memory upon fatal injury.")
        print("You try to process this information but a pain shoots into your neck, a needle. Your vision fades. Your life is forfeit.")
        print("Game Over.")
    elif book_choice == "ignore the book":
        print("You ignore the book. You have better things to do than read. You wander the void room.")
        print("Weeks then months then years pass. You have nothing in sight of the emptiness you have become accustomed to.")
        print("With nothing to consume or hydrate with, you decide to feast on yourself. Your life is forfeit.")
        print("Game Over.")
    else:
        print("Invalid Choice. Type look at the book or ignore the book.")

else:
    print("Invalid Choice. Type left or right.")