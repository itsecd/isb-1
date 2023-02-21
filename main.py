alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_Dec = ' ОИЕАНТСРВМЛДЯКПЗЫЬУЧЖГХФЙЮБЦШЩЭЪ'
New_word = ''
with open("MyText.txt", mode='r', encoding='utf-8') as MW:
    with open('Encryption.txt', mode='w', encoding='utf-8') as NW:
        My = MW.read().upper()
        for i in My:
            place = alfavit_RU.find(i)
            new_place = place + 1
            if i in alfavit_RU:
                New_word += alfavit_RU[new_place]
            else:
                New_word += i
        NW.write(New_word)
def freqIndexDic(text: str) -> dict:
    dic = dict()
    lst = list(set(text))
    for i in lst:
        dic[i] = text.count(i)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return dic

text = open("cod9.txt", "r", encoding="utf-8").read()
d = freqIndexDic(text)
