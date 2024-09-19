from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = img.load()  # Load pixel data

    # Get image dimensions
    width, height = img.size

    # Perform pixel swapping based on the key
    for i in range(0, width, key):
        for j in range(0, height, key):
            # Swap pixel values if within bounds
            if i+key < width and j+key < height:
                current_pixel = pixels[i, j]
                swap_pixel = pixels[i + key, j + key]
                pixels[i, j] = swap_pixel
                pixels[i + key, j + key] = current_pixel

    # Save the encrypted image
    img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Decrypt is same as encrypt since it's a swap operation
    encrypt_image(input_image_path, output_image_path, key)

# Set up image paths and key
input_image = "new.jpeg"  # Input image path (place the image in the same directory)
encrypted_image = "encrypted_image.jpeg"  # Encrypted image output
decrypted_image = "decrypted_image.jpeg"  # Decrypted image output
key = 10  # Key for swapping pixels (can be any number)

# Encrypt the image
encrypt_image(input_image, encrypted_image, key)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key)
