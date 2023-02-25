from encryptor import read_text
ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '


def read_true_frequencies(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    true_frequencies = {}
    for line in lines:
        key, value = line.split()
        true_frequencies[key] = value
    return true_frequencies


def create_alphabet(text: str):
    alphabet = list(set(text))
    alphabet.remove('\n')
    alphabet = "".join(alphabet)
    return alphabet


def frequency_analysis(alphabet: str, text: str) -> dict:
    frequencies = [0] * len(alphabet)
    for word in text:
        if word in alphabet:
            frequencies[alphabet.find(word)] += 1
    word_count = sum(frequencies)
    for i in range(len(frequencies)):
        frequencies[i] /= word_count
    word_frequencies = dict(zip(alphabet, frequencies))
    sorted_word_frequencies = {}
    sorted_keys = sorted(word_frequencies, key=word_frequencies.get)
    sorted_keys = sorted_keys[::-1]
    for key in sorted_keys:
        sorted_word_frequencies[key] = word_frequencies[key]
    print(sorted_word_frequencies)
    return sorted_word_frequencies


if __name__ == "__main__":
    ciphertext = read_text('cod7.txt')
    text_alphabet = create_alphabet(ciphertext)
    print(read_true_frequencies('true_frequencies.txt'))
    frequency_analysis(text_alphabet, ciphertext)
