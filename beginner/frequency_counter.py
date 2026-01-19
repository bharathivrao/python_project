x = input("Enter a word or phrase: ")
x = x.lower()

frequency_counter = {}
for char in x:
    if char in frequency_counter:
        frequency_counter[char] += 1
    else:
        frequency_counter[char] = 1

print(frequency_counter)
