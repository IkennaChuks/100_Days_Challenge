# Split string method
#Write a code to randomly determine who will pay the bill from a list of friends.

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

import random

No_Of_Friends = len(names)
RandomNo = random.randint(0,No_Of_Friends-1)
Payer = names[RandomNo]
print(f'{Payer} is going to buy the meal today!')




