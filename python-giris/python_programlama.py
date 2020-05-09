# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:21:53 2020

@author: Gökhan
"""


#sayılar ve stringlere giriş

9
9.2
9+9
9*9

print('HELLO AI ERA')

"HELLO AI ERA"


type(9)

type(9.2)

type("HELLO AI ERA")

# stringlere yakından bakalım.

"a"+ "b"

'a' * 3

# string - len()

val = "gökhan yavaş"

#del metodu ile varible silinebilir.
#del val

len(val)


a = 9
b = 10

a*b

# upper ve lower fonksiyonları 
val.upper()

# yeni değer ataması yaptık
newval = val.upper()

val.lower()

# ilk bulduğu kelimenin harfini büyük yapar
val.capitalize()

# küçükmü : true false döner
val.islower()

newval.islower() # false


# replace metodu 

val.replace("a","@")


# strip metodu : kırpma işlemi
val2 = "  gökhan yavaş  "
## boşlukları kırp defualt değeri vardır
val2.strip()

## METODLAR ##

dir(str)

# ilk harfleri büyük yap
val.title()

# substring ifadeler

# köşeli parantez seçim işlemi
# anlamına geliyor pythonda 

# index ifade ediyor.

val[0]

# : soldakinden sağdakine seçim yap
val[0:6]


## DEGISKENLER ## 

ax = 9999
bx = "gökhan yapay zeka giriş"
cx = ax * 6


## TİP DÖNÜŞÜMLERİ ## 

## input : kullanıcıdan bilgi alır.

birinci_sayi = input()

ikinci_sayi = input()


int(birinci_sayi) + int(ikinci_sayi) 

float(12)

str(12)

type(str(12))

## PRINT FONKSIYONU ##

print("geleceği", "yazanlar")
# sep : argumandır. biçimlendirme için kull.
print("geleceği", "yazanlar", sep="_")

print()
## ? işareti ile fonk. açıklamasına ulaşırız.
# ?type


## VERI YAPILARI ##

# LİSTELER 

#[]
#list()

notlar = [90,80,70,55]
type(notlar)

liste = ["a",19.3,909,notlar]

len(liste)

# listenin elemanına erişme.
type(liste[1])

#liste silmek
#del liste

#liste elemanları index, erişim
liste[0]
liste[3]
#aralıklı seçim
liste[0:2]
#sol kısım boş olabilir. yine aynı sonuç verir.
liste[:2]
# 2 dahil sona kadar al.
liste[2:]
# listenin alt elemanlarına erişim
liste[3][2]


# liste eleman ekle değiştir.

liste2 = ["ali","veli","berkcan","ayşe"]
#listenin elemanını değiştirme
liste2[1] = "velinin babası"


# listeye eleman ekleme
liste2 = liste2 + ["kemal"]

# liste eleman silme
del liste2[2]

liste2

## LİSTE METODLARI ## 

dir(liste2)
# kalici değişiklik meydana geliyor.
liste2.append("Gökhan")

liste2.remove("Gökhan")

liste2.insert(0,"Yavaş")

# liste sonuna eleman ekleme 
liste2.insert(len(liste2),"Gökhan")

#pop : eleman uçurmak için kullanılır. siler yani.
liste2.pop(0)

## count metodu

liste2.count("ali") 

liste2.count()

# copy : yedekleme kopyalama işlemi.

liste2_yedek = liste2.copy()

# extend : 2 listeyi birleştirmek için kullanılıyor.

liste2.extend(["a","b","c",10])

# index()
liste2.index("ali")

#reverse() : tersine çevirir.
liste2.reverse()

#sort : sıralama
liste3 = [10,30,65,9]
liste3.sort()
liste3 


#clear : temizler 

liste3.clear()
liste3 


## VERİ YAPILARI - Tuple ## 

# tupler listeler gibi değiştirilemez
# kafa rahat olsun değişmesin istersek kull.
# liste gibidir.
# sıralıdır, index işlemleri yapılabilir.

t = ("ali","veli",1,2,3.2,[1,2,3,4])


t = "ali","veli",1,2,3.2,[1,2,3,4]

t = ("eleman")
# str döner , tuple sonuna , atılırsa algılıyor.

t = ("eleman",)


type(t)

t[1]
t[:3]

## sözlükler ##

# kapsayacı, değiştirebilir, sırasız
# referanslı bir veri yapısıdır. 
# indexleme yapılamaz

# key, value

# sozlük oluşturma..
sozluk = {"REG" : "Regresyon Modeli", 
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classicification and Reg"}

len(sozluk)

sozluk[0] #olmazzz

# elemanlar bu şekilde seçilir, erişilir.
sozluk["REG"]

# SÖZLÜK İÇİNDE SÖZLÜK
sozluk = {
    "REG" : {"RMS":10, "ABC":20, "CAS":30}
    }

sozluk["REG"]["ABC"]


# eleman ekleme 
sozluk["GBM"] = "Gradient Boosting Mac"

sozluk


##  SET - KÜME OLUŞTURMA ##

## EŞŞİZ SIRASIZ DEĞİŞTİRİLEBİLİR, FARKLI TİPLER BARINDIRILIR
# PERFORMANS ODAKLIDIR.
# KÜMELERE BENZER

#set oluşturma

s = set()
# liste üzerinden set oluşturma
l = [1,"ali",123]

s =  set(l)

# tuple üzerinden set oluşşturma
t =("a","ali")
s = set(t)

# set : birden fazla değeri tekilleştirir.
a = "ali_ata_bakma_uzaya_git."
s = set(a)
s

len(s)

## sete eleman ekleme çıkarma

l = ["gelecegi","yazanlar"]

s = set(l)

dir(s)


s.add("ile")

s
s.add("gokhan")

s.remove("gokhan")

# =============================================================================
# yorum satırı yapmak için
# 
# ctrl + 4 
# 
# ctrl + 1
# =============================================================================


# setlerde işlemler 


set1 = set([1,2,5])
set2 = set([1,2,3])

# set1 de olup set2 de olmayanı getirir.
set1.difference(set2)
# set2 de olup set1 de olmayanı getirir.
set2.difference(set1)

# farklı olanları getirir.
set1.symmetric_difference(set2)

set1 - set2
set2 - set1


# intersection : kesisim
 
set1.intersection(set2)

# aynı işlemi bu yöntemlede yapabiliriz.
set1 & set2

# birleşim : union : her eleman birleşir.

set1.union(set2)

# intersection_update : birleşme işlemi
# set1.intersection_update(set2)


# setlerde sorgu işlemi .::::.:.

# iki kümenin boş olup olmadığı sorgulama
# > isdisjoint : boş değilse false
set1.isdisjoint(set2)

# set1 set2 mim alt kümesimdir? 
set1.issubset(set2)

# bir küme diğerini kapsıyor mu ?
set2.issuperset(set2)

