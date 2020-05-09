# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:43:11 2020

@author: Gökhan
"""


# =============================================================================
# hatalar / istisnalar (exceptions)
# =============================================================================

# ZeroDivisionError Hatası
a = 10
b = 0

# ZeroDivisionError: division by zero

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olmaz")


#  Tip Hatası
    
a = 10
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayı sayı ile bölünür")