
def saveFile(str: str, fileName: str) -> None:
    with open(f'{fileName}.txt', 'w', encoding="utf-8") as f:
        if (type(str) == 'dict'):
            print(str, file=f)
        f.write(str)
        # print(str, file=f)


def createKey(n: int) -> str:
    alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    n = -n
    alph = list(alph)
    if n < 0:
        n = abs(n)
        for i in range(n):
            alph.append(alph.pop(0))
    else:
        for i in range(n):
            alph.insert(0, alph.pop())
    return ''.join(alph)


def encrypt(str: str, n: int):
    alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alph = alph.lower()
    ln = len(alph)
    res = []
    noAlph = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in str:
        if not l in noAlph:
            res.append(alph[(alph.find(l)+n) % ln])
        else:
            res.append(l)
    return ''.join(res)


def makeDic():
    tmpLetter = '0'
    tmpValue = 0
    res = {}
    while (True):
        tmpLetter = (input('Char: '))
        tmpLetter = tmpLetter.upper()
        tmpValue = float(input('Value: '))
        if (tmpValue == -1):
            break
        res[tmpLetter] = tmpValue
    res = dict(sorted(res.items(), key=lambda item: item[1]))
    return res


def createDic(str: str):
    tmp = set(list(str))
    length = len(str)
    res = {}
    for i in tmp:
        count = 0
        for j in str:
            if (i == j):
                count += 1
        res[i] = count/length
    res = dict(sorted(res.items(), key=lambda item: item[1]))
    res = dict(reversed(list(res.items())))
    return res


def replaceLetter(text: str, letterOld: str, letterNew: str):
    text.replace(letterOld, letterNew)


if __name__ == '__main__':
    # text = "Потребность шифровать и передавать шифрованные сообщения возникла очень давно. Так, еще в древние греки применяли специальное шифрующее устройство. По описанию Плутарха, оно состояло из двух палок одинаковой длины и толщины. Одну оставляли себе, а другую отдавали отъезжающему. Эти палки называли скиталами. Когда правителям нужно было сообщить какую-нибудь важную тайну, они вырезали длинную и узкую, вроде ремня, полосу папируса, наматывали ее на свою скиталу, не оставляя на ней никакого промежутка, так чтобы вся поверхность палки была охвачена этой полосой. Затем, оставляя папирус на скитале в том виде, как он есть, писали на нем все, что нужно, а написав, снимали полосу и без палки отправляли адресату. Так как буквы на ней разбросаны в беспорядке, то прочитать написанное он мог, только взяв свою скиталу и намотав на нее без пропусков эту полосу"
    # text = text.lower()
    # saveFile(text, "original")
    # saveFile(createKey(1), "key")
    # saveFile(encrypt(text, 1), "encrypted")

    text2 = '''КwЧ5Д>ЫХЧ1ЪЕt Й2>ХИЬЧЙ ФХ 1 ХБЧБХЫПЫХЪЕЩЕtФЙХБЕ2rtЫИИ ХrЕЯЩЕ1ФУЙХДЫХЙЕ17БЕХ8ЛЛЫБЙ
ЩДЕХМtЧД Й7ХБЕДЛ wЫД4 Ч17Д>ЫХwЧДД>ЫХДЕХ ХДЧrt
2ЫtХЯДЧ5 ЙЫ17ДЕХК2ЫД7О
Й7ХtЧЯ2ЫtХrtЕЪtЧ22>ХБЕЙЕtКУХЯЧХЕw ДХrt
Ы2Х2ЕЬДЕХЯЧЪtКЯ Й7ХЩХrЧ2ФЙ7Х Х ИrЕ1Д
Й7ХИКПЫИЙЩКЫЙХДЫХ2ЫД7ОЫХwУЬ Д>ХtЧЯ1
5Д>МХКrЧБЕЩП БЕЩХ ИrЕ1Д 2>МХЛЧА1ЕЩХДЫБЕЙЕt>ЫХ
ЯХД МХИЕwЫtЬЧЙХtЫЧ1 ЯЧ4 ХЧ1ЪЕt Й2ЕЩХО ЛtЕЩЧД
ФХИХ4Ы17УХКИ1ЕЬД Й7ХЬ ЯД7ХrЕЙЫД4
Ч17Д>2ХМЧБЫtЧ2ХДЕХД ХЩХЕwДЕАХ ЯХД МХЧ1ЪЕt Й2ХО
ЛtЕЩЧД ФХД БЧБХДЫХИЩФЯЧДХИХЧ1ЪЕt Й2Е2ХИЬЧЙ ФХЕД
ХtЫЧ1 ЯЕЩЧД>ХБЧБХЕЙwЫ17Д>ЫХЧ1ЪЕt Й2>Х Х
ИrЕ17ЯКУЙИФХtЧЯwЫ17Д'''

