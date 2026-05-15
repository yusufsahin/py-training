#basit fonk. tanımlama

def merhaba():
    print("Merhaba Dünya!")

merhaba()

#parametre kullanımı

def topla(a,b):
    return a+b

sonuc = topla(2,3)
print(sonuc)

def cikar(a,b):
    return a-b

print(cikar(2,3))

print(type(topla(2,3)))
print(type(topla(2,3.5)))
print(topla(2,3.5))

def topla(*args):
    return sum(args)

print(topla(1,2,3,4,5))

def bilgiler(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

bilgiler(isim="John",age=25)
bilgiler(isim="Jane",age=35,city="Texas")
bilgiler(isim="Sue",age=35,city="California",state="LA")

#Default parametre

def selamla(isim="Dünya"):
    print(f"Merhaba, {isim}!")

selamla()
selamla("John")
selamla(isim="Jane")


def kare(x):
    return x*x
print(kare(5))

#def kare2(x):
#    print(x*x)
#kare2(5)

#sonuc2 = kare(5)
#print(sonuc2)

#sonuc3=kare2(5)
#print(type(sonuc3))
#print(sonuc3+2)


#Global ve yerel değişken

x=10
def fonksiyon():
    x=5
    print(x)

print(x)
fonksiyon()


#iç içe fonksiyon tanımlama

def dis_fonksiyon():
    print("Dış fonksiyon")
    def ic_fonksiyon():
        print("iç fonksiyon")
        def son_fonksiyon():
            print("son fonksiyon")
        son_fonksiyon()
    ic_fonksiyon()
dis_fonksiyon()

#kapsam
def dis_fonksiyon_kapsam():
    x=10
    print(x)
    def ic_fonksiyon_kapsam():
        print(x)
    ic_fonksiyon_kapsam()
dis_fonksiyon_kapsam()

#Docstring

def carp(a,b):
    """Bu fonksiyon 2 sayıyı çarpar"""
    return  a*b
print(carp.__doc__)

#def kare(x):
#    return x*x
#print(kare(5))


##lambda fonksiyonları

kare_l = lambda x:x*x
print(kare_l(5))

topla_l = lambda a,b:a+b
print(topla_l(5,3))

#Lambda Fonksiyonlarını Sıralama Anahtarı Olarak Kullanma - sort

liste =[(2,3),(1,2),(4,1)]
liste.sort(key=lambda  x: x[1])
print(liste)

#lambda ve regex re.sub fonksiyonunda lambda ifadeleri kullanarak dinamik ikameler yapabilirsiniz.

import re
text= "Merhaba 123 Dünya"

result= re.sub(r'\d+',lambda  x: str(int(x.group(0))*2),text)
print(result)

#rekürsif fonksiyonlar
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1) #5*4*3*2*1

print(factorial(5))

def fibonacci(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=20
fib_series=[fibonacci(i) for i in range(n)]
print(fib_series)




