import logging
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,-'

def readFile (fileName: str) -> str:
    """
    The function write text in file with fileName
    :param fileName: name of file
    :return: data from file
    """
    try:
        with open(f'{fileName}.txt', "r", encoding='utf-8') as file:
            data = file.read()
    except OSError as err:
        logging.warning(f'Во время чтения файла {fileName} произошла ошибка:\n{err}')
    return data

def saveFile (data: str, fileName: str) -> None:
    """
    The function write text in file with fileName
    :param data: data for writing
    :param fileName: name of file
    :return: None.
    """
    try:
        with open(f'{fileName}.txt', "w", encoding='utf-8') as file:
            file.write(data)
    except OSError as err:
        logging.warning(f'Во время записи в файл {fileName} произошла ошибка:\n{err}')


def encoding_Key (fileName: str) -> None:
    with open(f'{fileName}.txt', "a", encoding='utf-8') as file:
        for i in range(len(SYMBOLS)):
            file.write(f"{SYMBOLS[i]} -> {SYMBOLS[i + 3 - len(SYMBOLS) * ((i + 3) // len(SYMBOLS))]}""\n")

def encryption(fileName: str) -> None:
    """
    Encrypts the text and saves it in a file
    :param fileName: name of file
    :return: None
    """
    result = ''
    step = 3
    text = readFile(fileName).upper()
    for character in text:
        i = 0
        while i < len(SYMBOLS):
            if character == SYMBOLS[i]:
                character_code = SYMBOLS[i + step - len(SYMBOLS) * ((i + step) // len(SYMBOLS))]
                break
            i += 1
        result += character_code
    saveFile(result, 'text_encrypted_1')

if __name__ == '__main__':
    encoding_Key('Key_1')
    encryption('original_text_1')