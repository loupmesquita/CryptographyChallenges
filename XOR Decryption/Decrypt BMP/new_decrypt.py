def get_header_data(filename):
    with open(filename, 'rb') as f:
        if f is None:
            print("Error opening file")
            return 1
        header_data = bytearray(f.read(54))
    return header_data



header_data = get_header_data('ch2.bmp')

for i in range(6):
    print(f"{header_data[i]:02X}")


target_header = bytearray([0x42, 0x4d, 0x9a, 0xf8, 0x00])

# 0xF89A == real size of the bmp file 

# Assuming header_data and target_header are defined
found_key = [0]*6

# Try every possible one-byte key
for key in range(256):
    # XOR each byte of the header with the key
    b0 = header_data[0] ^ key
    b1 = header_data[1] ^ key
    b2 = header_data[2] ^ key
    b3 = header_data[3] ^ key
    b4 = header_data[4] ^ key
    b5 = header_data[5] ^ key

    # Check if the decrypted BMP header matches the target header
    if b0 == target_header[0]:
        print(f"byte 1: {key:02X} for xor byte {header_data[0]:02X}, b0 : {b0:02X}")
        found_key[0] = key
    if b1 == target_header[1]:
        print(f"byte 2: {key:02X} for xor byte {header_data[1]:02X}, b1 : {b1:02X}")
        found_key[1] = key
    if b2 == target_header[2]:
        print(f"byte 3: {key:02X} for xor byte {header_data[2]:02X}, b2 : {b2:02X}")
        found_key[2] = key
    if b3 == target_header[3]:
        print(f"byte 4: {key:02X} for xor byte {header_data[3]:02X}, b3 : {b3:02X}")
        found_key[3] = key
    if b4 == target_header[4]:
        print(f"byte 5: {key:02X} for xor byte {header_data[4]:02X}, b4 : {b4:02X}")
        found_key[4] = key
    if b5 == target_header[4]:
        print(f"byte 6: {key:02X} for xor byte {header_data[5]:02X}, b5 : {b5:02X}")
        found_key[5] = key

for i in range(6):
    print(f"{found_key[i]:02X}")

with open("ch2.bmp", "rb") as bmp_file, open("decrypted.bmp", "wb") as decrypted_file:
    byte = bmp_file.read(1)
    key_index = 0
    while byte:
        # XOR decryption with the current key byte
        decrypted_byte = bytes([byte[0] ^ found_key[key_index]])
        key_index = (key_index + 1) % len(found_key)  # Cycle through the key

        # Write the decrypted byte to the output file
        decrypted_file.write(decrypted_byte)

        # Read the next byte
        byte = bmp_file.read(1)