def start_game():
    print("You awake in the chair of a hospital room, the beep of the heartrate monitor can be heard in the room. As you look around you see your dad in the hospital bed. Next to the bed is a clipboard with writing on it. Type the number of your option")
    startchoices = input("1. Cry yourself to sleep | 2. Talk to your dad | 3. Pick up the clipboard | 4. leave > ")
    print(startchoices)
    if startchoices == "1":
        print("You fall back asleep. You are awoken a few hours later by doctors, they've come to break you some news. Your dad died from cancer, and you have to pay the bill. In order to pay the bill the doctors knock you unconscious and sell your organs.")
        start_game()
    elif startchoices == "2":
        print("You talk to your father, and as he is telling you about where he left the family fortune the heartrate monitor begins to beep as it flattens out into a line. In his final breaths he pulls you close and whispers in your ear how much of a disappointment you are. Doctors come into the room and ask how you are going to pay for the expenses.")
        choices1 = input("1. Give me more time, I'll get you the money | 2. You didn't even cure the cancer, why should I have to play? | 3. Offer your body as payment > ")
        print(choices1)
    elif startchoices == "3":
        print("You pick up the clipboard and see the massive hospital bill, in the hundreds of thousands. It says you have 5 days to pay.")
        choices2 = input("1. Join your father because you don't have the money to pay. | 2. leave the hospital > ")
        print(choices2)
    elif startchoices == "4":
        print("You leave your barely breathing father in the hospital bed, and a day later you are notified that your father has passed. You are notified that you have only a few days to pay the bill of several hundred thousand dollars. You remember that somehow you need to come up with the money.")
        moneygainchoices = input("1. rob the old lady | 2. Talk to Gregory > ")
        print(moneygainchoices)
def choices1():
    if choices1 == "1":
        print("The doctor frowns and tells you t    hat you have 5 days left to pay, they then kick you out of the hospital, telling you to only come back when you have the money. Knowing that you do not have the money to pay the hospital debts you come to the realization you only have 4 choices to get the money.")
        moneygainchoices = input("1. rob the old lady | 2. Talk to Gregory > ")
        print(moneygainchoices)
    elif choices1 == "2":
        print("The doctor laughs before pulling out a bat. He says that you'll pay willingly or not, he then knocks you out. The doctors then take your organs while you are asleep, killing you.")
        start_game()
    elif choices1 == "3":
        print("The doctor laughs before pulling out a bat. He says that will work. You are knocked out and the doctors harvest your organs to sell while you are asleep, killing you in the process.")
        start_game()
def choices2():
    if choices2 == "1":
        print("You force yourself to stay at your dead father's bedside, wasting away until after several days without water and food your soul joins his in the afterlife.")
        start_game()
    elif choices2 == "2":
        print("You walk out onto the street outside of the hospital. Knowing that you do not have the money to pay the hospital debts you come to the realization you only have 2 choices to get the money.")
        moneygainchoices = input("1. rob the old lady | 2. Talk to Gregory > ")
        print(moneygainchoices)
def moneygainchoices():
    if moneygainchoices == "1":
        print("You rob the old lady, and in her pockets and purse collectively you find 1 million dollars and a purple flower. What do you do?")
        oldladychoices = input("1. Steal the old woman's dentures | 2. Go home | 3. Go back to the hospital | 4. Talk to Gregory > ")
        print(oldladychoices)
    elif moneygainchoices == "2":
        print("You give Gregory a call, telling him that you only have a small amount of time to pay off your debts. He says to meet him in the alleyway between 64th and 63rd streets because he has an idea. What do you do?")
        GregoryChoices = input("1. Go home | 2. Go to the alleyway | 3. Go back to the hospital > ")
        print(GregoryChoices)
def oldladychoices():
    if oldladychoices == "1":
        print("You knock the old lady's dentures out, and in doing so several buff men see you and come beat you until you die from bleeding and blunt head trauma for hitting a woman.")
        start_game()
    elif oldladychoices == "2":
        print("You make it home with the money and flower, however hours later you are arrested by the police. It seems the old lady gave a scarily accurate description of you because she was a psychic. You are taken to jail and your father dies in the hospital, you know this because they attached it to a reminder to pay off your debts.")
        start_game()
    elif oldladychoices == "3":
        print("You go back to the hospital and hand over the money, however your father has already passed and there is nothing you can do about that. You go home, depressed, and eventually starve to death due to not eating out of sadness and grief for your father.")
        start_game()
    elif oldladychoices == "4":
        print("You call up Gregory, and after explaining the situation to you he tells you to meet him in the alley between 63rd and 64th KingsWay Avenue. What do you do?")
        OldLadyGregoryChoices = input("1. Meet up with Gregory | 2. Go home | 3. Go to the hospital > ")
        print(OldLadyGregoryChoices)
def GregoryChoices():
    if GregoryChoices == "1":
        print("You go home and that night you're paid a visit by Gregory. He angrily asks why you didn't meet up with him, and after failing to provide a good answer he pops a cap in you, putting you to rest with yo dad.")
        start_game()
    elif GregoryChoices == "2":
        print("You meet up with Gregory in the alleyway, and he tells you that he can lend you the money but you'll have to come work for his family in *Garbage Disposal*. Do you accept?")
        GarbageChoices = input("1. Work for the family | 2. Decline > ")
        print(GarbageChoices)
    elif GregoryChoices == "3":
        print("You go back to the hospital and give yourself up to them, selling your organs to pay off the debt and your dad is cured! Though in his grief for losing you he crashes the car, killing himself in the process.")
        start_game()
def OldLadyGregoryChoices():
    if OldLadyGregoryChoices == "1":
        print("You meet up with Gregory and he pops a cap in you, saying that he needs the money more than you do seeing as your father is already dead. The world fades to black as cops arrive on the scene.")
        start_game()
    elif OldLadyGregoryChoices == "2":
        print("You go home and go to sleep. In the night Gregory breaks into your house and robs you blind. After robbing the million dollars Gregory's men burn the house down with you in it to destroy the evidence.")
        start_game()
    elif OldLadyGregoryChoices == "3":
        print("You go to the hospital with the money and pay for the treatment. However the hospital worker notices the purple flower in your bag, which was a medicine only given to the old lady. They call the cops and you are arrested for robbery and taken to jail, where you spend the rest of your days.")
        start_game()
def GarbageChoices():
    if GarbageChoices == "1":
        print("You accept the job and Gregory's family takes care of the payments, eventually getting your father well again. You continue to work in the *Garbage Disposal* industry for Gregory and his family, however one day during a car chase you hit an old man on the side of the road. As the old man is flying through the air after the impact, you see its your father. The body crashes into a wall and you seem to have killed your father in a car crash.")
        start_game()
    elif GarbageChoices == "2":
        print("After declining Gregory's generous offer, he tells you good luck with the cops and shows you a video of you robbing the old woman. Soon the cops arrive and bring you to jail for robbery, there you rot in your cell and your father dies to the cancer.")
        start_game()
start_game()