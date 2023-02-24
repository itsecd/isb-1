#создание словаря-алфавита(dict_alphabet) для кодировки и талицы Виженера(alphabet)
nonsplit_alphabet = 'А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я'
split_alphabet = nonsplit_alphabet.split(',')
dict_alphabet = {}

for i in range(32):
    dict_alphabet[split_alphabet[i]] = i

alphabet = {}
for i in range(32):
    alphabet[i] = split_alphabet[i:i+32:1] + split_alphabet[0:i]
    
#получение исходного текста(text1) и кодового слова(codeword1) из файлов
text1 = ''
with open('text1.txt', mode='r', encoding='utf-8') as file:
    text1 = file.readline()
    file.close()
print('Исходный текст: \n', text1)

codeword1 = ''
with open('codeword1.txt', mode='r', encoding='utf-8') as file:
    codeword1 = file.readline()
print('\nКодовое слово: \n', codeword1)

#преобразование текста и создание строчки из повторяющегося кодового слова
text1 = text1.replace(' ', '')
n = int(len(text1) / len(codeword1) + 1)
wordstr = codeword1 * n
wordstr = wordstr[:len(text1)]

#индексиование букв в тексте и строке кодового слова
text_numbers = []
word_numbers = []
for i, j in zip(text1, wordstr):
    text_numbers.append(dict_alphabet[i])
    word_numbers.append(dict_alphabet[j])

#кодировка текста и запись в файл
new_text = ''
for i, j in zip(text_numbers, word_numbers):
    new_text += alphabet[i][j]
print('\nЗашифрованный текст:\n', new_text)

with open('shifr-text1.txt', mode='a', encoding='utf-8') as file:
    file.write(new_text)
    file.close()