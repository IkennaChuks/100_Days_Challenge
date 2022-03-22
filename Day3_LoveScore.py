# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

Full_name = name1 + name2
t = int(Full_name.count('t'))
r = int(Full_name.count('r'))
u = int(Full_name.count('u'))
e = int(Full_name.count('e'))

Full_name_true = str(t+r+u+e)

l = int(Full_name.count('l'))
o = int(Full_name.count('o'))
v = int(Full_name.count('v'))
e = int(Full_name.count('e'))
Full_name_love = str(l+o+v+e)
Love_score = int(Full_name_true + Full_name_love)

if Love_score < 10 or Love_score > 90:
  print(f'Your score is {Love_score}, you go together like coke and menthos.')
elif Love_score >= 40 or Love_score <= 50:
  print(f'Your score is {Love_score}, you are alright together.')
else:
  print(f'Your score is {Love_score}.')
