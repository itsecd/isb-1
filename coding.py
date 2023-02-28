ALF = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "


def find_number(text: str) -> list:
    new_text = []
    for itim in text:
        new_text.append(ALF.find(itim.upper())+1)
    return new_text


def sum_number(text_number: list, key_number: list) -> list:
    new_text = []
    count = 0
    for word in text_number:
        if count >= len(key_number):
            count = 0
        word = word + key_number[count]
        if (word > len(ALF)):
            word = word - len(ALF)
        new_text.append(word)
        count += 1
    return new_text


def spy(text_number: list) -> str:
    spy_text = ""
    for word in text_number:
        spy_text += ALF[word-1]
    # print(spy_text)
    return spy_text.lower()


def encryption(text: str, key: list) -> str:
    text_number = find_number(text)
    key_number = find_number(key)
    new_text_number = sum_number(text_number, key_number)
    return spy(new_text_number)


if __name__ == "__main__":
    file = open("text.txt", "r")
    text = file.read()
    file.close()
    new_file = open("new_text.txt", "w+")
    new_file.write(encryption(text, "кодирование"))
    new_file.close()
