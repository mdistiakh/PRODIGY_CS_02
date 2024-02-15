def read_image(filename):
    with open(filename, 'rb') as file:
        image_data = file.read()
    return bytearray(image_data)


def write_image(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)


def encrypt_image(image_data, shift=10):
    encrypted = bytearray()
    for byte in image_data:
        encrypted_byte = (byte + shift) % 256
        encrypted.append(encrypted_byte)
    return encrypted


def decrypt_image(encrypted, shift=10):
    decrypted = bytearray()
    for byte in encrypted:
        decrypted_byte = (byte - shift) % 256
        decrypted.append(decrypted_byte)
    return decrypted


def main():
    try:
        image_path = input("Enter the path to the image file: ")
        image_data = read_image(image_path)

        shift = int(input("Enter the shift value for encryption and decryption: "))

        encrypted = encrypt_image(image_data, shift)
        write_image("encrypted_image.raw", encrypted)

        decrypted = decrypt_image(encrypted, shift)
        write_image("decrypted_image.raw", decrypted)

        print("Images encrypted and decrypted successfully.")
    
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
