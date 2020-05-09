# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:34:59 2020

@author: Gökhan
"""


# =============================================================================
# karar & kontrol yapıları
# =============================================================================

# true false sorgulama

sinir = 5000

sinir == 4000 # denk mi : false

sinir == 5000 # denk mi : true


5 == 4
5 == 5


sinir = 50000

gelir = 40000

if gelir < sinir:
    print("Gelir sinirdan küçük")
    
if gelir > sinir:
    print("Gelir sinirdan küçük değil")
else:
    print("Gelir sinirdan küçük")


# elif : değilse ama böyleyse anlamında
    
sinir = 50000

gelir1 = 60000    
gelir2 = 50000 
gelir3 = 35000 
    
if gelir1 > sinir:
    print("Tebrikler hediye kazandınız")
elif gelir1 < sinir:
    print("uyarı!")
else:
    print("takibe devam")