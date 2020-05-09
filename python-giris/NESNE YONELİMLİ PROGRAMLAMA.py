# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:37:13 2020

@author: Gökhan
"""

# =============================================================================
# NESNE YONELİMLİ PROGRAMLAMA
# =============================================================================

# SINIF NEDİR?

"""
class VeriBilimci():
    print("Bu bir sınıftır")"""

# sınıf özellikleri (class attributes)
    
class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
# sınıf özelliklerine erişim
VeriBilimci.bolum
VeriBilimci.sql

# özellikleri değiştirmek :

VeriBilimci.sql = "Hayır"
VeriBilimci.sql

# Sınıf Örneklendirmesi (instantiation)
# ali sınıfın örneği oldu.
ali = VeriBilimci()
ali.sql

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql

# örneklenen değişiklik sınıfın özelliklerini etkiyor.
veli.bildigi_diller # python geliyor. ki python bilmiyor.


# örnek özellikleri

# her bir ayrı örnek için farklı özellik tutar. 
# self : örnekleri temsil eder. temsilcidir.
#  
class VeriBilimci():
    bildigi_diller = ["R","Python"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
        
ali = VeriBilimci()
ali.bildigi_diller.append("Python")
ali.bildigi_diller 


veli = VeriBilimci()
veli.bildigi_diller      

veli.bildigi_diller.append("R")
veli.bildigi_diller 

VeriBilimci.bildigi_diller

ali.bolum
VeriBilimci.bolum

ali.bolum = 'istatistik'
veli.bolum = 'pc müh'
veli.bolum

# =============================================================================
# örnek metodları
# =============================================================================

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
        
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller


# =============================================================================
# MİRAS YAPILARI - inheritance
# =============================================================================

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
# miras yapısı
class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()
veribilimci1.FirstName = "Gokhan Yavas"
        
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""
        
# fonksiyonel yapıda sınıf tanımlaması.
class Employees_New():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

a = Employees_New("a","b","c")    
a.FirstName
a.LastName
a.Address
