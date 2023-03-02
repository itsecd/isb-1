from File import File
from Shifter import Shifter

upper_alph = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

possibility_dict = {
    "О" : 0.096456,
    "И" : 0.075312,
    "Е" : 0.072292,
    "А" : 0.064841,
    "Н" : 0.061820,
    "Т" : 0.061619,
    "С" : 0.051953,
    "Р" : 0.040677,
    "В" : 0.039267,
    "М" : 0.029803,
    "Л" : 0.029400,
    "Д" : 0.026983,
    "Я" : 0.026379,
    "К" : 0.025977,
    "П" : 0.024768,
    "З" : 0.015908,
    "Ы" : 0.015707,
    "Ь" : 0.015103,
    "У" : 0.013290,
    "Ч" : 0.011679
}

def count_letters(text: str) -> dict:
    exp_dict = dict()
    
    total_letters = 0
    
    buffer = list()
    
    text = text.upper()
    
    for lett in text:
        if lett in upper_alph: total_letters+=1 # total letters
    
    for letter in text:
        if letter in upper_alph and (not (letter in buffer)):
            
            number_of_letters = text.count(letter) # for one letter
            exp_dict[letter] = (number_of_letters / total_letters)
        else:
            pass
        
    return exp_dict
            
def decoder(exp_dict: dict):
    
    shift_dict = dict()
    
    for letter in exp_dict:
        
        let_buf = str()
        delta = 1
        
        for let in possibility_dict:
            if abs(exp_dict[letter] - possibility_dict[let]) < delta: 
                delta = abs(exp_dict[letter] - possibility_dict[let])
                let_buf = let
        
        shift_dict[letter] = let_buf
        
    return shift_dict

# def find_key(shift_dict: dict):
#     values = list()
    
#     for letter in shift_dict:
#         difference = Shifter.get_shift(letter, shift_dict[letter])
#         print (f"{letter} - {shift_dict[letter]} = {difference}")
#         values.append(difference)
    
#     return round(sum(values) / len(values))
    
def changer(text: str, shift_dict: dict)-> str:
    output_text = str()
    
    for letter in text:
        if letter.upper() not in upper_alph: output_text += letter
    
        elif letter.isupper():
            output_text += shift_dict[letter]
            
        elif letter.islower():
            output_text += shift_dict[letter.upper()].lower()
    
    return output_text
    
if __name__=="__main__":
    
    src_text = str()
   
    try:
        src_file = File("./coder_data/output_text.txt", "r")
        src_text = src_file.read()
    except:
        print("Input file error (isn't it's name *.txt?)")
        exit()
        
    exp_dict = count_letters(src_text)
    
    shift_dict = decoder(exp_dict)
    
    out_text = changer(src_text, shift_dict)
    
    try:
        out_file = File("./decoder_data/output_text", "w")
        out_file.write(out_text)
    except:
        print("Output file error (does it already exist?)")
        exit()
    
    # key = find_key(shift_dict)
    
    # shifter = Shifter(key)
    
    # for letter in src_text:
    #     print(shifter.shift_decode(letter),end='')
    
    
        
    