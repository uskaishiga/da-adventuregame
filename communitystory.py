import time
import random

def intro():
    print("Welcome to the Adventure: Escape from Dora's Drug Cartel!")
    print("You find yourself trapped in the midst of Dora the Explorer's drug cartel.")
    print("Your mission is to escape before it's too late!")
    print("You have to make the right choices to survive. Good luck!\n")

def choose_path():
    print("Which path will you choose?")
    print("1. Sneak out quietly through the back door.")
    print("2. Confront Dora and negotiate your way out.")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def sneak_out():
    print("\nYou quietly sneak out through the back door...")
    time.sleep(2)
    print("As you tiptoe your way, you suddenly step on a squeaky toy!")
    time.sleep(2)
    print("The noise alerts Dora's guards, and they catch you!")
    game_over()

def confront_dora():
    print("\nYou decide to confront Dora and negotiate...")
    time.sleep(2)
    print("Dora seems amused by your courage.")
    time.sleep(2)
    print("She offers you a deal: If you can solve her riddle, she'll let you go.")
    time.sleep(2)
    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
    answer = input("What's your answer? ").lower()
    if answer == "echo":
        print("Congratulations! You've solved Dora's riddle.")
        print("Dora honors her word and lets you go free.")
        print("You've successfully escaped from Dora's drug cartel. Well done!")
        play_again()
    else:
        print("Incorrect answer! Dora's patience wears thin.")
        print("She orders her guards to capture you!")
        game_over()

def game_over():
    print("\nGAME OVER")
    print("Would you like to play again?")
    play_again()

def play_again():
    choice = input("Enter 'yes' to play again, or 'no' to quit: ").lower()
    if choice == "yes":
        play_game()
    elif choice == "no":
        print("Thanks for playing! Goodbye.")
        exit()
    else:
        print("Invalid choice!")
        play_again()

def play_game():
    intro()
    path = choose_path()
    if path == "1":
        sneak_out()
    elif path == "2":
        confront_dora()
    else:
        print("Invalid choice! Try again.")
        play_game()

def main():
    play_game()

if __name__ == "__main__":
    main()
