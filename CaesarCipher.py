alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, key, operation):
    output = ""
    if operation == "decode":
        key = key * -1
        
    for letter in message:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + key
            shifted_position = shifted_position % len(alphabet)
            output += alphabet[shifted_position]
        else:
            output += letter
            
    print(f"Here is the {operation}d text: {output}")

should_continue = True 
while should_continue:
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    secret_message = input("Type your message here:\n").lower()
    
    key = int(input("Enter the key:\n"))  
    
    if encode_or_decode in ["encode", "decode"]:
        caesar(message=secret_message, key=key, operation=encode_or_decode)
    else:
        print("Invalid choice! Please type 'encode' or 'decode'.")
        
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False 
        print("Goodbye!")
