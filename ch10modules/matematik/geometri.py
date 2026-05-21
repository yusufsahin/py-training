"""
geometri.py

Bu modül geometrik hesaplamalar içerir.
Kare, dikdörtgen, üçgen ve daire alanı hesaplar.
"""

PI = 3.14159


def kare_alani(kenar):
    """
    Karenin alanını hesaplar.
    """
    if kenar <= 0:
        raise ValueError("Kenar uzunluğu pozitif olmalıdır")

    return kenar * kenar


def dikdortgen_alani(kisa_kenar, uzun_kenar):
    """
    Dikdörtgenin alanını hesaplar.
    """
    if kisa_kenar <= 0 or uzun_kenar <= 0:
        raise ValueError("Kenar uzunlukları pozitif olmalıdır")

    return kisa_kenar * uzun_kenar


def ucgen_alani(taban, yukseklik):
    """
    Üçgenin alanını hesaplar.
    """
    if taban <= 0 or yukseklik <= 0:
        raise ValueError("Taban ve yükseklik pozitif olmalıdır")

    return (taban * yukseklik) / 2


def daire_alani(yaricap):
    """
    Dairenin alanını hesaplar.
    """
    if yaricap <= 0:
        raise ValueError("Yarıçap pozitif olmalıdır")

    return PI * yaricap ** 2