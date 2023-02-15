
def saveFile(str: str, fileName: str) -> None:
    with open(f'{fileName}.txt', 'w') as f:
        print(str, file=f)


def createKey(n: int) -> str:
    alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alph = list(alph)
    n = -n
    if n < 0:
        n = abs(n)
        for i in range(n):
            alph.append(alph.pop(0))
    else:
        for i in range(n):
            alph.insert(0, alph.pop())
    return alph


def encrypt(str: str, n: int):
    alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alph = alph.lower()
    ln = len(alph)
    res = []
    noAlph = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in str:
        if not l in noAlph:
            print(l)
            res.append(alph[(alph.find(l)+n) % ln])
        else:
            res.append(l)
    return res