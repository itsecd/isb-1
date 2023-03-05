def read_file(file_name):
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
        return file.read()


def save_file(file_name, text):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
        
        file.write('\n' + 'Зашифрованный текст:' + '\n'+ text)


def caesar_cipher(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            shifted_index = (index + shift) % len(alphabet)
            if char.isupper():
                result += alphabet[shifted_index].upper()
            else:
                result += alphabet[shifted_index]
        else:
            result += char
    return result


def caesar_cipher(text, shift):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += char
    return encrypted_text


def main():
    text = read_file('text1')
    new_text = caesar_cipher(text, 4)
    save_file('text1', new_text)


if __name__ == "__main__":
    main()
