sayilar=[1,2,3,4,5,6]
cift_sayilar=filter(lambda x:x%2==0,sayilar)
print(list(cift_sayilar))

tek_sayilar=filter(lambda x:x%2==1,sayilar)
print(list(tek_sayilar))


cift_sayilar_2=[]
tek_sayilar_2=[]

for sayi in sayilar:
    if sayi%2==0:
        cift_sayilar_2.append(sayi)
    else:
        tek_sayilar_2.append(sayi)
print(cift_sayilar_2)
print(tek_sayilar_2)


def cift_mi(x):
    return x % 2 == 0

cift_sayilar_3 = filter(cift_mi, sayilar)
print(list(cift_sayilar_3))

def tek_mi(x):
    return x % 2 == 1

tek_sayilar_3 = filter(tek_mi, sayilar)
print(list(tek_sayilar_3))

#List Comprehensions / Anlayış

#x*x
#x**2

kareler=[x**2 for x in sayilar]
print(kareler)

cift_sayilar_4 = [x for x in sayilar if x%2==0]
print(cift_sayilar_4)

cift_sayilar_4_karesi = [x**2 for x in sayilar if x%2==0]
print(cift_sayilar_4_karesi)
cift_sayilar_arti_3= [x+3 for x in sayilar if x%2==0]
print(cift_sayilar_arti_3)

#tuple->()
#liste->[]
#Küme {}

sayilar2=[1,2,3,4,4,5,5]
kareler_kumesi_listesi=[x**2 for x in sayilar2]
print(kareler_kumesi_listesi)
kareler_kumesi={x**2 for x in sayilar2}
print(kareler_kumesi)

kareler_kumesi_dict={x:x**2 for x in sayilar2}
print(kareler_kumesi_dict)

kareler_kumesi_dict_lambda=dict(map(lambda x:(x,x**2),sayilar2))
print(kareler_kumesi_dict_lambda)

sayilar5=(x**3 for x in range(5))
print(type(sayilar5))

for sayi in sayilar5:
    print(sayi)

#Lazy List
#Tembel değerleme, ihtiyaç duyulana kadar hesaplamaların ertelenmesini sağlar. Bu, bellek verimliliği sağlar.

sayilar4=(x**2 for x in range(5))
for sayi in sayilar4:
    print(sayi)

#Generator yield

def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
for sayi in fibonacci(10):
    print(sayi)


#Generator - next()
def basit_generator():
    yield 1
    yield 2
    yield 3

#yield anahtar kelimesi kullanılarak oluşturulan generator nesneleri üzerinde
# next() fonksiyonu ile iterasyon yapılabilir.
gen=basit_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#Liste anlayışları ile Generator
generator= (x**2 for x in range(5))
for sayi in generator:
    print(sayi)

#Kopyalama problemi
original_p=[1,2,3]
kopya_p=original_p
kopya_p.append(4)
print(kopya_p)
print(original_p)

orijinal=[1,2,3]
kopya=orijinal[::]
kopya.append(4)
print(orijinal)
print(kopya)

import copy
orijinal_d=[1,2,3]
kopya_d=copy.deepcopy(orijinal_d)
kopya_d.append(4)
print(orijinal_d)
print(kopya_d)


