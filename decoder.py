from encryptor import read_text
ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '


def read_true_frequencies(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    true_frequencies = {}
    for line in lines:
        key, value = line.split('-')
        true_frequencies[key] = float(value)
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
    for index in range(len(frequencies)):
        frequencies[index] /= word_count
    word_frequencies = dict(zip(alphabet, frequencies))
    sorted_word_frequencies = {}
    sorted_keys = sorted(word_frequencies, key=word_frequencies.get)
    sorted_keys = sorted_keys[::-1]
    for key in sorted_keys:
        sorted_word_frequencies[key] = word_frequencies[key]
    return sorted_word_frequencies


if __name__ == "__main__":
    ciphertext = read_text('cod7.txt')
    text_alphabet = create_alphabet(ciphertext)
    russian_frequencies = list(read_true_frequencies('true_frequencies.txt').items())
    ciphertext_frequencies = list(frequency_analysis(text_alphabet, ciphertext).items())
    current_text = ''
    for symbol in ciphertext:
        if symbol != '\n':
            current_text += '*'
        else:
            current_text += symbol
    is_open = True
    while is_open:
        print("частота в русском языке --> частота шифра")
        for i in range(min(len(ciphertext_frequencies), len(russian_frequencies))):
            print(f'{russian_frequencies[i][0]} ({russian_frequencies[i][1]}) --> '
                  f'{ciphertext_frequencies[i][0]} ({ciphertext_frequencies[i][1]})')
        print(ciphertext)
        print(current_text)
        print("Введите команду: ", end='')
        command = int(input())
        if command == 0:
            is_open = False
        elif command == 1:
            pass
        elif command == -1:
            pass
        print('\n' * 50)
