def main():
    print("start")
    alfavit="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    sdvig=int(input('Ключ шифрования: '))%33
    text=input("Шифруемый текст: ").upper()
    after_text=''
    for i in text:
        mesto = alfavit.find(i)
        new_mesto = mesto + sdvig
        if i in alfavit:
            after_text += alfavit[new_mesto]
        else:
            after_text += i
    print()
    print(after_text)
    print("end")
    
if __name__ == "__main__":
    main()