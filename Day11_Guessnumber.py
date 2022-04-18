#Number Guessing Game Objectives:
import random
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
  if guess > Number:
    print('Too high.\nGuess again.')
    attempts = attempts - 1
    return False
  elif guess < Number:
    print('Too low.\nGuess again.')
    attempts = attempts - 1
    return False
  else:   
    print(f'You got it, the answer was {Number}')
    return True

start_guess = True
while start_guess:
  status = Guess()
  if status == True:
    start_guess = False
  