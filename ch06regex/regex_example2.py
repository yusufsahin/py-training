"""
Regex ile metin içinden desen yakalama örnekleri.
Not: E-posta, URL, TC vb. için regex pratikte yaklaşık eşleşmedir;
    üretimde ek doğrulama (parser, checksum, resmi API) tercih edilir.
"""

import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (OSError, ValueError):
        pass

ORNEK_METIN = """
İletişim: ahmet.yilmaz@ornek.com, destek@firma.co.tr
Tel: +90 532 123 45 67, 0212 555 8899, 0555-444-3322
TC: 10000000146 (geçerli örnek kontrol algoritması ile doğrulanmalı)
Konum: enlem 41.0082° boylam 28.9784 veya 41.0082 N, 28.9784 E
Ağ: sunucu 192.168.1.1, gateway 10.0.0.1, IPv6 2001:0db8:0000:0000:0000:0000:0000:0001
Web: https://www.python.org/tr/ http://localhost:8080/api?v=1
HTML: <p class="x">Merhaba <b>dünya</b>!</p><br/><script>alert(1)</script>
"""


def bul(pattern: str, metin: str, aciklama: str) -> None:
    print(f"\n--- {aciklama} ---")
    print("Desen:", pattern)
    for m in re.finditer(pattern, metin, re.IGNORECASE | re.VERBOSE):
        print(" ", m.group(0))


def main() -> None:
    t = ORNEK_METIN

    # E-posta (yaygın pratik desen; tüm RFC kurallarını tek regex ile kapsamaz)
    email_re = r"""
        \b
        [a-z0-9._%+-]+
        @
        [a-z0-9.-]+
        \.
        [a-z]{2,}
        \b
    """
    bul(email_re, t, "E-posta")

    # Türkiye telefonu: +90, 0 ile başlayan sabit/mobil, boşluk/tire toleransı
    tel_re = r"""
        (?:
            \+90\s?0?\s?5\d{2}\s?\d{3}\s?\d{2}\s?\d{2}
          | 0\s?5\d{2}\s?[\s-]?\d{3}\s?[\s-]?\d{2}\s?[\s-]?\d{2}
          | 0\s?[2-4]\d{2}\s?[\s-]?\d{3}\s?[\s-]?\d{2}\s?[\s-]?\d{2}
        )
    """
    bul(tel_re, t, "Telefon (Türkiye odaklı yaklaşık)")

    # TC Kimlik No: 11 hane, ilk hane 0 olamaz (yakalama için; geçerlilik ayrı doğrulanır)
    tc_re = r"\b[1-9]\d{10}\b"
    bul(tc_re, t, "TC Kimlik numarası (11 hane, 0 ile başlamaz)")

    # Enlem / boylam (ondalık derece; isteğe bağlı yön harfi)
    koordinat_re = r"""
        (?:
            enlem\s*[-+]?\d{1,2}(?:\.\d+)?(?:\s*°)?(?:\s*[Nn])?
            \s*,?\s*
            boylam\s*[-+]?\d{1,3}(?:\.\d+)?(?:\s*°)?(?:\s*[EeWw])?
          | [-+]?\d{1,2}(?:\.\d+)?\s*°?\s*[Nn]\s*,\s*[-+]?\d{1,3}(?:\.\d+)?\s*°?\s*[EeWw]
        )
    """
    bul(koordinat_re, t, "Enlem ve boylam")

    # IPv4
    ipv4_re = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b"
    bul(ipv4_re, t, "IPv4 adresi")

    # IPv6 — tam (genişletilmiş) yazım; :: kısaltması için ipaddress modülü daha güvenilir
    ipv6_re = r"\b(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4}\b"
    bul(ipv6_re, t.lower(), "IPv6 adresi (8 grup, genişletilmiş biçim)")

    # http/https URL (sondaki noktalama hariç)
    url_re = r"https?://[\w./?#=&:%~-]+"
    bul(url_re, t, "URL (http/https)")

    # HTML etiketlerini kaldırıp düz metin
    html = re.search(r"HTML:\s*(.+)", t, re.DOTALL)
    if html:
        ham = html.group(1).strip()
        scriptsiz = re.sub(
            r"<script\b[^>]*>.*?</script\s*>",
            " ",
            ham,
            flags=re.IGNORECASE | re.DOTALL,
        )
        etiketsiz = re.sub(r"<[^>]+>", " ", scriptsiz)
        bosluk_duzelt = re.sub(r"\s+", " ", etiketsiz).strip()
        print("\n--- HTML temizleme ---")
        print("Ham:", ham)
        print("Metin:", bosluk_duzelt)


if __name__ == "__main__":
    main()
