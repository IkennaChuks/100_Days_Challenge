
#HINT: You can call clear() to clear the output in the console.


Bid_dict = {}
def bidding(Bidder,Amount):
  Bidder = Name
  Amount = Bid
  Bid_dict[Bidder] = Amount

while bidding:
  Name = input("What is your name?\n")
  Bid = int(input("What is your bid?\n"))
  bidding(Name,Bid)
  next = input('Are there any other bidders? type yes or no \n').lower()
  if next == 'no':
    bidding = False


  
Biggest = 0
for key in Bid_dict:
  if Bid_dict[key] > Biggest:
    Biggest = Bid_dict[key]
print(f'The Winner is {key} with a bid am ount of {Biggest}')