numbers = [10,25,43,42,7,90,20]
#Liste içinde 42 var mı?


target = 42
found = False

#for i in range(len(numbers)):
#    if numbers[i] == target:
#        found = True
#        break

for number in numbers:
    if number == target:
        found = True
        break
print(found)