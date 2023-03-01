def create_key(alp: str, offset: int) -> str:
    alp = list(alp)
    for i in range (abs(offset)):
        alp.append(alp.pop(0))
    return ''.join(alp)


if __name__ == '__main__':
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = create_key(alphabet)