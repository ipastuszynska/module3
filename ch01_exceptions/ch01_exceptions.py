# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:34:09 2019

@author: iza
"""
#--------------------------------------------------
#TASK 1: Run the code and see if the error message changed.
#--------------------------------------------------


#
#try:
#    f = open('testfile')
#except Exception:
#    print('Error!')
#    
#    
#try:
#    f = open('testfile')
#except Exception:
#    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")
#    
#
#try:
#    f = open('testfile.txt')
#except Exception:
#    print('Error!')
    
    
#--------------------------------------------------
#TASK2: Multiple errors
#--------------------------------------------------
    
##try:
##    f = open('testfile.txt')
##    s1 = not_exsit
##except Exception:
##    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")


# It still prints the same error message you wrote before, although the open file function has passed correctly.
# In this case we can use specific exceptions to filter out the error reporting process: e.g. change ‘Exception’ to ‘FileNotFoundError’.

#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")
    
#try:   
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
#except Exception:
#        print('Sorry. Something is wrong after opening function.')

#--------------------------------------------------
#BUILT IN EXCEPTIONS
#--------------------------------------------------

# print(math.sqrt(-1)) is a ValueError.
# 1+2+’three’ is a TypeError.
# 1/0 is a ZeroDivisionError.
# For i in range (5), forget ‘:’ is a SyntaxError.

# Exception is actually an object in Python


#--------------------------------------------------
#TASK 3:  Try the code below to see what is printed out to your console, can you think of other examples? Have a play with it.
#--------------------------------------------------
print("TASK3")
        
try:
    f = open('testfile.txt')
    s1 = not_exsit
except Exception as e:
    print(e)   
        
print()

#--------------------------------------------------
#TASK 4: Run the corrected code below and see what happens.
# -> The else clause will be executed if the try block does not raise an exception.
#--------------------------------------------------
print("TASK4")
try: 
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
print()

#--------------------------------------------------
#BLOCK
#--------------------------------------------------

#--------------------------------------------------
#TASK 5: You can try both code blocks (with error and without error) below to test out the finally block:        
#--------------------------------------------------       
print("TASK 5")
        
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executing finally…')
print()
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executing finally…')
print()

# else will execure if no exceptions 
#error or not, the finally block will always execute
#--------------------------------------------------   
# MANUAL EXCEPTIONS 
#--------------------------------------------------   
    
 
#If you would like to further test your code within the development code, you can manually raise an exception or set a boolean to check your code
    
    

#--------------------------------------------------    
#Task 6: Try the code below:
#-------------------------------------------------- 
print("TASK 6")
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print('file name are the same')
