def start_game():
    print("You just woke up from your nap on the train. You look around the dully-lit cart and feel compelled to explore. Do you want to reach the driver's compartment? ")
    startchoices = input("Yes | No> ")
    print(startchoices)
    if startchoices == "Yes":
        compartment1()
    else:
        compartment3()
def compartment1():
    print("You meet entity 868-4")
    compartment1choices = input("Stay | Leave > ")
    print(compartment1choices)
    if compartment1choices == "Stay":
        print("Narration of entity reaction")
        drivercompartment()
    elif compartment1choices == "Leave":
        print("Narration of reaction 2")
        start_game()
def drivercompartment():
    print("Good ending")
    start_game()
def compartment3():
    print("You meet entity 868-3")
    compartment3choices = input("Fight | Fright > ")
    print(compartment3choices)
    if compartment3choices == "Fight":
        print("Bad Ending 1")
        start_game()
    elif compartment3choices == "Fright":
        print("Bad Ending 2")
        start_game()
start_game()