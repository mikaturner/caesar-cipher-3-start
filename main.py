alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

i= 0
mess_list_indexes = []
en_de_list_indexes = []
en_de_message = []  

def caesar(text, shift, direction):
    if direction == "encode" or direction == "decode":
        for character in text:
          if character in alphabet:
              i = alphabet.index(character)
              mess_list_indexes.append(i)
          else: 
              mess_list_indexes.append(character)
    else:
         print("You did not enter a valid choice.  Please enter 'encode' or 'decode'")

    for character in mess_list_indexes:
        if type(character) == int:
            if direction == "encode":
                number_shift = character + shift
                if number_shift <= 25:
                    en_de_list_indexes.append(number_shift)
                else:
                    number_shift -= 26
                    en_de_list_indexes.append(number_shift)
            elif direction == "decode":
                number_shift = character - shift
                if number_shift >=0:
                    en_de_list_indexes.append(number_shift)
                else:
                    number_shift += 26 
                    en_de_list_indexes.append(number_shift)
        else: en_de_list_indexes.append(character)
  
  #creates a list with the shifted message
    for character in en_de_list_indexes:
        if type(character) == int:
            en_de_message.append(alphabet[character])
        else: 
            en_de_message.append(character)
    print(f"The {direction} text is: {''.join(en_de_message)}")
    
caesar(text, shift, direction)
