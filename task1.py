def encryption(message: str) -> str:
    alphabet =  "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
    key = 1
    new_message = ""
    for i in message:
        place = alphabet.find(i)
        if place == 64:
            new_place = 0
        elif place == 65:
            new_place = 1
        else: 
            new_place = place + 2*key
        if i in alphabet:
            new_message += alphabet[new_place]
        else:
            new_message += i
    return new_message


def get_message() -> str:
    file = open("oib_lab1/task1_text.txt", "r", encoding = "utf-8")
    text = file.read()
    file.close()
    return text


def new_file(new_message: str) -> None:
    new_file = open("oib_lab1/task1_encrypt_text.txt", "w+", encoding = "utf-8")
    new_file.write(new_message)
    new_file.close()


if __name__ == "__main__":
    message = get_message()
    encrypt_text = encryption(message)
    new_file(encrypt_text)
