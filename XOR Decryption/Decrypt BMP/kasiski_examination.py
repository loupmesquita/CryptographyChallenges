from collections import Counter


def kasiski_examination(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    # Find repeating sequences of 3 bytes and their distances
    sequences = {}
    for i in range(len(data) - 3):
        seq = data[i:i+3]
        if seq not in sequences:
            sequences[seq] = []
        sequences[seq].append(i)

    # Calculate the distances between repeating sequences and count their occurrences
    distances = []
    for seq, positions in sequences.items():
        for i in range(len(positions) - 1):
            distances.append(positions[i+1] - positions[i])
    distance_counts = Counter(distances)

    # Print the 10 most common distances
    for distance, count in distance_counts.most_common(10):
        print(f'Distance: {distance}, Count: {count}')

kasiski_examination('ch2.bmp')