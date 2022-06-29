import random
import string

words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act","action","activity","actor","actually"]

word_to_guess = random.choice(words)
tried_letters = []
letter_in_word = []
display = "_"*len(word_to_guess)
life = len(word_to_guess)

while display != (" ".join([letter for letter in word_to_guess])) and life != 0:
  new_try = input(f"You have {life} tries. Essayez une autre lettre : ")
  if not new_try or new_try not in string.ascii_letters:
    print("You need to give a letter")
    continue
  if new_try in tried_letters:
    print("You have already tried that letter.")
    continue
  if not new_try in word_to_guess:
      life -= 1
  tried_letters.append(new_try)
  for letter in word_to_guess:
    if letter in tried_letters:
      letter_in_word.append(letter)
    else:
      letter_in_word.append("_")
  display = " ".join(letter_in_word)
  letter_in_word = []
  print(display)
if display == (" ".join([letter for letter in word_to_guess])):
  print("Congrats, you found the word.")
elif life == 0:
  print(f"You lost. The word was {word_to_guess}")
  
