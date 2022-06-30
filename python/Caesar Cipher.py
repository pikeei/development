from tracemalloc import start
import art_for_cipher
print(art_for_cipher.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt(plain_text,shift_number):
#     encrypted=""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position =position+shift_number
#         encrypted+=alphabet[new_position]
#     print(f"the encrypted message would be {encrypted}")
# def decrypt (encrypted,shift_number):
#     decrypted=""
#     for letter in encrypted:
#         position = alphabet.index(letter)
#         new_decrypted_position = position-shift_number
#         decrypted+=alphabet[new_decrypted_position]
#     print(f"the decrypted message would be {decrypted}")

def caesar(start_text,shift_number,cipher_instruction):
    end_text=""
    if cipher_instruction=="decode":
            shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_number 
            end_text+=alphabet[new_position]
        else:
            end_text+=char     
    print(f"the {instruction}d is {end_text}")

caesar_cipher = False
while not caesar_cipher:
    instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("enter your message: ").lower()
    shift = int(input("whats the shift?: "))
    shift = shift % 25
    caesar(start_text=text,shift_number=shift,cipher_instruction=instruction)
    end = input("do you want to go on? Type 'yes' if you want to keep going. Otherwise, type 'no'").lower()
    if end=="yes":
        caesar_cipher= False 
    elif end=="no":
        caesar_cipher= True