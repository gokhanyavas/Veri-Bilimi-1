# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:05:56 2020

@author: Gökhan
"""


# =============================================================================
# map & filter & reduce 
# =============================================================================


liste = [1,2,3,4,5]


for i in liste:
    print(i + 10) 

# map : verilen vektörün içinde tanımlanacak fonk. calısıtırma imkanı verir.
    
list(map(lambda x : x + 10, liste))

# filter

liste = [1,2,3,4,5,6,7,8,9,10]

# çift sayıları bulduk :))
list(filter(lambda x: x % 2 == 0, liste))

# reduce : indirgeme işlemi yapar

from functools import reduce

liste = [1,2,3,4,5]
reduce(lambda a,b: a+b, liste) 
# 55 çıkar sonuc.