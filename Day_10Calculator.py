def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2


calc = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for key in calc:
  print(key)
operation = input("Pick an operation from the line above: ")
function = calc[operation]
Ans = function(num1,num2)
print(f'{num1} {operation} {num2} = {Ans}')

calculating = True
while calculating :
  status = input("Do you want to perform another operation? type yes or no ").lower()
  if status == 'no':
    calculating = False
  else:
    operation = input("Pick another operation: ")
    num3 = int(input("What's the second number?: "))
    function = calc[operation]
    result = function(Ans,num3)
    print(f'{Ans} {operation} {num3} = {result}')

  
