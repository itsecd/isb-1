alphabet_eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def encryption(step: int, message: str, lang: str) -> None:
    f = open("source_text1", mode='w', encoding='utf-8')
    f.write(message)
    f.close()
    result = ''
    if lang == '1':
        for i in message:
            place = alphabet_ru.find(i)
            new_place = place + step
            if i in alphabet_ru:
                result += alphabet_ru[new_place]
            else:
                result += i
    else:
        for i in message:
            place = alphabet_eu.find(i)
            new_place = place + step
            if i in alphabet_eu:
                result += alphabet_eu[new_place]
            else:
                result += i
    f = open("encrypted_text1", mode='w', encoding='utf-8')
    f.write(result)
    f.close()


if __name__ == '__main__':
    step = int(input('Шаг шифровки: '))
    message = input("Сообщение для шифровки: ").upper()
    print('Выберите язык : 1) RU  2) EU')
    lang = input()
    encryption(step, message, lang)
