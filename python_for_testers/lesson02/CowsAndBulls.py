import random
#Source:https://www.practicepython.org/solution/2014/07/18/18-cows-and-bulls-solutions.html
def compare_numbers(number, user_guess):
    cowbull = [0, 0]  # cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


def helper():
    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")


playing = True  # gotta play the game
number = str(random.randint(1, 9999))  # random 4 digit number
guesses = 0

while playing:
    user_guess = input("Give me your best guess!\n")
    if user_guess == "exit":
        break
    if user_guess == "cheat":
        print("Answer is :", number)
        continue
    if user_guess == "help":
        helper()
    if (len(user_guess) != 4):
        print("invalid input...please provide a 4 digit number!")
        continue
    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1
    print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
    if cowbullcount[1] == 4:
        print("You win the game after " + str(guesses) + "! The number was " + str(number))
        print("Generating a new number now!")
        number = str(random.randint(1, 9999))  # random 4 digit number
        guesses = 0
        print("You can exit by typing 'exit'")
    else:
        print("Your guess isn't quite right, try again.")
