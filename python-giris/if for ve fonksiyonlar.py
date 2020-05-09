# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:13:37 2020

@author: Gökhan
"""

# =============================================================================
# if for ve fonksiyonları birlikte kullanmak 
# =============================================================================

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100 + x)
    
    
def maas_alt(x):
    print(x*20/100 + x)


for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)
    
    
# =============================================================================
# break ve continue
        
# break: işlemi keser: döngünden at.
# continue : bunu at çalışmaya devam et.
# =============================================================================

maaslar = [8000,5000,2000,1000,3000,1000]

dir(maaslar)

maaslar.sort()

maaslar

# 3000 olduğunda işlemi kes.

for i in maaslar:
    if i == 3000:
        print("kesildi.")
        break
    print(i)
    
# continue : değeri atladı. devam et anlamında
for i in maaslar:
    if i == 3000:
        continue
    print(i)
    
    
# =============================================================================
# while : olduğu sürece, şart sağlandığı sürece.
# =============================================================================
    
sayi = 1
# sayi 10 dan küçük olduğu sürece işlemi yap.
while sayi < 10:
    sayi += 1
    print(sayi)
