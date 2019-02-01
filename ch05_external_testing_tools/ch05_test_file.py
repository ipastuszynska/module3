# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:31:42 2019

@author: iza
"""

#Task 1: Let’s write the test file first (as this is the correct order when you do test-driven development):

import unittest
from ch05_external_testing_tools import Calculator

class TddInPythonExample(unittest.TestCase): 
    
    def setUp(self): 
        self.calc = Calculator()
        
    def test_calculator_add_method_returns_correct_result(self): 
        result = self.calc.add(2,2) 
        self.assertEqual(4, result)
    
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):           
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        #we are now checking for a ValueError to be raised if we pass in strings.
    
    def test_calculator_returns_error_message_if_x_arg_not_number(self):        
        self.assertRaises(ValueError, self.calc.add, 'two', 3) 
    
    def test_calculator_returns_error_message_if_y_arg_not_number(self):        
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        
        
# Python does allow for the addition of strings and other types, but, for our calculator, it makes sense to only allow the addition of numbers. Let's add another failing test for this case, making use of the assertRaises method to test if an exception is raised here:
        
    

#standard unittest runner
        
        
    
if __name__ == '__main__': 
    unittest.main()
    
# nosetests nameOfTheTestFile.py - -> this will run the test wehen typed in acacomda prompt 
    
# pytest nameogTheTestFile.py  --> this will run the py test 