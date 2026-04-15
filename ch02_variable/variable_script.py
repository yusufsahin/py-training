#Değişken ve değer atama
x=5 #int
a=4.5 #float
a_=7
name="John" #str / string
is_student = True # boolen
print(x)
print(a)
print(name)
print(is_student)
x=10
print(x)
x=x+7
print(x)
x+=5
print(x)

#değişken sayı ile başlamaz
#2a=9
a_2=5
#tire / - ile değişken tanımlanamaz
#a-2=5
A_2=7 # a_2 den farklı değişken

name="Alice"

print(name)
print(name.upper())
print(name.lower())

#Operatörler

k=7
l=5
print(k+l)
print(k-l)
print(k*l)
print(k/l)
print(k//l)
print(k%l)

age=35
print(age)
print(type(age))

height=1.75
print(height)
print(type(height))

first_name="John"
print(first_name)
print(type(first_name))
last_name="Smith"
print(last_name)
print(type(last_name))
full_name=first_name+" "+last_name
print(full_name)
full_name_alias=first_name+last_name
print(full_name_alias)

bool_value=True
print(bool_value)
print(type(bool_value))

z=9
print(z)
print(type(z))
z=9.0
print(z)
print(type(z))
z=10
print(z)
print(type(z))

#switching types

t="123"
print(type(t))
print(t+"1")
print(int(t)+1)
print(float(t)+1)
print(t+str(1))
print(bool(0))
print(bool(1))
print(bool(10))
print(int(True)),
print(int(False))
print(int(True))
print(int(False))
print(float(True))
print(float(False))

#List
meyveler=["apple", "banana", "cherry"]
print(meyveler)
print(meyveler[0])
print(meyveler[1])
print(meyveler[2])
meyveler[2]="orange"
print(meyveler[2])
print(meyveler)
print(type(meyveler))

#Tuples - Demetler

point=(20,30)
print(point)
print(type(point))
coordinate=(5.0,6.7,8.3)
print(coordinate)
print(type(coordinate))
#point(1)=6
#point[1]=7
#print(point)
#print(type(point))

#dictionary

person={"name":"John","age":25,"city":"New York"}
print(person)
print(type(person))

print(person["name"])
person["name"]="Sam"
print(person)
del person["age"]
print(person)
for key in person.keys():
    print(key,person[key])

for key,value in person.items():
    print(key,value)

keys=person.keys()
print(keys)
values=person.values()
print(values)
items=person.items()
print(items)

person.update({"city":"Texas"})
print(person)

person2={"isim":"John","yas":25,"adres":{"sehir":"New York","postakodu":"34007"}}
print(person2["adres"]["sehir"])
print(person2["adres"]["postakodu"])