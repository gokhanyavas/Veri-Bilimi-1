# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:38:40 2020

@author: Gökhan
"""
# Vektorel Operasyonlar
# oop

a = [1,2,3,4]
b = [2,3,4,5]

ab =[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])


print(ab)


# FP : fonksiyonel programlama

import numpy as np

ax = np.array([1,2,3,4])
bx = np.array([2,3,4,5])

ax * bx
