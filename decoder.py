from encryptor import read_text
ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '


def frequency_analysis(alphabet: str, text: str) -> dict:
    frequencies = [0] * len(alphabet)
    for word in text:
        if word in alphabet:
            frequencies[alphabet.find(word)] += 1
    word_count = sum(frequencies)
    for i in range(len(frequencies)):
        frequencies[i] /= word_count
    word_frequencies = dict(zip(alphabet, frequencies))
    print(word_frequencies)
    return word_frequencies


if __name__ == "__main__":
    ciphertext = read_text('cod7.txt')
    text_alphabet = list(set(ciphertext))
    text_alphabet.remove('\n')
    text_alphabet = "".join(text_alphabet)
    frequency_analysis(text_alphabet, ciphertext)
