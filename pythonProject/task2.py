from main import read_file, write_file
LETTERS = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯWRT124578"


def count_frequencies(text: str):
    text = text.upper()
    lenght = len(text)
    fre = {}
    for letter in LETTERS:
        fre[letter] = str(float(text.count(letter) / lenght))
    fre = sorted(fre.items(), key=lambda x: x[1], reverse=True)
    with open("task2_frequencies.txt", "w", encoding='utf-8') as f:
        for ele in fre:
            f.write(str(ele) + str('\n'))


def decode(text: str, filename: str):
    text = text.replace(' ', 'е')
    text = text.replace('Х', ' ')
    text = text.replace('е', 'и')
    text = text.replace('1', 'л')
    text = text.replace('2', 'м')
    text = text.replace('Д', 'н')
    text = text.replace('8', 'э')
    text = text.replace('Б', 'к')
    text = text.replace('Ч', 'а')
    text = text.replace('Е', 'о')
    text = text.replace('Ъ', 'г')
    text = text.replace('T', 'р')
    text = text.replace('И', 'с')
    text = text.replace('R', 'п')
    text = text.replace('Й', 'ф')
    text = text.replace('>', 'ы')
    text = text.replace('Ы', 'е')
    text = text.replace('П', 'щ')
    text = text.replace('W', 'д')
    text = text.replace('К', 'у')
    text = text.replace('5', 'ч')
    text = text.replace('Щ', 'в')
    text = text.replace('Ф', 'я')
    text = text.replace('Я', 'з')
    text = text.replace('Ь', 'ж')
    text = text.replace('ф', 'т')
    text = text.replace('7', 'ь')
    text = text.replace('Л', 'ф')
    text = text.replace('О', 'ш')
    text = text.replace('4', 'ц')
    text = text.replace('А', 'й')
    text = text.replace('М', 'х')
    text = text.replace('У', 'ю')
    with open(f'{filename}.txt', "w", encoding='utf-8') as f:
        f.write(text)
    count_frequencies(text)
    print(text)


if __name__ == "__main__":
    text = read_file("cod7").upper()

    decode(text, 'task2-decode')


