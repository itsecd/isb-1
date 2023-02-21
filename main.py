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
text = text.replace("-", " ")
text = text.replace("e", "о")
text = text.replace("0", "е")
text = text.replace("2", "и")
text = text.replace("6", "а")
text = text.replace("n", "с")
text = text.replace("i", "т")
text = text.replace("w", "н")
text = text.replace("m", "р")
text = text.replace("8", "в")
text = text.replace("q", "м")
text = text.replace("r", "п")
text = text.replace("5", "д")
text = text.replace("\\", "л")
text = text.replace("3", "з")
text = text.replace("/", "к")
text = text.replace(";", "ы")
text = text.replace("`", "я")
text = text.replace("s", "ь")
text = text.replace("7", "б")
text = text.replace("t", "х")
text = text.replace("1", "й")
text = text.replace("k", "ч")
text = text.replace("o", "у")
text = text.replace("z", "ю")
text = text.replace("c", "щ")
text = text.replace("p", "ф")
text = text.replace("f", "ц")
text = text.replace("d", "ш")
text = text.replace("9", "г")
text = text.replace("x", "э")
text = text.replace("4", "ж")
text = text.replace("?", ".")
file = open('Decoding.txt', mode="w", encoding="UTF-8")
file.write(text)
file.close()
f = open('Key.txt', mode="w", encoding="UTF-8")
f.write("- : Space\ne : о\n0 : е\n2 : и\n6 : а\nn : с\ni : т\nw : н\nm : р\n8 : в\nq : м\nr : п\n5 : д\n\\ : л\n3 : з"
        "\n/ : к\n; : ы\n` : я\ns : ь\n7 : б\nt : х\n1 : й\nk : ч\no : у\nz : ю\nc : щ\np : ф\nf : ц\nd : ш\n9 : г"
        "\nx : э\n4 : ж\n? : .")
f.close()
