def readFile (fileName: str) -> str:
    with open(f'{fileName}.txt', "r", encoding='utf-8') as file:
        return file.read()

def savefile (message: str, fileName: str) -> None:
    with open(f'{fileName}.txt', "w", encoding='utf-8') as file:
        file.write(message)