word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
random_word = random.choice(word_list)
print(random_word)

# - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = input("Guess a letter!: ")

# - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if user_guess in random_word:
    print("Correct")
else:
    print("wrong")


# - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
