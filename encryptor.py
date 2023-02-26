import logging

logger = logging.getLogger()
logger.setLevel('INFO')
ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
CIPHER_KEY = 'БЯЫАГЖРТУЭХЩМЙИЬДОЧКЮВНЪШЕФСЦЛПЗ'


def read_text(file_name: str) -> str:
    """
    The function write text in file with filename file_name.

    :param file_name: name of file.
    :return: text from file.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
    except OSError as err:
        logging.warning(f'Во время чтения файла {file_name} произошла ошибка:\n{err}')
    return text


def write_text(file_name: str, text: str) -> None:
    """
    The function write text in file with filename file_name.

    :param file_name: name of file.
    :param text: text for writing.
    :return: None.
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
    except OSError as err:
        logging.warning(f'Во время записи в файл {file_name} произошла ошибка:\n{err}')


def encryptor(alphabet: str, cipher_key: str, text: str) -> str:
    """
    The function encrypts a text, replacing a symbol from an alphabet with the corresponding symbol from a cipher_key.
    If some symbol missing from an alphabet, it will not be replaced.

    :param alphabet: symbols, which is needed to be replaced.
    :param cipher_key: symbols, on which symbols from alphabet are replaced.
    :param text: original text for encryption.
    :return: ciphertext.
    """
    text = text.upper()
    cipher = ''
    for character in text:
        if character in alphabet:
            cipher += cipher_key[alphabet.find(character)]
        else:
            cipher += character
    return cipher


if __name__ == "__main__":
    original_text = read_text('task_1-original_text.txt')
    my_cipher = encryptor(ALPHABET, CIPHER_KEY, original_text)
    write_text('task_1-ciphertext.txt', my_cipher)
