import math
from pickle import TRUE
from _ast import In

# print('hello world')
# print('*'*10)
#
# Using input method getting data from prompt(input method returns string even number given
# name = input("What is your name? ")
# print('Hi '+name)
# colour = input("What is your favourite colour? ")
# print(name+' likes '+colour)

#type casting and finding type of variable
# birth_year = input('Enter year of birth')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)

#String usage
# course = 'Python for programming'
# another = course[:7] #from 0 to 7th character
#course[0:-1] #from zero character to last but one character, '-' represents from end of the string.
# print(another)

#Format string
# first ='john'
# last = 'smith'
# message = first + ' ['+last+'] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)


#String methods
# cource = 'Python for Beginners'
# print(len(cource)) #For length of the string
#
# print(cource.upper()) #To convert all characters uppercase and returns new string as java
#
# print(cource.lower()) #To convert all characters to lowercase and returns a new string as java
#
# print(cource)
#
# print(cource.find('P')) #To find the position of given character and return the index
#
# print(cource.find('Beginners')) #To find the position of the sequence of a characters in a given string and return index
#
# print('Python' in cource) #in used to find sequence for character present in given string. Returns boolean value.

#arithmatic operators
# print(10 + 3) #addition operator
# print(10 -3)  #subtraction operator
# print(10 / 3) #division operator returns float value
# print(10 // 3) # division operator returns int value
# print(10 % 3) #percentile operator return reminder value
# print(10 ** 3) #exponential operator

#augment operator
# x = 10
# x += 3
# print(x)

#mathematic operators
# a=1,2,3
# print(math.ceil(2.8)) #To round of the precision value
# print(math.floor(2.9)) #To round of to previous value
# print(math.factorial(5)) #To find the factorial value
# print(math.fabs(-2.9)) #To get absolute value
# print(math.fsum(a)) #To add the array of values
# To further more math functions, go through the following link
#https://docs.python.org/3/library/math.html


#Pragraphed string values
# value = ''' 
# Hi Santhosh
#
# Believe your doing good. 
# Expext to meet as soon as possible.
#
# Thanks and regards
# Your beloved friend.
# '''
#
# print(value)

#if elseif else stament

# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
# elif is_cold:
#     print("It's cold day")
# else:
#     print("It's a lovely day")
# print('Enjoy your day')
#
# price = 1000000
# has_good_credit = False
#
# if has_good_credit:
#         down_payment = price * 0.1
# else:
#     down_payment = price * 0.2
# print(f'Down payment for the property is: ₹{down_payment}')

#Logical operators

# has_good_credit = True
# has_criminal_record = False
#
# if has_good_credit and not has_criminal_record:
#     print('Eligible for loan')

#Comparision operators

# name = 'aded'
#
# if len(name)<3:
#     print('Name should be atleast 3 characters')
# elif len(name)>50:
#     print('Name should be less than 50 characters')
# else:
#     print('Name looks good')    

# Simple program to convert weight from pounds to kgs and vice versa

# weight = input('Enter your wieght: ')
# unit=input('(L)bs or (K)g: ')
#
# if unit.upper() == 'L':
#     converted = int(weight) * 0.45
#     print(f'Weight in KGs is {converted}')
# elif unit.upper() == 'K':
#     converted = int(weight) / 0.45
#     print(f'Weight in LBS is {converted}')
    
#While loop

# i =1
# while i<=5:
#     print('*' * i)
#     i = i+1
# print('Done')

#program for guess number using while loop

# secret_number = 7
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else: 
#     print('Sorry, you lost!')

#car program using while loop

# started = False
# while True:
#     command = input('> ').lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car is started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "quit":
#         break
#     elif command == "help":
#         print("""
#         start - to start a car
#         stop - to stop the car
#         quit - to quit
#         """)
#     else:
#         print("Sorry, I don't understand that")

#For loop

# for item in range(10):  # range(10) from 0 -9, range(2,10) starts from 2 and end to 9, range(2,10,2) starts from 2 ends at 9 and different from values are 2
#     print(item)

#program addition of array

# price = 10,20,30
# total=0
#
# for item in price:
#     total +=item
# print(f"Total price is: {total}")

#Nested loops

for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")
    
numbers = [5,2,5,2,2]

for x_count in numbers:
    output = ""
    for x in range(x_count):
        output += 'x'
    print(output)
