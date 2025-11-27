# def decrypt(org_text, shift_amt):
#     decoded_text = ''
#     for i in org_text:
#         shifted_pos = alphabet.index(i) - shift_amt
#         if shifted_pos < 0:
#             shifted_pos = 26 - abs(shifted_pos)       (we can use -> shifted_position %= len(alphabet)  here too
#                                                       instead of lines 5, 6 as .eg. -2 % 25 returns 23)
#         decoded_text += alphabet[shifted_pos]
#     print(f"Decoded text is : {decoded_text}")
#
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# This single function does the work of two above functions

def cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


logo = """           
         ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
        a8"     ""  ""     `Y8  a8P_____88  I8[    88  ""     `Y8  88P'   "Y8  
  %     8b    /     ,adPPPPP88  8P           `"Y8ba,   ,adPPPPP88  88              ^      
        "8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88     !     
     .   `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'   OYbbdP"/   `"8bbdP"Y8 88 
           +              #                  &             @                 $
   *          !                $     88           ?             %         
         ~          08       .       88     ,       !                   ) 
           ,                    *    88         .           +            
   !     ,adPPYba,  00  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,           >  
        a8"     ""  88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8    
        8b          88  88       d8  88       88  8PP"""""""  88              `
     .  "8a,   ,aa  88  88b,   ,a8"  88   (   88  "8b,   ,aa  88    $      
         `"Ybbd8"'  00  88`YbbdP"'   88       88   `"Ybbd8"'  88          
 @           -         88                               )                 %
                   ?   88           +
         """
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt(Without any spaces):\n").lower()

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

# 3vkoknukpc@FAM