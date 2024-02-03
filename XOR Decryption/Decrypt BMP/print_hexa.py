def print_first_six_bytes(filename):
    with open(filename, 'rb') as f:
        bytes = f.read(6)
    print(bytes)

print_first_six_bytes('ch2.bmp')