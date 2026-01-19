str = input("Enter a string: ")
str_arr = str.split(" ")
max = 0
max_str = ""
for word in str_arr:
    if len(word) > max:
        max = len(word)
        max_str = word

print(f"Max word is {max_str} with length {max}")