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

def decoding_text():
    """
    Расшифровка текста.
    """
    text2 = read_text('text2.txt')
    c = dict()
    for i in text2:
        c[i] = c.get(i, 0) + 1
    print(c)
    dec_text2 = text2.replace('-', ' ')
    dec_text2 = dec_text2.replace('E', 'О')
    dec_text2 = dec_text2.replace('2', 'И')
    dec_text2 = dec_text2.replace('0', 'Е')
    dec_text2 = dec_text2.replace('6', 'А')
    dec_text2 = dec_text2.replace('N', 'С')
    dec_text2 = dec_text2.replace('I', 'Т')
    dec_text2 = dec_text2.replace('W', 'Н')
    dec_text2 = dec_text2.replace('M', 'Р')
    dec_text2 = dec_text2.replace('8', 'В')
    dec_text2 = dec_text2.replace('Q', 'М')
    dec_text2 = dec_text2.replace('R', 'П')
    dec_text2 = dec_text2.replace('5', 'Д')
    dec_text2 = dec_text2.replace('\\', 'Л')
    dec_text2 = dec_text2.replace('3', 'З')
    dec_text2 = dec_text2.replace('/', 'К')
    dec_text2 = dec_text2.replace(';', 'Ы')
    dec_text2 = dec_text2.replace('`', 'Я')
    dec_text2 = dec_text2.replace('S', 'Ь')
    dec_text2 = dec_text2.replace('7', 'Б')
    dec_text2 = dec_text2.replace('T', 'Х')
    dec_text2 = dec_text2.replace('1', 'Й')
    dec_text2 = dec_text2.replace('K', 'Ч')
    dec_text2 = dec_text2.replace('O', 'У')
    dec_text2 = dec_text2.replace('Z', 'Ю')
    dec_text2 = dec_text2.replace('C', 'Щ')
    dec_text2 = dec_text2.replace('P', 'Ф')
    dec_text2 = dec_text2.replace('F', 'Ц')
    dec_text2 = dec_text2.replace('D', 'Ш')
    dec_text2 = dec_text2.replace('9', 'Г')
    dec_text2 = dec_text2.replace('X', 'Э')
    dec_text2 = dec_text2.replace('4', 'Ж')
    dec_text2 = dec_text2.replace('?', '.')
    write_text("dec_text2.txt", dec_text2)
    key2 = "'-' - пробел\n'E'- 'О'\n'6'- 'А'\n'N'- 'С'\n'I'- 'Т'\n'W'- 'Н'\n'M'- 'Р'\n'8'- 'В'\n'Q'- 'М'\n'R'- 'П'\n" \
           "'5'- 'Д'\n'\\'- 'Л'\n'3'- 'З'\n'/'- 'К'\n';'- 'Ы'\n'`'- 'Я'\n'S'- 'Ь'\n'7'- 'Б'\n'T'- 'Х'\n'1'- 'Й'\n" \
           "'K'- 'Ч'\n'O'- 'У'\n'O'- 'У'\n'Z'- 'Ю'\n'C'- 'Щ'\n'P'- 'Ф'\n'F'- 'Ц'\n'D'- 'Ш'\n'9'- 'Г'\n'X'- 'Э'\n" \
           "'4'- 'Ж'\n'?'- '.'"
    write_text("key2.txt", key2)

if __name__ == "__main__":
    encoding_text()
    decoding_text()
