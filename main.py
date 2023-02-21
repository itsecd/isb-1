alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
New_word = ''
with open("MW.txt", mode='r', encoding='utf-8') as MW:
    with open('NW.txt', mode='w', encoding='utf-8') as NW:
        My = MW.read().upper()
        for i in My:
            place = alfavit_RU.find(i)
            new_place = place + 1
            if i in alfavit_RU:
                New_word += alfavit_RU[new_place]
            else:
                New_word += i
        NW.write(New_word)
