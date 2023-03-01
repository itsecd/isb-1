def create_key(alp: str, offset: int) -> str:
    alp = list(alp)
    for i in range (abs(offset)):
        alp.append(alp.pop(0))
    return ''.join(alp)

def save_text(text:str, filename:str) -> None:
    with open(f'{filename}.txt', 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = create_key(alphabet, 5)
    save_text(key, 'key1')