word_list = ["aardvark", "baboon", "camel"]
display = []
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
random_word = random.choice(word_list)
print(random_word)

# - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guesses = ["_"] * len(random_word)

for _ in range(len(random_word)):
    display += "_"
print(display)
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = input("Guess a letter!: ")

# - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(random_word)):
    letter = random_word[position]
    if letter == user_guess:
        display[position] = letter

# - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
