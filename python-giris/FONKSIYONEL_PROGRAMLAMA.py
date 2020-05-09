# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:03:30 2020

@author: Gökhan
"""


# =============================================================================
# FONKSİYONEL PROGRAMLAMA
# =============================================================================

# PURE FUNCTION : YAN ETKİSİZ FONKSİYONLAR 


# örnek 1 : yan etki .. bağımsızlık
A = 9

#impure : saf olmayan

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6) # sonucları değişiyor dikkat.

pure_sum(3,4)


# örnek 2: ölümcül yan etkiler




