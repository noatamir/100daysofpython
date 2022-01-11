#Number Guessing Game Objectives:

from art import logo
import random

print(logo)

def set_difficulty():
    mode = input("Would you like to play in easy or hard mode? (easy/hard): ")
    if mode == "easy":
        attempts = 10
    elif mode == "hard":
        attempts = 5
    else:
        print("you can only answer 'easy' or 'hard'")
        set_difficulty()
    return attempts, mode

def check_guess(goal):
    attempt = int(input("Make a guess: Guess a number between 1 and 100: "))
    if attempt == goal:
        print(f"You got it! The answer was {goal}")
        return True
    elif attempt > goal and attempt < 100:
        print("Too high. \nGuess again.")
    elif attempt < goal and attempt > 1:
        print("Too low. \nGuess again.")
    else:
        print("You need to guess a number between 1 and 100")
        check_guess()


def guess(attempts, goal):
    print(f"You have {attempts} attempts remaining to guess the number")
    game_over = check_guess(goal)
    attempts -= 1
    if game_over != True and attempts == 0:
        print("You ran out of turns :(")
        game_over = True
    elif game_over != True:
        game_over = False
    return game_over, attempts

def game():
    game_over = False
    goal = random.randint(1, 100)
    #print(f"the number is {goal}")
    attempts, mode = set_difficulty()
    print("I'm thinking of a number between 1 and 100.")
    while game_over == False:
        game_over, attempts = guess(attempts, goal)


game()

# If they run out of turns, provide feedback to the player. 
