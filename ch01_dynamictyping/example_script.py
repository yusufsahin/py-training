#!/usr/bin/env python3
#Shebang Line Dosyanın en üstünde bulunabilir.
#Özellikle Linux/macOS ortamında script’in
# hangi Python yorumlayıcısıyla çalıştırılacağını belirtir.

"""
Bu bir Modül Docstring
example_script.py

Bu script kullanıcıyı selamlar ve o anki tarihi/saat bilgisini gösterir.
Aynı zamanda tipik bir Python script yapısını örnekler.
"""
#importlar / Başka modülleri veya kütüphaneleri içe aktarmak için kullanılır.
#Hazır Python modüllerini kullanmanı sağlar.
#Kendi yazdığın modülleri de import edebilirsin.
import sys
from datetime import datetime

#fonksiynalr
def greet(name):
    """Verilen isme göre selamlama mesajı döndürür."""
    return f"Merhaba, {name}!"


def get_current_time():
    """Geçerli tarih ve saati okunabilir formatta döndürür."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#main fonk 
def main():
    """Programın ana çalışma akışı."""
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("Adınızı girin: ")

    print(greet(name))
    print(f"Şu anki zaman: {get_current_time()}")
    print(greet(__doc__))
    print(__doc__)


if __name__ == "__main__":
    main()