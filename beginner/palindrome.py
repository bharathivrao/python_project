x = input("Enter a word or phrase: ")
end = len(x)
i = 0
palindrome = True
while i < end:
    if x[i] == x[end - i - 1]:
        i += 1
    else:
        palindrome = False
        break
print()
print('Palindrome' if palindrome else 'Not a palindrome')
