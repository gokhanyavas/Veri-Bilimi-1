# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:33:10 2020

@author: Gökhan
"""


# =============================================================================
# isimsiz fonksiyonlar
# =============================================================================

# isimli fonk
def old_sum(a,b):
    return a+b

old_sum(4, 5)

# lambda

new_sum = lambda a,b : a+b

new_sum(4,7)


sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

#lambda x: x[1] : 1. değerden başlasın ve sıralasın
sorted(sirasiz_liste, key = lambda x: x[1])


