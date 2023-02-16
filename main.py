alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
dict = {' ': 0.128675, 'О': 0.096456, 'И': 0.075312, 'Е': 0.072292, 'А': 0.064841, 'Н': 0.061820, 'Т': 0.061619, 'С': 0.051953, 'Р': 0.040677, 'В': 0.039267, 'М': 0.029803, 'Л': 0.029400, 'Д': 0.026983, 'Я': 0.026379, 'К': 0.025977, 'П': 0.024768,
        'З': 0.015908, 'Ы': 0.015707, 'Ь': 0.015103, 'У': 0.013290, 'Ч': 0.011679, 'Ж': 0.010673, 'Г': 0.009867, 'Х': 0.008659, 'Ф': 0.007249, 'Й': 0.006847, 'Ю': 0.006847, 'Б': 0.006645, 'Ц': 0.005034, 'Ш': 0.004229, 'Щ': 0.003625, 'Э': 0.002416, 'Ъ': 0.000000}


def encryption(message: str) -> None:
    f = open("source_text.txt", mode='w', encoding='utf-8')
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
    f = open("key1.txt", mode='w', encoding='utf-8')
    f.write(key)
    f.close()


def decoding() -> None:
    f = open("cod8.txt", mode='r', encoding='utf-8')
    new_dict = {}
    text = f.read()
    length = len(text)
    tmp = []
    for elem in text:
        count = 0
        if elem not in tmp:
            print()
            for j in text:
                if j == elem:
                    count += 1
            new_dict[elem] = count / length
            tmp.append(elem)
    f.close()
    result = sorted(new_dict.items(), key=lambda t: t[1], reverse=True)
    new_tmp = ''
    tmp_dic = {}
    for i in text:
        if i == ' ':
            new_tmp += 'а'
            if i not in tmp_dic:
                tmp_dic[' '] = 'a'
        elif i == 'Я':
            new_tmp += ' '
            if i not in tmp_dic:
                tmp_dic['Я'] = ' '
        elif i == 'Д':
            new_tmp += 'е'
            if i not in tmp_dic:
                tmp_dic['Д'] = 'е'
        elif i == '4':
            new_tmp += 'о'
            if i not in tmp_dic:
                tmp_dic['4'] = 'о'
        elif i == 'Ъ':
            new_tmp += 'ь'
            if i not in tmp_dic:
                tmp_dic['Ъ'] = 'ь'
        elif i == 't':
            new_tmp += 'и'
            if i not in tmp_dic:
                tmp_dic['t'] = 'и'
        elif i == 'Е':
            new_tmp += 'ж'
            if i not in tmp_dic:
                tmp_dic['Е'] = 'ж'
        elif i == 'r':
            new_tmp += 'з'
            if i not in tmp_dic:
                tmp_dic['r'] = 'з'
        elif i == 'Л':
            new_tmp += 'м'
            if i not in tmp_dic:
                tmp_dic['Л'] = 'м'
        elif i == 'Й':
            new_tmp += 'к'
            if i not in tmp_dic:
                tmp_dic['Й'] = 'к'
        elif i == '1':
            new_tmp += 'г'
            if i not in tmp_dic:
                tmp_dic['1'] = 'г'
        elif i == 'Х':
            new_tmp += 'ч'
            if i not in tmp_dic:
                tmp_dic['Х'] = 'ч'
        elif i == '2':
            new_tmp += 'д'
            if i not in tmp_dic:
                tmp_dic['2'] = 'д'
        elif i == 'К':
            new_tmp += 'л'
            if i not in tmp_dic:
                tmp_dic['К'] = 'л'
        elif i == 'М':
            new_tmp += 'н'
            if i not in tmp_dic:
                tmp_dic['М'] = 'Н'
        elif i == 'У':
            new_tmp += 'х'
            if i not in tmp_dic:
                tmp_dic['У'] = 'х'
        elif i == 'О':
            new_tmp += 'р'
            if i not in tmp_dic:
                tmp_dic['О'] = 'р'
        elif i == 'П':
            new_tmp += 'с'
            if i not in tmp_dic:
                tmp_dic['П'] = 'с'
        elif i == 'А':
            new_tmp += 'б'
            if i not in tmp_dic:
                tmp_dic['А'] = 'б'
        elif i == 'Ч':
            new_tmp += 'щ'
            if i not in tmp_dic:
                tmp_dic['Ч'] = 'щ'
        elif i == '>':
            new_tmp += 'у'
            if i not in tmp_dic:
                tmp_dic['>'] = 'у'
        elif i == 'Р':
            new_tmp += 'т'
            if i not in tmp_dic:
                tmp_dic['р'] = 'т'
        elif i == 'Б':
            new_tmp += 'в'
            if i not in tmp_dic:
                tmp_dic['Б'] = 'в'
        elif i == 'И':
            new_tmp += 'й'
            if i not in tmp_dic:
                tmp_dic['И'] = 'Й'
        elif i == 'Ы':
            new_tmp += 'ю'
            if i not in tmp_dic:
                tmp_dic['Ы'] = 'ю'
        elif i == 'Щ':
            new_tmp += 'ы'
            if i not in tmp_dic:
                tmp_dic['Щ'] = 'ы'
        elif i == 'Т':
            new_tmp += 'ф'
            if i not in tmp_dic:
                tmp_dic['Т'] = 'ф'
        elif i == 'Ь':
            new_tmp += 'я'
            if i not in tmp_dic:
                tmp_dic[' Ь'] = 'я'
        elif i == 'Ц':
            new_tmp += 'ш'
            if i not in tmp_dic:
                tmp_dic['Ц'] = 'ш'
        elif i == '5':
            new_tmp += 'п'
            if i not in tmp_dic:
                tmp_dic['5'] = 'п'
        elif i == 'w':
            new_tmp += 'э'
            if i not in tmp_dic:
                tmp_dic['w'] = 'э'
        elif i == 'Ф':
            new_tmp += 'ц'
            if i not in tmp_dic:
                tmp_dic['Ф'] = 'ц'
        else:
            new_tmp += i
    f = open("key2.txt", mode='w', encoding='utf-8')
    f.write(str(tmp_dic))
    f.close()
    f = open("decrypted_text.txt", mode='w', encoding='utf-8')
    f.write(new_tmp)
    f.close()


if __name__ == '__main__':
    print('Шаг шифровки: 1\nСообщение для шифровки: ')
    new_text = input().upper()
    encryption(new_text)
    new_key = key()
    decoding()
