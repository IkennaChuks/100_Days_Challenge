rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n'))
Computer = random.randint(0,2)
print(Computer)

if choice == 0 and Computer == 2:
  print(f'You chose rock {rock}')
  print(f'Computer chose Scissors {scissors}')
  print('You win')
elif choice == 0 and Computer == 1:
  print(f'You chose rock {rock}')
  print(f'Computer chose Paper {paper}')
  print('You lose')
elif choice == 0 and Computer == 0:
  print(f'You chose rock {rock}')
  print(f'Computer chose rock {rock}')
  print('Draw')
elif choice == 1 and Computer == 0:
  print(f'You chose paper {paper}')
  print(f'Computer chose rock {rock}')
  print('You Win')
elif choice == 1 and Computer == 2:
  print(f'You chose paper {paper}')
  print(f'Computer chose scissors {scissors}')
  print('You Loose')
elif choice == 1 and Computer == 1:
  print(f'You chose paper {paper}')
  print(f'Computer chose paper {paper}')
  print('Draw')
elif choice == 2 and Computer == 1:
  print(f'You chose scissors {scissors}')
  print(f'Computer chose paper {paper}')
  print('You Win')
elif choice == 2 and Computer == 0:
  print(f'You chose scissors {scissors}')
  print(f'Computer chose rock {rock}')
  print('You Loose')
else:
  print(f'You chose scissors {scissors}')
  print(f'Computer chose scissors {scissors}')
  print('Draw')