alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift_amount) % 26
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

def user_inputs():
  end_of_session = False
  direction_checker = False
  next_step = False
  while direction_checker == False and end_of_session == False and next_step == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "decode" or direction == "encode":
       direction_checker = True
       next_step = True
    else:
      direction_checker = False
  while end_of_session == False and direction_checker == True and next_step == True:
    next_step = False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    continue_process = input("Type 'yes' or 'y' if you want to go again, otherwise type 'no' or 'n'.\n").lower()
    if continue_process == 'yes' or continue_process == 'y':
      user_inputs()
    else:
      print("Goodbye!")
      end_of_session = True

user_inputs()