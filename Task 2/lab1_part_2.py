def Decript ( text: str ):
    letters = set( text )
    freq = dict()
    for letter in letters:
        freq[letter] = text.count( letter )
    freq = sorted( freq.items(), key=lambda x: x[1] )
    print( freq )
    text = text.replace(' ', 'а')
    text = text.replace('Я', ' ')
    text = text.replace('Д', 'е')
    text = text.replace('М', 'н')
    text = text.replace('Й', 'к')
    text = text.replace('t', 'и')
    text = text.replace('У', 'х')
    text = text.replace('2', 'д')
    text = text.replace('4', 'о')    
    text = text.replace('Л', 'м')    
    text = text.replace('1', 'г')   
    text = text.replace('Ч', 'щ')
    text = text.replace('Е', 'ж')
    text = text.replace('Х', 'ч')     
    text = text.replace('r', 'з')
    text = text.replace('Ъ', 'ь')
    text = text.replace('Р', 'т')
    text = text.replace('П', 'с')
    text = text.replace('Т', 'ф')
    text = text.replace('w', 'э')
    text = text.replace('Б', 'в')
    text = text.replace('Ц', 'ш')
    text = text.replace('О', 'р')
    text = text.replace('К', 'л')
    text = text.replace('5', 'п')
    text = text.replace('Щ', 'ы')
    text = text.replace('Ь', 'я')
    text = text.replace('Ы', 'ю')
    text = text.replace('И', 'й')
    text = text.replace('А', 'б')
    text = text.replace('>', 'у')
    text = text.replace('Ф', 'ц')
    text = text.replace('?', '.')
    print( text )
    return text






if __name__ == '__main__':
    fileName = 'Task 2/textForEncoding.txt'
    text = ''
    with open( fileName, mode='r', encoding='utf-8' ) as file:
        text = file.read()
        print( text )
        text = Decript( text )
    with open( 'Task 2/Decripted_text.txt', mode='w', encoding='utf-8' ) as file:
        file.write( text )
