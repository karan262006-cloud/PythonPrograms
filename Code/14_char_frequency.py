def char_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency
