numbers=[3,5,4,10,8,56,611,17]

tek_count=0
cift_count=0
for num in numbers:
    if num%2==0:
        cift_count+=1
    else:
        tek_count+=1
print("Çift sayi adedi : ",cift_count)
print("Tek sayi adedi : ",tek_count)