import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

chosen_word = random.choice(word_list)

number_blanks = len(chosen_word)
blanks = []
for blank in range(number_blanks):
    blanks.append("_")

def display(blanks):
    blanks_string = " ".join(blanks)
    print(blanks_string)

def check_guess(guess,chosen_word,blanks):
    success = 0 
    for char in range(len(chosen_word)):
        if guess == chosen_word[char]:
            success += 1
            blanks[char] = guess
    return success, blanks

print(logo)

print(stages[lives])
display(blanks)

success_counter = 0
user_guesses = []
while (success_counter < number_blanks) and (lives > 0) :
    guess = input("Guess a letter: ").lower()
    if guess in user_guesses:
        print("You already guesses this letter. Try another letter")
    else: 
        user_guesses.append(guess)
        success, blanks = check_guess(guess,chosen_word,blanks)
        if success > 0:
            success_counter += success
        else:
            lives -= 1
            print("Your guess "+guess+" is not in the word. Try another letter")
        print(stages[lives])
        display(blanks)


if success_counter == number_blanks:
    print("You have won! Congrats!")
elif lives == 0:
    print("You lose :( Try again")

