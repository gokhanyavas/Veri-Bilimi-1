# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:43:48 2020

@author: Gökhan
"""


# =============================================================================
# maaslara yüzde 20 zam yapılacak gerekli kodları yazınız
# =============================================================================


maaslar = [1000,2000,3000,4000]
# bu şekilde tek tek yazmak olmaz.. 
1000*20/100 + 1000
# otonomlaştırma : optimize işlemi yaptık
maaslar[0] * 20 / 100 + maaslar[0]

# dongü yazılacak 
# fonksiyon yazmak 

def yeni_maas(x):
    print(x)
    
yeni_maas(4)


def yeni_maas(x):
    print(x*20/100 + x)
    
yeni_maas(1000)


for i in maaslar:
    yeni_maas(i)