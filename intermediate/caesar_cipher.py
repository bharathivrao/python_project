str = input("Enter a string: ")
shift = int(input("Enter the shift value (1-25): "))

if shift < 1 or shift > 25:
    print("Shift value must be between 1 and 25.")
    exit(1)

base = ord('A')
new_str = ""
for char in str:
    shifted_char = (ord(char) - base + shift) % 26 + base
    new_str += chr(shifted_char)
print(f"Shifted string: {new_str}")