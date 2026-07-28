def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        value = numbers[middle]

        if value == target:
            return middle

        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


numbers = [3, 7, 12, 18, 25, 40]

print(binary_search(numbers, 18))