def frec(text: str) -> dict:
    dic = dict()
    lst = list(set(text))
    l = len(text)
    for i in lst:
        dic[i] = (text.count(i))/l
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic)
    text = text.replace(' ', 'а')
    text = text.replace('Х', ' ')
    text = text.replace('Е', 'о')
    text = text.replace('Д', 'н')
    text = text.replace('а', 'и')
    text = text.replace('Ч', 'а')
    text = text.replace('Ы', 'е')
    text = text.replace('Б', 'к')
    text = text.replace('1', 'л')
    text = text.replace('П', 'щ')
    text = text.replace('Ъ', 'г')
    text = text.replace('Щ', 'в')
    text = text.replace('t', 'р')
    text = text.replace('Ф', 'я')
    text = text.replace('Й', 'т')
    text = text.replace('2', 'м')
    text = text.replace('>', 'ы')
    text = text.replace('r', 'п')
    text = text.replace('Я', 'з')
    text = text.replace('У', 'ю')
    text = text.replace('w', 'д')
    text = text.replace('5', 'ч')
    text = text.replace('7', 'ь')
    text = text.replace('К', 'у')
    text = text.replace('И', 'с')
    text = text.replace('Ь', 'ж')
    text = text.replace('Л', 'ф')
    text = text.replace('4', 'ц')
    text = text.replace('8', 'э')
    text = text.replace('О', 'ш')
    text = text.replace('А', 'й')
    text = text.replace('М', 'х')

    print(text)


if __name__ == "__main__":
    fileName = 'task_text.txt'

    with open( fileName, mode='r', encoding="utf-8") as f:
        text = f.read()

    text = frec(text)

