def read_text(filename: str) -> str:
    """
        Получение текста из файла.
    """
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        return file.read().upper()

def write_text(filename: str, text: str):
    """
        Запись текста в файл.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        file.write(text)

def encoding_text():
    """
    Шифрование текста.
    """
    rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    text1 = read_text('text1.txt')
    text1 = text1.lower()
    text2 = ""
    for i in text1:
        flag = False
        for j in range(len(rus_alph)):
             if i == rus_alph[j]:
                 if rus_alph[j] == " ":
                     text2 += "а"
                 else:
                    text2 += rus_alph[j+1]
                 flag = True
        if not flag:
            text2 += i
    write_text('enc_text1.txt', text2)


if __name__ == "__main__":
    encoding_text()
