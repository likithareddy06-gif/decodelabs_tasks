def process(text, shift, mode):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'e':
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
text = input("Enter text: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
output = process(text, shift, choice)
print("Result:", output)    