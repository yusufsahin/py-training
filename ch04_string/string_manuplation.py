tek_tirnak_str='Merhaba'
cift_tirnak_str="Dunya"
cok_satir_str="""Bu
bir 
çok
satırlı
string'tir.
"""
print(tek_tirnak_str)
print(cift_tirnak_str)
print(cok_satir_str)

print(tek_tirnak_str+cift_tirnak_str+cok_satir_str)
print(tek_tirnak_str+' '+cift_tirnak_str)
print(tek_tirnak_str+" "+cift_tirnak_str)
print(tek_tirnak_str+""" """+cift_tirnak_str)
print(tek_tirnak_str+"\n"+cift_tirnak_str)

#isim=input("isim girin : ")
#print("Merhaba ",isim)

#print("Merhaba, {isim}".format(isim=isim))

#Ayırıcı / Separatör ile default boşluk " "

print("Merhaba","Dünya","!")
print("Merhaba","Dünya","!",sep="-")
print("Merhaba","Dünya","!",sep=";")
print("Merhaba","Dünya","!",sep="\t")
print("Merhaba","Dünya","!",sep="\n")

#Sonlandırıcı
print("Merhaba Dünya!",end=" BİTTİ\n")

yeni_satır_str="\nMerhaba\nDünya"
print(yeni_satır_str)

#Cooking String
tab_str="Merhaba\tDunya"
print(tab_str)

print("O \"Merhaba\" dedi")
print('O "Merhaba" dedi')

ters_slash_str="Bu bir ters slash \\"
print(ters_slash_str)

#Concateation / String Birleştirme işlemleri

merhaba="Merhaba"
dunya="Dunya"
merhaba_dunya=merhaba+" "+dunya
print(merhaba_dunya)

tekrar_str="Merhaba"*3
print(tekrar_str)

uc_tırnak_str="""Bu bir çok satırlı ve 
'tek tırnak' ile "çift tırnak" 
içeren string"""
print(uc_tırnak_str)

#string yöntemleri / methodları
s="merhaba - ı i"

print(s.upper())

k="DÜNYA - I İ"
print(k.lower())

print(s.capitalize())

t="merhaba dünya, merhaba uzay"
print(t.title())

v="    Merhaba Dünya      "
print(len(v))
print(v.strip())
u=v.strip()
print(len(u))

z="merhaba dünya"
print(z.replace("dünya","Python"))

print(z.find("dünya"))
l="merhaba dünya, merhaba uzay, merhaba Python"
print(l.count("merhaba"))

#String Testleri
print("merhaba Python".startswith("merhaba"))

m="merhaba dünya"
print(m.endswith("dünya"))
print(m.endswith("dunya"))

g="merhaba"
print(g.isalpha())
print("merhaba9".isalpha())
print("12345".isdigit())

print("    ".isspace())

#String Formatlama

#% operatörü
name="Alice"
age=30
city="New York"
formatted_str="İsim: %s, Yaş: %d, Şehir: %s" % (name,age,city)
print(formatted_str)

format_func_str="İsim: {}, Yaş: {}, Şehir:{}".format(name,age,city)
print(format_func_str)

#f String

f_str=f"İsim: {name}, Yaş: {age}"
print(f_str)


#Diğer yardımcılar
person={"name":"Alice","age":30}
formatted_dicti_str="İsim: {name}, Yaş: {age}".format(**person)
print(formatted_dicti_str)

from string import Template
template=Template("İsim: $name, Yaş: $age")
formatted_temp_str=template.substitute(name="Alice",age=30)
print(formatted_temp_str)

#Slicing  s[start:stop:step]

h="merhaba dünya"

print(h[0:7])
print(h[8:])
print(h[:7])
print(h[::2])
print(h[::-1])


#split

n="merhaba dünya"
kelimeler=n.split()
print(kelimeler)
csv="elma;armut;çilek"
meyveler=csv.split(";")
print(meyveler)
#join
sozcukler=['merhaba','dünya','merhaba','python']
print(' '.join(sozcukler))
fruits=['apple','banana','ananas']

csv2='|'.join(fruits)
print(csv2)
