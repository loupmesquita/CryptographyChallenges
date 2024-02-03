def get_bmp_size(filename):
    with open(filename, 'rb') as f:
        f.seek(2)  # Skip the first two bytes (BMP signature)
        size_bytes = f.read(4)  # Read the next four bytes (file size)
    size = int.from_bytes(size_bytes, 'little')  # Convert bytes to integer (little-endian)
    return size

filename = 'ch2.bmp'  # Replace with your BMP file name
size = get_bmp_size(filename)
print(f"The size of {filename} is {size} bytes ({size:02X} in hexadecimal).")