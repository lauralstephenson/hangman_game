from replit import clear
import random
from hangman_words import word_list
#This is a hangman game I learned in the 100 Days of Code class.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  #clear the game in between rounds
  clear()

  if guess in display:
    print(f"You've already guessed {guess}")
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    #the next line is used for testing purposes only
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  #Check if user is wrong.
  if guess not in chosen_word:
    print(f"The letter {guess} is not in the word. You lose a life!")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")

  from hangman_art import stages
  print(stages[lives])
