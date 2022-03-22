print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

# Small pizza: $15
# Medium pizza : $20
# Large Pizza : $25

# Pepperoni for small Pizza $2 for Medium and Large $3
# Chesse for any Pizza $1

Bill = 0

if size == 'l':
  Bill += 25
  if add_pepperoni == 'y':
    Bill += 3
  else:
    Bill  
elif size == 'm':
  Bill +=20
  if add_pepperoni == 'y':
    Bill += 3
  else:
    Bill 
else:
  Bill +=15
  if add_pepperoni == 'y':
    Bill += 2
  else:
    Bill 

if extra_cheese == 'y':
  Bill += 1

else:
  Bill

print(f'Your final bill is ${Bill}')





