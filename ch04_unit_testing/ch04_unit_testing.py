# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:23:44 2019

@author: iza
"""

#----------------------------------------------
#TASK1:  1: Think about how you would write a function to check if the input number is a prime number?
#---------------------------------------------

#def is_prime(number): 
#    """Return True if *number* is prime."""    
#    for element in range(number): 
#        if number % element == 0: 
#            return False 
#        return True 
    
def print_next_prime(number): 
    """Print the closest prime number larger than *number*.""" 
    index = number 
    while True:
        index += 1 
        if is_prime(index): 
            print(index)


#----------------------------------------
#TASK 2: Prime take 2
#----------------------------------------  
            
def is_prime(number): 
    """Return True if *number* is prime.""" 
    if number > 1: 
        for element in range(2, number): 
            print(number, element) 
            if number % element == 0: 
                return False 
        return True
        
#is_prime(4)


#----------------------------------------
# Task 3 - Prime take 3
#----------------------------------------  

    
def is_prime(number):
    """Return True if *number* is prime.""" 
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True 


