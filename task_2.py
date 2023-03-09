from task_1 import readFile, saveFile

def save_frequency (text: str, fileName: str) -> None:
    set_text = set(text)
    frequency = {}
    for i in set_text:
        counter = 0
        for j in text:
            if j == i:
                counter += 1
        frequency[i] = counter / len(text)
    sorted_fre = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    with open(f'{fileName}.txt', "w", encoding='utf-8') as file:
        for item in sorted_fre:
            file.write(f'{item[0]} = {item[1]}\n')

def decryption(text:str) -> str:
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
    return new_text

if __name__ == "__main__":
    text_code = readFile("cod6")
    save_frequency(text_code, "frequency_2")
    new_texts = decryption(text_code)
    saveFile(new_texts, 'decryption_text_2')



