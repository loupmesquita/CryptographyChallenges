import os

def get_file_size(filename):
    return os.path.getsize(filename)

filename = 'basic4.webp'  # Replace with your file name
size = get_file_size(filename)
print(f"The size of {filename} is {size} bytes.")