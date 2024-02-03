from collections import Counter

def frequency_analysis(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    # Calculate the frequency of each byte value
    frequencies = Counter(data)

    # Print the 10 most common bytes and their frequencies
    for byte, freq in frequencies.most_common(10):
        print(f'Byte: {byte:02X}, Frequency: {freq}')

frequency_analysis('ch2.bmp')