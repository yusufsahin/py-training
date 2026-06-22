numbers = [1, 2, 3,4]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        print(numbers[i], numbers[j])
print("*"*40)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i], numbers[j])