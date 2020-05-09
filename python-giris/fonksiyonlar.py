# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:37:16 2020

@author: Gökhan
"""

# fonksiyonlara giriş ve fonk. okuryazarlığı

print #<function print>

?print


# fonksiyon nasıl yazılır ?

# def ile başlanır fonksiyonlara

def kare_al(x):
   print(x**2)
    
kare_al(5)  


# bilgi notuyla işlem yapma
# x argumanı
def kare_al(x):
   print("Girilen sayinin karesi : " + str(x**2))
   
kare_al(5)  


def kare_al(x):
   print(
       "Girilen sayi : " + str(x) + " " +
       "Girilen sayinin karesi : " + str(x**2)
        )
   
kare_al(5)  

# 2 argumanlı fonksiyonlar
def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(3, 4)

# ön tanımlı argumanlar

def carpma_yap(x,y = 1):
    print(x*y)
 
carpma_yap(3)
carpma_yap(3,4)

# argumanların sıralaması

carpma_yap(y=2,x=3)


# ne zaman fonksiyon yazılır?
# tekrar eden işlemlerin önüne geçmek için

# isi, nem, sarj

def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)
    
direk_hesap(25, 40, 70)


# fonksiyon cıktılarını girdi olarak kullanmak

# return 

def direk_hesap(isi, nem, sarj):
    return (isi + nem)/sarj

direk_hesap(25, 40, 70) * 9


# local ve global ifadesi

# bunlar global değişkenlerdir. tüm yerdeler
x = 10
y = 20


# x,y local değişkenlerdir. 
def carpma_yap(x,y):
    return x*y

carpma_yap(2, 4)

# local etki alanından global etki alanını değiştirme

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
eleman_ekle(5)

x



