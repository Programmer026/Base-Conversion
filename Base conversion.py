#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:18:47 2020

@author: oluwayemisirunsewe
Title: Base Conversion
Decription: This Program Helps to convert number from one base to another
Inspiration: I got this idea from my first class in Computer Organization 
where we were talking about binary, octal, Decimal, Hexadecimal.
"""

"""
@parameter: The number to convert, The base of the number to be converted, Count to keep track of how many recursion steps
@returns: it returns a number in base 10
"""
def toDecimalConvertion(number, oldbase, count):
    if(number == 0):
        return 0
    return ((number%10) * (oldbase**count)) + toDecimalConvertion(number//10, oldbase, count+1)
   
    
"""
@parameter: The number to convert, The base of the number to be converted to
@returns: it returns a String containing numbers in the base specified
"""    
def toBaseConversion(number, newBase):
    if(number == 0):
        return ""
    return str(toBaseConversion(number//newBase, newBase)) + str(number%newBase)
    
"""
@parameter: Any number, the base of the number
@returns: True or False depending of if the number is truly in that base
@decription: if any number in the number passed to the function is equal to or graeter than the base it will return false
"""
def verifyBase(number, base):
    for i in str(number):
        if(int(i) >= base):
            print(number, "is not in base", base)
            return False
    return True
    
"""
@parameter: Any number
@returns: True or False depending of if the number is truly in that base
"""
def verifyBaseDecimal(number):
    if not(number.isnumeric()):
         print(number, "is not in base 10")
         return False
    return True

#Ask user for input
prompt = input("Would you like to use Yemi Base coonversion program\nPlease enter Yes or No: ").lower()

#While the user still wants to use the program
while(prompt == "yes"):
    #Prompts the user for option to select
    options = int(input("Select 1 to convert to Decimal\nSelect 2 to convert from a decimal to a base\nSelect 3 to convert from a base to a new base: "))
    #If the user choses to convert from one base to another
    if(options == 3):
        numToBeConverted = int(input("Please the number you want to convert: "))
        old_base = int(input("Please enter the base of the number you want to convert: "))
        new_base = int(input("Please enter the base you want to convert to: "))
        verification = verifyBase(numToBeConverted, old_base)
        if(verification == True):
            toDecimal = toDecimalConvertion(numToBeConverted, old_base, 0)
            print(numToBeConverted, "in base", old_base, "is", toBaseConversion(toDecimal, new_base), "in base", new_base)
    
    #If the user chooses to convert from a base to decimal
    elif(options == 1):
        numToBeConverted = int(input("Please the number you want to convert: "))
        old_base = int(input("Please enter the base of the number you want to convert: "))
        verification = verifyBase(numToBeConverted, old_base)
        if(verification == True):
            print(numToBeConverted,  "is", toDecimalConvertion(numToBeConverted, old_base, 0), "in base 10")
    
    #If the user chooses to convert from a decimal to any base
    elif(options == 2):
        numToBeConverted = int(input("Please the number you want to convert: "))
        new_base = int(input("Please enter the base you want to convert to: "))
        verification = verifyBaseDecimal(str(numToBeConverted))
        if(verification == True):
           print(numToBeConverted,  "is", toBaseConversion(numToBeConverted, new_base), "in base", new_base)
    else:
        print("You have entered an invalid number!")
    
        
        
    prompt = input("Would you like to use Yemi Base coonversion program again\nPlease enter Yes or No: ").lower()

#Ending Statement
print("\nThank you for using my Base Convertion. GoodBye!!!")

"""print(toDecimalConvertion(101,2,0))
print(toBaseConversion(5,3))
print(verifyBase(1031,2))"""