#import sys

#print("Bu bir normal mesajdır",file=sys.stdout)
#print("Bu bir hata mesajıdır",file=sys.stderr)

#import  warnings
#warnings.warn("Bu bir uyarıdır",UserWarning)
#warnings.warn("Bu fonksiyon ileride kaldırılacak", DeprecationWarning)


#try except else finally

#birinci_sayi=int(input("birinci sayiyi giriniz : "))
#ikinci_sayi=int(input("ikinci sayiyi giriniz : "))
birinci_sayi=2
ikinci_sayi=2
#ikinci_sayi=0
try:
    x=birinci_sayi/ikinci_sayi
except ZeroDivisionError as e:
    print("Hata oluştu :",e)
else:
    print("Hata yoksa çalışır")
    print(x)
finally:
    print("uygulamadan çıkılıyor...")
    print("uygulamadan çıkıldı.")

try:
    x=int("abc")
    #x=int(7)
    print(x)
except ValueError as e:
    print("Bir değer hatası meydana geldi.",e)
except TypeError as e:
    print("Bir tür hatası meydana geldi.",e)

try:
    y=int("abc")
except (ValueError,TypeError) as e:
    print("Bir hata meydana geldi.",e)

#argümanlar
try:
    z=int("abc")
except ValueError as ex:
    print("Bir değer hatası meydana geldi.",ex)

a=input("Bir sayı giriniz : ")
try:
    x=1/int(a)
    print(x)
except ZeroDivisionError as e:
    print("Sıfıra bölme hatası meydana geldi.",e)
except (ValueError,TypeError) as e:
    print("Bir hata meydana geldi.",e)
finally:
    print("Her zaman çalışacak")

#istisna hiyerarşisi
#Bütün istisnalar BaseException türetilmiştir.

try:
    raise ValueError("Bu bir değer hatası")
except BaseException as e:
    print("Bir temel istisna meydana geldi.",e)

#Yaygin bir hata
try:
    h=1/0
except:
    print("Bir hata meydana geldi.")


def pozitif_sayi(sayi):
    if sayi<=0:
        raise ValueError("Sayı pozitif olmalıdır")
    return sayi

try:
    print(pozitif_sayi(-2))
except ValueError as e:
    print("Hata : ",e)