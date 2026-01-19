str1 = input("Enter a string: ").lower()
str2 = input("Enter another string: ").lower()

for c in str1:
    if c not in str2 and c != ' ':
        print(f"'{c}' is not in the second string.")
        break
else:
    print("The strings are anagrams.")