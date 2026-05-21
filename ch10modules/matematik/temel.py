"""
temel.py

Bu modil temel matematik işlemlerini içerir.
Toplama, çıkarma, çarpma ve bölme fonksiyonları vardır.
"""

def topla(a, b):
    """
    İki sayıyı toplar.
    :param a: birinci sayı
    :param b: ikinci sayi
    :return:a+b
    """
    return a+b

def cikar(a,b):
    """
    İki sayıyı çıkarır.
    :param a: birinci sayı
    :param b: ikinci sayi
    :return:a-b
    """
    return a-b

def carp(a,b):
    """
    İki sayıyı çarpar.
    :param a: birinci sayı
    :param b: ikinci sayi
    :return:a-b
    """
    return a*b

def bol(a,b):
    """
    İki sayıyı böler.
    :param a: birinci sayı
    :param b: ikinci sayi
    :return:a/b
    """
    if b==0:
        raise ValueError("Sıfıra bölme yapılamaz")
    return a/b