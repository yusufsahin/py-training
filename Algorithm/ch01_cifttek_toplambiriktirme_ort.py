numbers=[3,5,4,10,8,56,611,17]
#Listedeki çift sayıları ve tek sayıların ortalaması nedir
tek_toplam=0
tek_count=0
cift_toplam=0
cift_count=0
for num in numbers:
    if num%2==0:
        cift_toplam+=num
        cift_count+=1
    else:
        tek_toplam+=num
        tek_count+=1
print("Çift sayiları ortalaması : ",cift_toplam/cift_count)
print("Tek sayiların ortalaması : ",tek_toplam/tek_count)
