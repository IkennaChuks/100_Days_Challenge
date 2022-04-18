#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level =  input('Choose a difficulty. Type "easy" or "hard": ').lower()
Number = random.randint(1,100)
attempts = 0
if level == 'easy':
  attempts = 10
else:
  attempts = 5

def Guess():
  global attempts
  print(f'You have {attempts} attempts remaining to guess the number')
  guess = int(input('make a guess: '))
  if attempts < 2:
    print(f'Game Over, you have {attempts-1} attempts')
    return True
  elif guess > Number:
    print('Too high.\nGuess again.')
    attempts = attempts - 1
    return False
  elif guess < Number:
    print('Too low.\nGuess again.')
    attempts = attempts - 1
    return False
  else:   
    print('You guessed correctly')
    return True

start_guess = True
while start_guess:
  status = Guess()
  if status == True:
    start_guess = False
  