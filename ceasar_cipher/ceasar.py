def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) + shift - base) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - base) % 26 + base)
        else:
            result += char

    return result

# Dynamic input for encryption
data = input("Encrypt\nInput data: ")
key = int(input("Input key (shift): "))
encrypted_text = caesar_cipher(data, key, mode='encrypt')
print("Output (Encrypted):", encrypted_text)

data = input("\nDecrypt\nInput data: ")
key = int(input("Input key (shift): "))
decrypted_text = caesar_cipher(data, key, mode='decrypt')
print("Output (Decrypted):", decrypted_text)
