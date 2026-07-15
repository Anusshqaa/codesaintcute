# 1. Write a python program to add two numbers.
# 2. Write a python program to find remainder when a number is divided by z.
# 3. Check the type of variable assigned using input() function.
# 4. Use comparison operator to find out whether ‘a’ given variable is greater than ‘b’ or not.
# Take a = 34 and b = 80
# 5. Write a python program to find an average of two numbers entered by the user.
# 6. Write a python program to calculate the square of a number entered by the user.

#SOLUTIONS

#1. 
# num1=int(input("Enter num: "))
# num2=int(input("Enter num: "))
# print(f"The sum is {num1+num2}")

#2
# divid=int(input("Enter num that is to be divided: "))
# div=int(input("Enter num that divides: "))
# print(f"The remainder is {divid % div}")

#3
# userInput=input("Enter a data: ")
# print(type(userInput))

#4
# a = 34 
# b = 80
# print(a>b)
# print(a<b)

#5
# num1=int(input("Enter num: "))
# num2=int(input("Enter num: "))
# print(f"The average is {(num1+num2)/2}")

#6
# num1=int(input("Enter num: "))
# print(f"The square of {num1} is {num1**2} ")


# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.


#SOLUTIONS


#2. 
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# name=input("Enter name: ")
# date=input("Enter date: ")
# letter=letter.replace("<|Name|>", name)
# letter=letter.replace("<|Date|>", date)
# print(letter)

#3
# text = "This string contains  double spaces."
# DetectSpace=text.find("  ")
# if DetectSpace != -1 :
#     print(f"Detected at {DetectSpace}")
# else:
#     print("Not Detected")

#4
# text = "This string contains  double spaces."
# NewTxt=text.replace("  ", " ")
# print(NewTxt)
