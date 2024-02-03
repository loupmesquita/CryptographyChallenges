def get_header_data(filename):
    with open(filename, 'rb') as f:
        if f is None:
            print("Error opening file")
            return 1
        header_data = bytearray(f.read(1240))
    return header_data



header_data = get_header_data('basic4.webp')

#for i in range(20):
#    print(f"{header_data[i]:02X}")


target_header = bytearray([0x52, 0x49, 0x46, 0x5C, 0xE2, 0x00, 0x57, 0x45, 0x42, 0x50, 0x56, 0x38, 0x20])
# "RIFF" "SIZE" "WEBP" "VP8 "

# 0xF89A == real size of the bmp file 

found_key = [0]*15

# Try every possible one-byte key
for key in range(256):
    # XOR each byte of the header with the key
    b0 = header_data[0] ^ key
    b1 = header_data[1] ^ key
    b2 = header_data[2] ^ key
    b3 = header_data[3] ^ key
    b4 = header_data[4] ^ key
    b5 = header_data[5] ^ key
    b6 = header_data[6] ^ key
    b7 = header_data[7] ^ key
    b8 = header_data[8] ^ key
    b9 = header_data[9] ^ key
    b10 = header_data[10] ^ key
    b11 = header_data[11] ^ key
    b12 = header_data[12] ^ key
    b13 = header_data[13] ^ key
    b14 = header_data[14] ^ key
 

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
    if b3 == target_header[2]:
        print(f"byte 4: {key:02X} for xor byte {header_data[3]:02X}, b3 : {b3:02X}")
        found_key[3] = key
    if b4 == target_header[3]:
        print(f"byte 5: {key:02X} for xor byte {header_data[4]:02X}, b4 : {b4:02X}")
        found_key[4] = key
    if b5 == target_header[4]:
        print(f"byte 6: {key:02X} for xor byte {header_data[5]:02X}, b5 : {b5:02X}")
        found_key[5] = key
    if b6 == target_header[5]:
        print(f"byte 7: {key:02X} for xor byte {header_data[6]:02X}, b6 : {b6:02X}")
        found_key[6] = key
    if b7 == target_header[5]:
        print(f"byte 8: {key:02X} for xor byte {header_data[7]:02X}, b7 : {b7:02X}")
        found_key[7] = key
    if b8 == target_header[6]:
        print(f"byte 9: {key:02X} for xor byte {header_data[8]:02X}, b8 : {b8:02X}")
        found_key[8] = key
    if b9 == target_header[7]:
        print(f"byte 10: {key:02X} for xor byte {header_data[9]:02X}, b9 : {b9:02X}")
        found_key[9] = key
    if b10 == target_header[8]:
        print(f"byte 11: {key:02X} for xor byte {header_data[10]:02X}, b10 : {b10:02X}")
        found_key[10] = key
    if b11 == target_header[9]:
        print(f"byte 12: {key:02X} for xor byte {header_data[11]:02X}, b11 : {b11:02X}")
        found_key[11] = key
    if b12 == target_header[10]:
        print(f"byte 13: {key:02X} for xor byte {header_data[12]:02X}, b12 : {b12:02X}")
        found_key[12] = key
    if b13 == target_header[9]:
        print(f"byte 14: {key:02X} for xor byte {header_data[13]:02X}, b13 : {b13:02X}")
        found_key[13] = key
    if b14 == target_header[11]:
        print(f"byte 15: {key:02X} for xor byte {header_data[14]:02X}, b14 : {b14:02X}")
        found_key[14] = key
        

#for i in range(12):
#    print(f"{found_key[i]:02X}")

with open("basic4.webp", "rb") as bmp_file, open("decrypted.webp", "wb") as decrypted_file:
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
        
    print("File decrypted successfully!")