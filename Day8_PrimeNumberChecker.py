#Write your code below this line 👇
def prime_checker(number):
  for num in range(2,number):
    if number % num == 0  :
      print("It's not a prime number")
      break
    else:
      print("It's a prime number")
      break

n = int(input("Check this number: "))
prime_checker(number=n)



