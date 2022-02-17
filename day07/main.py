from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo3)
print("\nTo win, guess the word before the person is hung.\n")

display = []
wrong_guesses = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()

    clear()

    if guess in wrong_guesses:
      print(f"{' '.join(display)}")
      print(stages[lives])
      print(f"You've already guessed with the letter '{guess}', pick another letter.")
    else:
      wrong_guesses.append(guess)

      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      print(f"{' '.join(display)}")

      if "_" not in display:
          end_of_game = True
          print("\nGeninus, genius, genius! You won!")
          print(logo2)

      if guess not in chosen_word:
        lives -= 1

      if not end_of_game:
        print(stages[lives])
        if guess not in chosen_word:
          print(f"'{guess}' is not in the word, you lost 1 life.")

      if lives == 0:
        end_of_game = True
        print("The man has been hung, you lose.")
        print(f"\nThe word was '{chosen_word}'")
