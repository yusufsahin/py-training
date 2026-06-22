numbers = [3, 7, 11, 15,6]
target = 9

# Bu listedeki iki sayı toplanınca target değerini veriyor mu?

# Çözüm 1 - Pahalı Çözüm
# Time Complexity: O(n²)
# Space Complexity: O(1)

print("Çözüm 1 - Pahalı Çözüm")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])


# Çözüm 2 - Daha Akıllı Çözüm
# Time Complexity: O(n)
# Space Complexity: O(n)

print("Çözüm 2 - Daha Akıllı Çözüm")

seen = set()

for number in numbers:
    needed = target - number

    if needed in seen:
        print(needed, number)
        break

    seen.add(number)

print("Seen:", seen)