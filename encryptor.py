ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
CIPHER = 'БЯЫАГЖРТУЭХЩМЙИЬДОЧКЮВНЪШЕФСЦЛПЗ'


def read_text(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def write_text(file_name: str, text: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)


def encryptor(alphabet: str, key: str, text: str) -> str:
    text = text.upper()
    cipher = ''
    for word in text:
        if word in alphabet:
            cipher += key[alphabet.find(word)]
        else:
            cipher += word
    return cipher


if __name__ == "__main__":
    original_text = read_text('original_text.txt')
    my_cipher = encryptor(ALPHABET, CIPHER, original_text)
    write_text('ciphertext.txt', my_cipher)
