name="John Doe"
age=20
salary_per_hour=19.65
is_employed=True

print(name)
print(age)
print(salary_per_hour)
print(is_employed)

print(type(name))
print(type(age))
print(type(salary_per_hour))
print(type(is_employed))

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

number_text="123"
print(number_text+"10")
#print(number_text+10) hata verir
print(int(number_text)+10)
print(int(number_text)+int("10"))

age = 18

if age >= 18:
    print("Reşitsiniz")
else:
    print("Reşit değilsiniz")

score = 75

if score >= 90:
    print("Çok iyi")
elif score >= 70:
    print("İyi")
elif score >= 50:
    print("Orta")
else:
    print("Başarısız")

for i in range(5):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11,2):
    print(i)

for i in range(0,11,2):
    print(i)

names = ["Ali", "Ayşe", "Mehmet"]

for name in names:
    print(name)

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

for i in range(1, 10):
    if i == 5:
        break

    print(i)

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

text = "Python öğreniyorum"

print(text)

text = "Python"

print(len(text))  # 6

text = "Python Programlama"

print(text.upper())  # PYTHON PROGRAMLAMA
print(text.lower())  # python programlama


text = "   Merhaba Dünya   "
print(text.strip())

text = "Python çok güçlü bir dildir"

if "Python" in text:
    print("Python kelimesi var")
else:
    print("Python kelimesi yok")

text = "Java öğreniyorum"

new_text = text.replace("Java", "Python")

print(new_text)

text = "Ali,Veli,Ayşe"

names = text.split(",")

print(names)

names = ["Ali", "Veli", "Ayşe"]

text = "-".join(names)

print(text)

text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n

text = "Python Programlama"

print(text[0:6])   # Python
print(text[7:])    # Programlama
print(text[:6])    # Python

name = "John Doe"
age = 20
salary_per_hour = 19.65
age = 35

message = f"Merhaba {name}, yaşınız {age}"

print(message)

price = 100
tax = 20

total = price + tax

print(f"Toplam fiyat: {total} TL")