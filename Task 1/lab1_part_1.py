import os
#import pandas as pd



def encription ( key: int, text: str ):

    symbols = set( text )
    frequency = dict()
    for sym in symbols:
        frequency[sym] = text.count(sym)
    frequency = sorted(frequency.items(), key=lambda x: x[1])
    
    letters = []
    for i in frequency:
        letters += i[0]
    letters = letters[::-1]
    print(letters)

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    newText = ''
    text = text.replace( '.', '')
    text = text.replace( ',', '')
    text = text.replace( '!', '')
    text = text.replace( '?', '')
    text = text.replace( '-', '')
    text = text.replace( ':', '')
    text = text.lower()
    for sym in text:
        newText += alphabet[( alphabet.index(sym) + key )%len( alphabet )]
    return newText

def decript ( text: str ):
    symbols = set( text )
    frequency = dict()
    for sym in symbols:
        frequency[sym] = text.count(sym)/len(text)
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    print(frequency)
    letters = []
    for i in frequency:
        letters += i[0]
    print(letters)

if __name__ == '__main__':

    fileName = 'Task 1/text.txt'
    key = 1
    text = ''
    with open( fileName, mode='r', encoding='utf-8' ) as file:
        text = file.read()
        print(len(text))
        text = encription( key, text )
        
        with open( 'Task 1/textEncripted.txt', mode='w', encoding='utf-8'  ) as file1:
            file1.write( text )

    decript(text)
    