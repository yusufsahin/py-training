from ch01_bigo1 import target

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

target=13

left=0
right=len(numbers)-1

while left<=right:
    mid=(left+right)//2
    if numbers[mid]==target:
        print(numbers[left],numbers[mid])
        print("found")
        break
    elif numbers[mid]<target:
        left=mid+1
        print(numbers[left], numbers[mid])
    else:
        right=mid-1
        print(numbers[right], numbers[mid])