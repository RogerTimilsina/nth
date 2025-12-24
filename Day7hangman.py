import random
from Day7hangman_materials import word_list, logo, stages

chosen_word = random.choice(word_list).lower()

print(logo)

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6
end_of_game = False
word_length = chosen_word.__len__()

# Create blanks
display = []
for i in range(word_length):
    display += "_"

print(display)
print(stages[lives])
while not end_of_game:
    guess = input("Guess a letter :\n").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")
    else:
        for j in range(0, word_length):
            if guess == chosen_word[j]:
                display[j] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"You have guessed the letter {guess}. That's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The correct word is {chosen_word}")

    print(stages[lives])

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("You win")
