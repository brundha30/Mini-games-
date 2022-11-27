# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:38:09 2022

@author: LENOVO
"""


def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number%i ==0:
            is_prime=False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
