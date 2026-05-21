from matematik import topla, cikar, carp, bol, kare_alani, dikdortgen_alani, ucgen_alani, daire_alani
#from matematik.geometri import kare_alani
#from matematik.temel import topla

#from matematik.geometri import kare_alani init tanımlanmazsa

print("***=== Temel Matematik ===***")
print("Toplama : ",topla(5,3))
print("Çıkarma : ",cikar(5,3))
print("Çarpma : ",carp(5,3))
print("Bölme : ",bol(5,3))

print("***=== Geometri Matematik ===***")
print("Kare Alanı : ",kare_alani(5))
print("Dikdörtgen alanı:", dikdortgen_alani(4, 7))
print("Üçgen alanı:", ucgen_alani(10, 6))
print("Daire alanı:", daire_alani(3))

#Module  = .py dosyası
#Package = içinde modüller olan klasör
#Import  = başka dosyadaki kodu kullanmak