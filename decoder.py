from File import File
import Shifter
from collections import Counter

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
    "Ч" : 0.011679,
    " " : 0.128675
}

def count_letters(text: str) -> dict:
    
    exp_dict = dict()
    
    total_letters = 0
    
    buffer = list() #remember counted letters
    
    for lett in text:
        #if lett in Shifter.alphabet_upper: total_letters+=1 # total letters
        if lett != '\n' :total_letters+=1
    
    for letter in text:
        
        if (not (letter in buffer)) and letter!='\n':    
            count_for_one_letter = text.count(letter) # for one letter
            exp_dict[letter] = (count_for_one_letter / total_letters)
        else:
            pass
        
    return exp_dict
            
def decoder(exp_dict: dict):
    
    shift_dict = dict()
    
    for src in exp_dict:
        
        let_buf = str() #remmeber sutable letter
        delta = 1 # possib_from_text - possib_from_RU
        
        for alph in possibility_dict:
            
            if abs(possibility_dict[alph] - exp_dict[src]) < delta: 
                delta = abs(possibility_dict[alph] - exp_dict[src])
                let_buf = alph
                
        print(f"[{let_buf} : {possibility_dict[let_buf]}] <- [{src} : {exp_dict[src]}]")
        shift_dict[src] = let_buf
        
    return shift_dict

# def find_key(shift_dict: dict):
#     possible_keys = list()
    
#     for letter in shift_dict:
#         possible_keys.append(Shifter.Shifter.get_shift(letter, shift_dict[letter]))
    
#     c = Counter(possible_keys)
    
#     return c.most_common(1)[0][0]
    
def changer(text, shift_dict):
    output_text = str()
    
    for letter in text:
    
        if letter in shift_dict: output_text += shift_dict[letter]
        
    return output_text
    
if __name__=="__main__":
    
    filename = "./decoder_data/cod7"
    
    src_text = str()
   
    try:
        src_file = File(filename , "r")
        src_text = src_file.read()
    except:
        print("Input file error (isn't it's name *.txt?)")
        exit()
        
    exp_dict = count_letters(src_text) # { a_letter_from_text : probability }
    
    shift_dict = decoder(exp_dict) # { a_letter_from_text  : approxed_letter }
    
    out_text = changer(src_text, shift_dict)
    
    print(out_text)
                
    try:
        out_file = File("./decoder_data/output_text", "w")
        out_file.write(out_text)
    except:
        print("Output file error (does it already exist?)")
        exit()
        
    
    
        
    