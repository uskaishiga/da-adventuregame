def start_game():
    print("You just woke up from your nap on the train. You look around the dully-lit cart and feel compelled to explore. Do you want to reach the driver's compartment? ")
    startchoices = input("Yes | No> ")
    print(startchoices)
    if startchoices == "Yes":
        compartment1()
    else:
        compartment3()
def compartment1():
    print("You leave your original compartment and head forward towards the first compartment. When you arrive, you take note that the cart is well-lit. You look ahead and see an entity before you. It is a female ball-jointed doll with cracks spread all over her body, mended with gold. Alarmingly, in the center of her chest is a live, beating heart laid bare. Her eyes are that of a regular human. You are scared, but she calmly introduces herself as 868-4. 868-4 invites you to stay in the compartment for as long as you need.")
    print("Will you stay or will you leave?")
    compartment1choices = input("Stay | Leave > ")
    print(compartment1choices)
    if compartment1choices == "Stay":
        print("868-4 smiles and nods her head in approval. You sat with her and stayed in the compartment for as long as you wanted.")
        drivercompartment()
    elif compartment1choices == "Leave":
        print("868-4 releases a sad sigh. She says you are welcome to return to the compartment anytime.")
        start_game()
def drivercompartment():
    print("After spending time with 868-4, she bids you goodbye as you decide to complete your journey and head towards the driver's compartment. The cart is brightly lit, but not in an uncomfortable way, in a warm way. The compartment was empty, but in time you returned.")
    print("Good ending: Local psychiatric hospital patient _______ was discharged on XX/XX/XXXX. She returns home feeling clearheaded and in the most control of herself in years.")
    start_game()
def compartment3():
    print("You leave your original compartment and head backward to the third compartment. The cart is dark, and it makes you uncomfortable. You hear rustling and see an entity before you. It is a female ball-jointed doll with deep cracks all over her body, splitting her apart. She moves erratically, with her eyes pushed far back into her faceplate, a beating heart barred off by the ribcage, and carved into her collarbone is 868-3. You are scared and look for the exit back to your cart, but the door has disappeared, with only a dilapitated door on the other end of the third compartment. There is no going back.")
    print("You lock eyes with 868-3, and she starts charging towards you. She starts manhandling you towards the dilapitated door. You have two choices: Fight or Fright.")
    compartment3choices = input("Fight | Fright > ")
    print(compartment3choices)
    if compartment3choices == "Fight":
        print("You enter an intense struggle against 868-3's manhandling. You manage to overpower 868-3, pinning her against one of the cart walls and bashing her head into the wall until it shatters.You feel a terrible pain in your head and black out.")
        print("Bad ending 1: Local psychiatric hospital patient ______ committed suicide on XX/XX/XXXX. The poor woman was losing her mind and killed herself before she went insane by bashing her head repeatedly into the walls until she died of blunt-force head trauma.")
        start_game()
    elif compartment3choices == "Fright":
        print("You are paralyzed with shock and can't find the strength to fight back. 868-3 pushes you into the darkness beyond the dilapidated door. You have lost your composure and are sobbing before you black out.")
        print("Bad ending 2: ________ has been declared a permanent patient in the psychiatric hospital on XX/XX/XXXX. The poor woman has lost her mind beyond repair.")
        start_game()
start_game()