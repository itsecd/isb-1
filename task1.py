SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,-'


def readFile (fileName: str) -> str:
    '''Reading data from a file'''
    with open(f'{fileName}.txt', "r", encoding='utf-8') as file:
        return file.read()


def savefile (text: str, fileName: str) -> None:
    '''Writing data to a file'''
    with open(f'{fileName}.txt', "w", encoding='utf-8') as file:
        file.write(text)


def key1() -> dict:
    '''Creating a key1 by shifting the original symbols and saving it to a file'''
    key ={}
    for elem in SYMBOLS:
        position = SYMBOLS.find(elem)
        if position < 34:
            key[SYMBOLS[position]] = SYMBOLS[position+3]
        else:
            key[SYMBOLS[position]] = SYMBOLS[position-34]
    print(key)
    with open('key1.txt', 'w', encoding='utf-8') as file:
        file.write(str(key))
    return key
    

def encryption(fileName: str) -> None:
    '''Encrypts the text and saves it in a file'''
    text = readFile(fileName).upper()
    key = key1()
    result = text.translate(str.maketrans(key))
    savefile(result, 'task1_decrypted')


if __name__ == '__main__':
    encryption('task1_original')
    
