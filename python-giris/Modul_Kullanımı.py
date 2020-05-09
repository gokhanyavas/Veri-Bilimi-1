# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:16:03 2020

@author: Gökhan
"""


# =============================================================================
#  modül oluşturmak
# =============================================================================

# belli bir amacı yerine getirmek için toplu işlemleri içerir

import HesapModulu

HesapModulu.yeni_maas(800)

# kısa isim vererek kullanma
import HesapModulu as hm

hm.yeni_maas(1000)


# sadece o modülü kullanmak istiyorsak 
from HesapModulu import yeni_maas
yeni_maas(4000)

# modülün içindeki değerlere ulaşma 

import HesapModulu as hm
hm.maaslar
