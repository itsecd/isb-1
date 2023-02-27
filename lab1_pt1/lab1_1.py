

def encrypt(text: str) -> str:
    print(len(text))
    text = text.lower()
    
    alpha = list(' абвгдежзийклмнопрстуфхцчшщъыьэюя')
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('–', '')
    text = text.replace(':', '')
    text = text.replace('?', '')
    text = text.replace('«', '')
    text = text.replace('»', '')
    text = text.replace('-', '')
    res = ''
    for sym in text:

        res += alpha[(alpha.index(sym) + 2)%len(alpha)]
    print(res)
    return (res)



if __name__ == "__main__":
    fileName = 'text.txt'
    text = ''
    with open( fileName, mode='r', encoding="utf-8") as f:
        text = f.read()
    

    enc_text = encrypt(text)