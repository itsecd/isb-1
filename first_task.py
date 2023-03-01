def create_key(alp: str, offset: int) -> str:
    alp = list(alp)
    for i in range(abs(offset)):
        alp.append(alp.pop(0))
    return "".join(alp)


def save_text(text: str, filename: str) -> None:
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(text)


def encryption(text: str, alp: str, key: str) -> str:
    offset = 0
    symbols = "1234567890!@#$%^&*()?\/[]{}()=-.,; :'\""
    key = list(key)
    for letter in list(alp):
        if letter == key[0]:
            break
        offset += 1
    result = []
    alp = alp.lower()
    text = text.lower()
    length = len(alp)
    for letter in text:
        if not letter in symbols:
            result.append(alp[(alp.find(letter) + offset) % length])
        else:
            result.append(letter)
    return "".join(result)


if __name__ == "__main__":
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key = create_key(alphabet, 5)
    save_text(key, "key1")
    with open("text_first.txt", "r", encoding="utf-8") as f:
        topic = f.read()
    encrypted_text = encryption(topic, alphabet, key)
    save_text(encrypted_text, "encrypted_text_first")
