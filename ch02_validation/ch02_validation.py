# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:05:11 2019

@author: iza
"""

#-------------------------------------------
#TASK 1: Do you remember how to ask user input with a pre-coded new line or with a space in front?
#TASK 2: Cast age to int data type.
#-------------------------------------------


##With a new line:
#print ("What’s your age?")
#age = int(input())
##or this age = input()  / age_int = int(age)
#
##With a space:
#Age = int(input("What’s your age? "))


#-------------------------------------------
#TASK 3: Try the code below in a python file:
#-------------------------------------------
    
    
#Option = input("Please input yes or no ").lower()


#-------------------------------------------
#TASK 4: An example for validating string length
#-------------------------------------------

#Option = input("Please input yes or no ").lower()
#print(len(Option))

#if len(Option) == 2 or len(Option)==3:
#    print ("yay!")
#else:
#    print ("nay!!!")



#if 2 <= len(Option) < 4:
#    print ("yay!")no
#else:
#    print ("nay!!!")
#    print ("try again")
#    Option = input("Please input yes or no ").lower()


#-------------------------------------------
#TASK 5: Cehcking input - while loop
#TASK 6: think about which loop the break statement is breaking and at which stage of the code?
#-------------------------------------------


#print("***choice****")
#print("1. Display my name")
#print("2. Display my age")
#print("3. Display my city")
#choice = int(input("What is your choice? "))
#
#if choice == 1:
#    print("Z")
#elif choice == 2:
#    print("5 years old")
#elif choice == 3:
#    print("London")
#
#
#
##while choice < 1 or choice > 3:
##    choice = int(input("What is your choice? "))
#
#
#while True:
#    try:
#        while choice< 1 or choice > 3:
#            choice = int(input('What is your choice?'))
#            break
#    except ValueError:
#        print('please type a number! ')
#        
        
        
        
        
#-------------------------------------------
#TASK 7: Think about how you will write this code based on the description?
#In a scenario where you would not want the description of a Spam to be empty and an input value must be greater than zero, you can write some validation as (validate those values passed to the constructor).
#-------------------------------------------
        
class Spam(object):
    def __init__(self, description, value):
        if not description or value <=0:    
            raise ValueError
        self.description = description
        self.value = value
        

s = Spam("c", 5)

#assert version
  
class Spam2(object): 
    def __init__(self, description, value): 
        assert description != "" 
        assert value > 0 
        self.description = description 
        self.value = value
s = Spam2("c", -5)