#Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

c=word_length
while (c>0):

  guess = input("Guess a letter: ").lower()
  
  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      # print(
      #     f"Current position: {position} Current letter: {letter} Guessed letter: {guess}"
      # )
      if letter == guess:
          display[position] = letter
  
  print(display)
  
  c-=1

if "_" in display:
  print("you lost")
else:
  print("you win")