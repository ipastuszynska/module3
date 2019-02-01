# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:06:28 2019

@author: iza
"""

#NOSE
# begin each tests method with “test_” to ensure that the nosetest runner can find your tests

# this is how to execute a single test file
# nosetests test_primes.py

class Calculator(object): 
#    def add(self, x, y): 
#        number_types = (int, float, complex) 
#        if isinstance(x, number_types) and isinstance(y, number_types): 
#            return x + y 
#        else: 
#            raise ValueError


#--------------------------------------------------
#TASK 2: Debugging / break teh above code
#--------------------------------------------------

    def add(self, x, y): 
        number_types = (int, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types): 
            import pdb; pdb.set_trace() # new debugging technique 
            result = x - y 
            print ('Result is: {}'.format(result)) 
            return result 
        else: 
            raise ValueError