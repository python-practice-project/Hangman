# Hangman
import random
from art import logo, stages
from list import word_list

print(logo)


#challange - 1
'''word_list = ["apple", "mango", "banana"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Enter a letter: ").lower()
print(guess)
for letter in chosen_word:
    print(letter)
    if letter == guess:
        print("yes")
    else:
        print("no")'''
    
#challange - 2
'''word_list = ["apple", "mango", "banana"]
chosen_word = random.choice(word_list)
length = len(chosen_word)
print(length)
(print(f'Pssst, the solution is {chosen_word}.'))
display = []
for letter in chosen_word:
    display += "_"
print(display)
guess = input("Enter a letter: ").lower()
print(guess)
for position in range(length):
    letter = chosen_word[position]
    print(letter)
    if letter == guess:
        display[position] = letter
print(display)'''

#challange - 3
'''word_list = ["apple", "mango", "banana"]
chosen_word = random.choice(word_list)
length = len(chosen_word)
print(length)
(print(f'Pssst, the solution is {chosen_word}.'))
display = []
for letter in chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Enter a letter: ").lower()
    print(guess)
    for position in range(length):
        letter = chosen_word[position]
        print(letter)
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")'''

#challange - 4

chosen_word = random.choice(word_list)
length = len(chosen_word)
print(length)
(print(f'Pssst, the solution is {chosen_word}.'))
display = []
for letter in chosen_word:
    display += "_"
print(display)
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Enter a letter: ").lower()
    print(guess)
    for position in range(length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
            lives -=1
            print(lives)
            if lives == 0:
                print("You lose.")
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])