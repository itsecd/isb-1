#получение частот букв русского алфавита из файла для удобства работы
litter_chastota = {}
with open('chastota.txt', mode='r', encoding='utf-8') as file:
    for i in range(33):
        r = file.readline()
        r=r.split('\n')
        r=r[0].split('=')
        litter_chastota[r[0]] = [r[1]]
    file.close()

#получаем текст из файла
text = ''
with open('2-text.txt', mode='r', encoding='utf-8') as file:
    text = file.read()
    file.close()

#находим все разичные символы в тексте и определяем их частоту, последовательно отсортировав
text_chastota = {}
l = len(text)
text_litters = []
for i in text:
    if text_litters.count(i) == 0:
        text_litters.append(i)

for i in text_litters:
    text_chastota[i] = text.count(i) / l

text_chastota = sorted(text_chastota.items(), key = lambda item: item[1])
text_chastota = dict(text_chastota[::-1])

#получение и вывод частот для удобства работы
item_litter_chastota = tuple(litter_chastota.items())
item_text_chastota = tuple(text_chastota.items())
for i in range (32):
    print(i, ' ', item_litter_chastota[i], '\t\t', item_text_chastota[i])
    
print('--'*40)

#расшифровка
new_text = text
print('1 - Й = Т')
new_text = new_text.replace(item_text_chastota[7][0], item_litter_chastota[6][0])
print('2 - Ф = Й')
new_text = new_text.replace(item_text_chastota[24][0], item_litter_chastota[25][0])
print('3 - Ш = Ф')
new_text = new_text.replace(item_text_chastota[25][0], item_litter_chastota[24][0])
print('4 - Ы = Ш')
new_text = new_text.replace(item_text_chastota[31][0], item_litter_chastota[29][0])
print('5 - \' \' = Ы')
new_text = new_text.replace(item_text_chastota[17][0], item_litter_chastota[17][0])
print('6 - M = \' \'')
new_text = new_text.replace(item_text_chastota[0][0], item_litter_chastota[0][0])
print('7 - 2 = М')
new_text = new_text.replace(item_text_chastota[15][0], item_litter_chastota[10][0])
print('8 - О = В')
new_text = new_text.replace(item_text_chastota[8][0], item_litter_chastota[9][0])
print('9 - Е = О')
new_text = new_text.replace(item_text_chastota[1][0], item_litter_chastota[1][0])
print('10 - > = Е')
new_text = new_text.replace(item_text_chastota[4][0], item_litter_chastota[3][0])
print('11 - Д = Н')
new_text = new_text.replace(item_text_chastota[5][0], item_litter_chastota[5][0])
print('12 - Р = Д')
new_text = new_text.replace(item_text_chastota[10][0], item_litter_chastota[12][0])
print('13 - И = С')
new_text = new_text.replace(item_text_chastota[6][0], item_litter_chastota[7][0])
print('14 - У = И')
new_text = new_text.replace(item_text_chastota[2][0], item_litter_chastota[2][0])
print('15 - Ч = У')
new_text = new_text.replace(item_text_chastota[19][0], item_litter_chastota[19][0])
print('16 - К = Ю')
new_text = new_text.replace(item_text_chastota[22][0], item_litter_chastota[26][0])
print('17 - Х = К')
new_text = new_text.replace(item_text_chastota[13][0], item_litter_chastota[14][0])
print('18 - Щ = Х')
new_text = new_text.replace(item_text_chastota[20][0], item_litter_chastota[23][0])
print('19 - Ь = Щ')
new_text = new_text.replace(item_text_chastota[28][0], item_litter_chastota[30][0])
print('20 - 5 = Б')
new_text = new_text.replace(item_text_chastota[29][0], item_litter_chastota[27][0])
print('21 - Л = Я')
new_text = new_text.replace(item_text_chastota[14][0], item_litter_chastota[13][0])
print('22 - 1 = Л')
new_text = new_text.replace(item_text_chastota[11][0], item_litter_chastota[11][0])
print('23 - Ъ = Ц')
new_text = new_text.replace(item_text_chastota[23][0], item_litter_chastota[28][0])
print('24 - А = Ь')
new_text = new_text.replace(item_text_chastota[18][0], item_litter_chastota[18][0])
print('25 - 4 = A')
new_text = new_text.replace(item_text_chastota[3][0], item_litter_chastota[4][0])
print('26 - П = Г')
new_text = new_text.replace(item_text_chastota[26][0], item_litter_chastota[22][0])
print('27 - r = П')
new_text = new_text.replace(item_text_chastota[12][0], item_litter_chastota[15][0])
print('28 - t = Р')
new_text = new_text.replace(item_text_chastota[9][0], item_litter_chastota[8][0])
print('29 - 7 = Ж')
new_text = new_text.replace(item_text_chastota[27][0], item_litter_chastota[21][0])
print('30 - < = Ч')
new_text = new_text.replace(item_text_chastota[21][0], item_litter_chastota[20][0])
print('31 - 8 = З')
new_text = new_text.replace(item_text_chastota[16][0], item_litter_chastota[16][0])

print(new_text)
