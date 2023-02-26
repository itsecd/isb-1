import logging
from encryptor import read_text, write_text
ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '


def read_true_frequencies(file_name: str) -> dict:
    """
    The function reads frequencies from file with filename file_name.
    A file contains data in the format 'word-frequency'.

    :param file_name: name of file.
    :return: None.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except OSError as err:
        logging.warning(f'Во время чтения файла {file_name} произошла ошибка:\n{err}')
    true_frequencies = {}
    for line in lines:
        key, value = line.split('-')
        true_frequencies[key] = float(value)
    return true_frequencies


def create_alphabet(text: str, ignore_symbols: str) -> str:
    """
    The function create an alphabet for a text, ignoring symbols from the ignore_symbols.

    :param text: a text for creating alphabet.
    :param ignore_symbols: symbols, which should be ignored.
    :return: an alphabet.
    """
    alphabet = list(set(text))
    for character in ignore_symbols:
        alphabet.remove(character)
    alphabet = "".join(alphabet)
    return alphabet


def frequency_analysis(alphabet: str, text: str) -> dict:
    """
    The function does frequency analysis of a text, using an alphabet of this text.
    Symbols, which is not in an alphabet, will be ignored.

    :param alphabet: alphabet with symbols for frequency analysis.
    :param text: a text for frequency analysis.
    :return: a sorted dict with symbols as keys and frequencies as values.
    """
    frequencies = [0] * len(alphabet)
    for character in text:
        if character in alphabet:
            frequencies[alphabet.find(character)] += 1
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
    text_alphabet = create_alphabet(ciphertext, '\n')
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
        command = input('Введите команду: ')
        match command:
            case '0':
                is_open = False
            case '1':
                old_character = input('Введите букву, которую нужно заменить: ').upper()
                new_character = input('Введите букву, на которую нужно заменить: ').upper()
                tms = ''
                for i in range(len(ciphertext)):
                    if ciphertext[i] == old_character:
                        tms += new_character
                    else:
                        tms += current_text[i]
                current_text = tms
            case '-1':
                del_character = input('Введите букву, которую нужно удалить: ').upper()
                current_text = current_text.replace(del_character, '*')
            case 's':
                filename = input('Введите путь к файлу: ')
                write_text(filename, current_text)
        print('\n' * 50)
