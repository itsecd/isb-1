ALPHABETS = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def read_file(filename: str):
    with open(f'{filename}.txt', "r", encoding='utf-8') as file:
        return file.read()


def write_file(filename: str, text: str):
    with open(f'{filename}.txt', "w", encoding='utf-8') as file:
        file.write(text)


def substitutions() -> dict:
    dict1 = {}
    for letter in ALPHABETS:
        pos = ALPHABETS.find(letter)
        if pos < 28:
            dict1[letter] = ALPHABETS[pos + 3]
        else:
            dict1[letter] = ALPHABETS[pos - 28]
    with open("task1-key_value.txt", "w", encoding='utf-8') as f:
        f.write(str(dict1))
    return dict1


def encryption(filename: str):
    with open('task1-original_text.txt', "r", encoding='utf-8') as f:
        text = f.read().upper()
    dict1 = substitutions()
    text = text.translate(str.maketrans(dict1))
    write_file(filename, text)


if __name__ == "__main__":
    encryption("task1-encode")
