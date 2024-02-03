def get_header_data(filename):
    with open(filename, 'rb') as f:
        header_data = f.read(6)
    return [b for b in header_data]

header_data = get_header_data('sample.bmp')
print([f'{b:02x}' for b in header_data])