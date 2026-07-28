numbers=[5,3,8,1]

n=len(numbers)

for i in range(n):
    for j in range(0,n-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            print(numbers[j],numbers[j+1])
            print(numbers)
print("-"*40)
print("bubble sort")
print(numbers)
