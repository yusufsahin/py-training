#Kaç tane var sorusunun cevabı

text="banana"
freq={}

for char in text:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] += 1
print(freq)

most_common=None
max_count=0

for number in freq:
    if freq[number] > max_count:
        max_count = freq[number]
        most_common = number
print(most_common,max_count)
