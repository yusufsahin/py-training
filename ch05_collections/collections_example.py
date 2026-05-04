#Demet /tuple oluşturmak
t=(1,2,3,4,2,5,6,2)
print(t[1])
#t[1]=5
print(t.count(2))
print(t.index(3))
print(t)
#Farklı veri tipleri ile demet / tuple
demet2 = (1, "merhaba", 3.14, True)
print(demet2)

#Liste
my_list=[1,2,3]
print(my_list)
my_list.append(4)
print(my_list)
my_list.extend([5,6])
print(my_list)
my_list.remove(3)
print(my_list)
my_list.insert(0,0)
print(my_list)
my_list.insert(3,3)
print(my_list)
my_list.sort()
my_list.reverse()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_list.sort()
print(my_list)
#Slicing [start:stop:step]
l=[0,1,2,3,4,5,6]
print(l)
print(l[3])
print(l[5])
k=["a","b","c","d","e","f","g","h","i"]
print(k)
print(k[3])
print(k[5]) #6. eleman
print(k[4]) #5. eleman

#slicing

print(l[1:4])
print(k[1:4])
print(l[2:])
print(k[2:])
print(l[::1])
print(k[::1])
print(l[::2])
print(k[::2])
print(l[::-1])
print(k[::-1])
print("\n")
#Genişletilmiş Yinelemeli Paketleme (Extended Iterable Unpacking)
#Yinelemeli Paketleme
a,b,*r=[1,2,3,4,5]
print(a,b,r)
x,y,z,*n=[10,20,30,40,50]
print(x)
print(y)
print(z)
print(n)

a=[1,2,3]
a.append(4)
print(a)
a.extend([5,6])
print(a)
a.insert(0,0)
print(a)

a.pop(1)
print(a)
del a[0]
print(a)

b=[1, 2, 3, 4, 2, 5]
b.remove(2)
print(b)
b.remove(2)
print(b)

c=[3,1,4,1,5,9]
c.sort()
print(c)

sorted_c=sorted(c)
print(sorted_c)
d=c.copy()
print(d)

print(c.count(1))

#Kümeler Set

s={1,2,3}
print(s)
s2=set([1,2,3])
print(s2)

s.add(4)
print(s)
s.update([5,6])
print(s)
s.remove(2)
print(s)
s.discard(3)
print(s)
s.pop()
print(s)
s.clear()
print(s)


#işlemler

s1={1,2,3}
s2={3,4,5}
print(s1)
print(s2)
print(s1 | s2) #bileşim
print(s1 & s2) # kesişim
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2) #simetrik fark / kesişim dışında kalanlar
print(s1.intersection(s2))
print(s2.intersection(s1))

#Küme Operatörleri

a1={1,2,3}
a2={1,2}
print(a2<=a1)
print(a2<a1)
print(a1>=a2)
print(a1>a2)

print(a1<=a2)

#Dictionary - sözlükler
d= {'isim':'Alice','yaş':25}
print(d['isim'])
d['yaş']=26
print(d)

del d['yaş']
print(d)

isim=d.pop('isim')
print(d)
print(isim)

sozluk={'isim':'John','yaş':'25'}
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())
print(sozluk.get('isim'))
sozluk.update({'yaş':27,'şehir':'Texas'})
print(sozluk)

v={'isim':'Alice','yaş':25}
keys_view=v.keys()
v['şehir']='Texas'
print(keys_view)