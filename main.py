alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
dict = {' ': 0.128675, 'О': 0.096456, 'И': 0.075312, 'Е': 0.072292, 'А': 0.064841, 'Н': 0.061820, 'Т': 0.061619, 'С': 0.051953, 'Р': 0.040677, 'В': 0.039267, 'М': 0.029803, 'Л': 0.029400, 'Д': 0.026983, 'Я': 0.026379, 'К': 0.025977, 'П': 0.024768,
        'З': 0.015908, 'Ы': 0.015707, 'Ь': 0.015103, 'У': 0.013290, 'Ч': 0.011679, 'Ж': 0.010673, 'Г': 0.009867, 'Х': 0.008659, 'Ф': 0.007249, 'Й': 0.006847, 'Ю': 0.006847, 'Б': 0.006645, 'Ц': 0.005034, 'Ш': 0.004229, 'Щ': 0.003625, 'Э': 0.002416, 'Ъ': 0.000000}


def encryption(message: str) -> None:
    f = open("source_text1", mode='w', encoding='utf-8')
    f.write(message)
    f.close()
    result = ''
    for i in message:
        place = alphabet_ru.find(i)
        new_place = place + 1
        if i in alphabet_ru:
            if new_place == 33:
                result += 'А'
            else:
                result += alphabet_ru[new_place]
        else:
            result += i
    f = open("encrypted_text1", mode='w', encoding='utf-8')
    f.write(result)
    f.close()


def key() -> None:
    key = ''
    for elem in alphabet_ru:
        place = alphabet_ru.find(elem)
        new_step = place + 1
        if new_step == 33:
            key += 'A'
        else:
            key += alphabet_ru[new_step]
    f = open("key1", mode='w', encoding='utf-8')
    f.write(key)
    f.close()


def decoding() -> None:
    f = open("cod8.txt", mode='r', encoding='utf-8')
    new_dict = {}
    text = f.read()
    text = text.upper()
    length = len(text)
    for elem in text:
        count = 0
        if elem not in new_dict:
            for j in text:
                if j == elem:
                    count += 1
            new_dict[elem] = count / length
    f.close()
    result = sorted(new_dict.items(), key=lambda t: t[1], reverse=True)
    print(result)


if __name__ == '__main__':
    print('Шаг шифровки: 1')
    message = input("Сообщение для шифровки: ").upper()
    encryption(message)
    new_key = key()
    decoding()
