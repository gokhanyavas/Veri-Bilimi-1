# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:53:08 2020

@author: Gökhan
"""


# =============================================================================
# mini uygulama 
# =============================================================================


sinir = 50000

magaza_adi = input("Mağaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz :"))

if gelir > sinir:
    print("Tebrikler; " +  magaza_adi +", promosyon kazandınız!")
elif gelir < sinir:
    print("uyari! Çok düşük : " + str(gelir))
else:
    print("Takibe devam!")