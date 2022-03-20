# Tip Calculator calculates tips.
print('welcome to the tip calculator.')
bill = float(input('what was the total bill? $'))
people = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
tip = (tip + 100)/100
bill = bill * tip
charge = round(bill / people)
print('Each person should pay $'+ str(charge))