# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:16:50 2018

@author: iza
"""
"""Module 2 - Wk 6. Design a simple program."""
"""(8) Mobile Data Bundle Purchase Program"""

#KEY LEARNING OUTCOMES 
#Create a program which demonstrates the following key learnings:
#● Validating inputs
#● Checking a value input against a minimum value requirement
#● Printing and returning values
#The demonstration will involve creating a program that replicates buying data bundles using credit already on your phone.
#This includes the ability to:
#● Access your phone top up account with a passcode
#Once logged in, you can:
#● Check a balance on your phone
#● Buy a data bundle from the credit you have on your phone
#During the buying of the data bundle process, this includes the following functions
#● Verifying the persons phone number
#● Requests how much you want to top up
#● Confirming the person has enough in their payment source for the top-up, and if not, reject the transaction

#DELIVERY REQUIREMENTS
#One Python file called: SimpleBundlePurchase_v2.py 
#This file should be created in line with the details as described in Chapter 8 Curriculum
#One updated version of the Python file called: test_DataBundlePurchase.py <-----IN THIS DOCUMENT !!!
#-----------------------------------------------------




from ch01mobilebundle_validation import DataBundlePurchase
print ("TEST 1")
DataBundlePurchase("cats", 35)

#print ("TEST 2")
#DataBundlePurchase("dogs", 5)
#
#print ("TEST 3")
#DataBundlePurchase("6773585", 0)
#
#print ("TEST 4")
#DataBundlePurchase("gj67ssj", 20)
