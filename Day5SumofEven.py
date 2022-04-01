SumOfEven = 0
for Number in range(0,101):
  if Number % 2 == 0:
    SumOfEven += Number
print(f'The sum of Even numbers between 1 and 100 is {SumOfEven}')