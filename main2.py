def read_file(file_name):
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
        return file.read()


def save_file_frequency(file_name, text, counts):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
        file.write('\n' + 'Частота появления:' + '\n')
        for letter, count in text.items():
            file.write(f"{letter} : {count/counts}" "\n")

def save_file(file_name, text):
    with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
        file.write('\n' + 'Расшифрованный текст:' + '\n'+ text)
        

def letter_frequency(text):
    letter_count = {}
    counts = len(text)
    for letter in text:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1
    return letter_count, counts

def decryption(text):
    new_text=text
    new_text=new_text.replace(' ','р')
    new_text=new_text.replace('Х',' ')
    new_text=new_text.replace('Ь','о')
    new_text=new_text.replace('Б','т')
    new_text=new_text.replace('Ч','и')
    new_text=new_text.replace('t','е')
    new_text=new_text.replace('1','a')
    new_text=new_text.replace('А','с')
    new_text=new_text.replace('Ы','н')
    new_text=new_text.replace('<','м')
    new_text=new_text.replace('Д','в')
    new_text=new_text.replace('Ъ','л')
    new_text=new_text.replace('Щ','к')
    new_text=new_text.replace('Я','п')
    new_text=new_text.replace('Ф','я')
    new_text=new_text.replace('>','ы')
    new_text=new_text.replace('И','ж')
    new_text=new_text.replace('5','ч')
    new_text=new_text.replace('Е','г')
    new_text=new_text.replace('2','б')
    new_text=new_text.replace('r','д')
    new_text=new_text.replace('7','ь')
    new_text=new_text.replace('Л','ф')
    new_text=new_text.replace('К','у')
    new_text=new_text.replace('О','ш')
    new_text=new_text.replace('М','х')
    new_text=new_text.replace('Й','з')
    new_text=new_text.replace('Ш','й')
    new_text=new_text.replace('8','э')
    new_text=new_text.replace('4','ш')
    new_text=new_text.replace('У','ю')
    
    print(new_text)
    return new_text


def main():
    text = read_file("text2")
    frequency, counts = letter_frequency(text)
    frequency = dict(sorted(frequency.items(), key = lambda item: item[1] , reverse=True))
    save_file_frequency("frequency", frequency ,counts)
    new_texts=decryption(text)
    save_file('decryptiontext',new_texts)


if __name__ == "__main__":
    main()
