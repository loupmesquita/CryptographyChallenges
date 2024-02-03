def get_header_data(filename):
    with open(filename, 'rb') as f:
        header_data = f.read(8)
    return [b for b in header_data]

header_data = get_header_data('basic4.webp')
print([f'{b:02x}' for b in header_data])