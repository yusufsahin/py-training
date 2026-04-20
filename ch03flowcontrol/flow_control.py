#input
from itertools import count
from unittest import result

x=int(input('Bir sayi giriniz : '))
print(x)
#if elif else
if x>5:
    print("Girilen sayi 5'ten büyüktür")
elif x==5:
    print("Girilen sayi 5'e eşittir.")
else:
    print("Girilen sayi 5'ten küçüktür")

gun=int(input("1-7 arasında sayi giriniz"))

if gun==1:
    print("Girilen gün Pazartesi")
elif gun==2:
    print("Girilen gün Salı")
elif gun==3:
    print("Girilen gün Çarşamba")
elif gun == 4:
    print("Girilen gün Perşembe")
elif gun==5:
    print("Girilen gün Cuma")
elif gun==6:
    print("Girilen gün Cumartesi")
elif gun==7:
    print("Girilen gün Pazar")
else:
    print("Gün tanımlı değil")

if not []:
    print("Boş liste False olarak değerlendirilir")
print("And,Or,Not")
a=True
b=False
print(a and b)
print(a or b)
print(not a)


print("---k = 7 ---- , < <")
k=7

print(1<k<10)
print(10<k<20)
print(5>k<20)
print(10>k<20)

#in
meyveler =["elma","portakal","mandalina"]

print("elma" in meyveler)
print("üzüm" in meyveler)

#type check
z=43

print(type(z))
print(type(z) == int)
print(type(z) is int)
print(isinstance(z,int))

t=43.7

print(type(t))
print(type(t) == int)
print(type(t) is int)
print(isinstance(t,int))


m=int(input("1. sayi : "))
n=int(input("2. sayi : "))
try:
    result=m//n
    print(result)
except ZeroDivisionError:
    print("Sayi 0 a bölünemez")
else:
    print("hata ile karşılaşılmadı")
finally:
    print("her durumda çalışır")

#comment yorum satırı - çalışmaz / kod olarak interpreter değerlendirmez / interpreter görmezden gelir


count=0
while count<10:
    #count += 2
    print(count)
    count+=1
    #count+=2

for i in range(0,10,1):
    print(i)

count1=0
while count1<10:
    #count += 2
    print(count1)
    count1+=2
for i in range(0,10,2):
    print(i)

for meyve in meyveler:
    print(meyve)

for index,meyve in enumerate(meyveler):
    print(index,meyve)

for i in range(10):
    if i==5:
        break
    print(i)

names=["Alice","Bob","Charlie"]
ages=[25,30,33]

for name,age in zip(names,ages):
    print(f"{name} is {age} years old")

age=18
status="Adult" if age>=18 else "Minor"
print(f"{status} - ehliyet alabilir")

u=4
#u=-1
if u>0:
    pass # ... de kullanılabilir
else:
    print("negatif sayi")

numbers=[]

for num in range(10):
    numbers.append(num)
print(numbers)

x = range(3, 6)
for n in x:
  print("sayi" +str(n))