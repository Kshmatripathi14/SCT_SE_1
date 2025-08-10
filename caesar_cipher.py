# Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
if __name__ == "__main__":
    print("=== Caesar Cipher Program ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"\nEncrypted Message: {encrypted_text}")
    print(f"Decrypted Message: {decrypted_text}")
