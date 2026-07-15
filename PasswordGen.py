import random
# 1. ALPHABETS
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# 2. NUMBERS (as strings to preserve formatting/leading zeros if needed)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 3. COMMON SYMBOLS
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~'
]
PassList=[]
NumL=int(input("How many letters do you want?"))
NumS=int(input("How many symbols do you want?"))
NumN=int(input("How many numbers do you want?"))
for i in range(0,NumL):
    PassList.append(random.choice(alphabets))
for i in range(0,NumS):
    PassList.append(random.choice(symbols))
for i in range(0,NumN):
    PassList.append(random.choice(numbers))
    random.shuffle(PassList)
password="".join(PassList)
print(f"Your password is:{password}.")



