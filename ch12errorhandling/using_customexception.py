#Kendi istinanızı oluşturma
class NegatifSayiHatasi(Exception):
    pass

def pozitif_sayi(sayi):
    if sayi<=0:
        raise NegatifSayiHatasi("Sayı negatif olamaz.")
    return sayi

try:
    print(pozitif_sayi(-10))
except NegatifSayiHatasi as e:
    print("Özel Hata : ",e)
