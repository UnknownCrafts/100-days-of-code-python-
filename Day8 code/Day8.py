#Caesar Cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat_flag = True

print(art.logo)
print("")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
print("")
text = input("Type your message:\n").lower()
print("")
shift = int(input("Type the shift number:\n")) % 26
print("")

def caesar(text, shift, direction):
    output_text = ""
    is_encoding = direction == "encode"
    
    for char in text:
        is_alphabet = char in alphabet
        
        if is_alphabet:
            index = alphabet.index(char)
            
            if is_encoding:
                if index + shift > 25:
                    output_text += alphabet[(index + shift) - 26]
                else:
                    output_text += alphabet[index + shift]
            else:
                output_text += alphabet[index - shift]
        else:
            output_text += char
    
    print(f"The {direction}d text is {output_text}")
    
    return output_text

caesar(text, shift, direction)

print("")
user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower().strip()
print("")

if user_input == "yes":
    repeat_flag = True
else:
    repeat_flag = False

while repeat_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    print("")
    text = input("Type your message:\n").lower()
    print("")
    shift = int(input("Type the shift number:\n")) % 26
    print("")
    
    caesar(text, shift, direction)
    
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower().strip()
    print("")

    if user_input == "yes":
        repeat_flag = True
    else:
        repeat_flag = False

print("Goodbye")