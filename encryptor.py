ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
CIPHER_KEY = 'БЯЫАГЖРТУЭХЩМЙИЬДОЧКЮВНЪШЕФСЦЛПЗ'


def read_text(file_name: str) -> str:
    """
    The function write text in file with filename file_name.

    :param file_name: name of file.
    :return: text from file.
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def write_text(file_name: str, text: str) -> None:
    """
    The function write text in file with filename file_name.

    :param file_name: name of file.
    :param text: text for writing.
    :return: None.
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)


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
    for word in text:
        if word in alphabet:
            cipher += cipher_key[alphabet.find(word)]
        else:
            cipher += word
    return cipher


if __name__ == "__main__":
    original_text = read_text('original_text.txt')
    my_cipher = encryptor(ALPHABET, CIPHER_KEY, original_text)
    write_text('ciphertext.txt', my_cipher)
