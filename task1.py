symbols = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,-'

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
    #char_list = list(text.upper())
    key ={}
    for elem in symbols:
        position = symbols.find(elem)
        if position < 34:
            key[symbols[position]] = symbols[position+3]
        else:
            key[symbols[position]] = symbols[position-34]
    print(key)
    with open('key1.txt', 'w', encoding='utf-8') as file:
        file.write(str(key))
    return key
    

if __name__ == '__main__':
    key1()
    
