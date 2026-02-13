def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher Program ===")
choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == 'e':
    print("Encrypted message:", encrypt(message, shift))
elif choice == 'd':
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice")