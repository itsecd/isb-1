alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Шаг шифровки: '))
itog = ''
with open("Text.txt", mode='r', encoding='utf-8') as T:
    with open('Encryption.txt', mode='w', encoding='utf-8') as ET:
        MyText = T.read().upper()
        for i in MyText:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_RU:
                 itog += alfavit_RU[new_mesto]
            else:
                itog += i
        print(itog)
        ET.write(itog)
