# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 12:44:36 2022

@author: LENOVO
"""


for i in range (1,101,1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
         print("Fizz")
    elif i%5==0:
         print("Buzz")
    else:
        print(i)