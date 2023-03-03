from collections import Counter
TEXT = "Х4МЕОb1cХЛЫХ>7МcОХАМЕtЬОЕratКrМЕ1rХ>МД4РУ><Х ЙМ4Уb1Д>rФ1aМЕП4r>ЛМ5ОРМ21rОДАМЕМ4c42r>aХ Ф>М>МЕr4r><ОЕ8>Ф>МФ1cОУЛФ>М2ДОcЕr4aУОХ>ЛМc4ХХ ЙМ>ЙМaЕОМФ1ПХ1МД4Р5>rАМХ4МХО2ОДОЕО84КЬ>ОЕЛМ8У4 ЕЕ М>У>МЕОФО7Еra4М21МЕ21Е15tМ81c>Д1a4Х>ЛМc4ХХ ЙМ84Пc1ОМЕОФО7Еra1М2Д>Рa4Х1МЕП4rАМrО8ЕrМ12ДОcОУОХ Х17МЕrДt8rtД МЕМ12ДОcОУОХХ17МЕrО2ОХАКМБИИО8r>aХ1Еr>М>М5 ЕrД1cО7Еra>ЛМaМР4a>Е>Ф1Еr>М1rМr1b1М<r1Мa4ПХООМaМ2Д> У1ПОХ>>МЕ81Д1ЕrАМ>У>М81БИИ>Ч>ОХrМЕП4r>Л"
ALF = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "

def count_symbols()->dict:
    simvols = Counter(TEXT)
    for item in simvols:
        simvols[item] = simvols[item]/len(TEXT)
        #print(item,simvols[item])
    return simvols

def chenging(new_text: str)->str:
    print("При введении некорректного символа расшифровка прекратится")
    flag = 0
    while flag == 0:
        simvol = str(input(new_text+"\n"+"Какой символ поменять? - "))
        if simvol not in new_text:
            flag = 1
        new_simvol = str(input(new_text+"\n"+"На какой символ поменять? - "))
        if new_simvol not in ALF:
            flag = 1
        if flag!=1:
            new_text = new_text.replace(simvol, new_simvol)
    return new_text

if __name__ == "__main__":
    text = TEXT.replace(" ", ".")
    print(count_symbols())
    user = int(input("Введите: 0 - расшифровывать текст; 1 - записать текст\n - "))
    while not user == 0 and not user == 1:
        user = int(input("Введите корректно: 0 - расшифровывать текст; 1 - записать текст\n - "))
    while user == 0:
        text = chenging(text)
        user = int(input("Введите: 0 - расшифровывать текст; 1 - записать текст\n - "))
        while not user == 0 and not user == 1:
            user = int(input("Введите корректно: 0 - расшифровывать текст; 1 - записать текст\n - "))
    print(text)