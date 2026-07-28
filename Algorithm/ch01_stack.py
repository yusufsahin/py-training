from operator import truediv

text="({[]})"

stack=[]

valid=True
pairs={")":"(","}":"{","]":"["}

print("Kontrol edilen metin:", text)
print("Başlangıç stack:", stack)
print("-" * 40)

for char in text:
    print(f"Okunan karakter: {char}")
    print(f"İşlem öncesi stack: {stack}")

    if char in "({[":
        stack.append(char)
        print("Açılış parantezi bulundu.")
        print(f"{char} stack'e eklendi.")
        print(f"İşlem sonrası stack: {stack}")

    elif char in ")}]":
        print("Kapanış parantezi bulundu.")

        if not stack:
            print("HATA: Stack boş.")
            print("Bu kapanış parantezinin açılışı yok.")
            valid=False
            break
        last=stack.pop()

        print(f"Stack'ten çıkarılan son açılış parantezi: {last}")
        print(f"{char} karakterinin beklediği açılış: {pairs[char]}")

        if last != pairs[char]:
            print("HATA: Parantezler eşleşmedi.")

            valid=False
            break
    print("-" * 40)
if stack:
    print("HATA: Stack boş değil.")
    print("Kapanmamış açılış parantezleri:", stack)

    valid = False
else:
    print("Stack boş. Açılan bütün parantezler kapatıldı.")

print("-" * 40)
print("Sonuç:", valid)