def count_it(sequence):
    freq = {}
    for char in sequence:
        num = int(char)
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    result = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3])
    return result

sequence = "1234567890123456789012345678901234567890"
result = count_it(sequence)
print(result)
