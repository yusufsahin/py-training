numbers = [8, 3, 12, 5, 9]

#Sol:  [8, 3]
#Sağ:  [12, 5, 9]

#Sonra iki sonucu karşılaştıralım:
#max(8, 12) = 12

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    middle = len(numbers) // 2
    left_half=numbers[:middle]
    right_half=numbers[middle:]
    left_max = find_max(left_half)
    right_max = find_max(right_half)
    return max(left_max, right_max)

print(find_max(numbers))