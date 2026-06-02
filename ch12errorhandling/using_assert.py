#assert, Python’da “bu şart doğru olmalı, doğru değilse hata ver”
#demek için kullanılır.
#assert koşul

#x=5
x=-5
assert x > 0, "x pozitif olmalıdır"
print("program devam ediyor")

#Kod içinde varsayım kontrolü
#Test amaçlı doğrulama
#Geliştirme sırasında hata yakalama
#Fonksiyonun beklenen değerle çalıştığını kontrol etme

#Önemli fark: assert kullanıcı hatası için ideal değildir

#Şuna dikkat etmek önemli:

#assert, genellikle geliştirici kontrolü içindir.

#Kullanıcıdan gelen hatalı veriyi kontrol etmek için genelde if + raise daha doğrudur.