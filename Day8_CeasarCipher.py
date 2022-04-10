alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(text,shift,direction):
  word = ''
  shift = shift % 26 
  if direction == 'encode':
    for letter in text:
      if letter not in alphabet:
        word+= letter
      else:
        index =  alphabet.index(letter)
        newindex = index + shift
        word += alphabet[newindex]
    print(f'The encoded text is {word}')
  else :
    for letter in text:
      if letter not in alphabet:
        word+= letter
      else:
        index =  alphabet.index(letter)
        newindex = index - shift
        word += alphabet[newindex]
    print(f'The decoded text is {word}')

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceasar(text,shift,direction)
  flag= input('Do you want to play again yes or no \n')
  if flag == 'no':
    should_continue = False
    print('GoodBye!!!')
