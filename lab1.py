
def saveFile(str: str, fileName: str) -> None:
    with open(f'{fileName}.txt', 'w') as f:
        print(str, file=f)
