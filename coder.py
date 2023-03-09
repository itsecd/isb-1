import random

ALPHABET = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ "


def coder(input_str: str) -> str:
    new_key = ""
    result_str = ""
    origin_key = ["1", "<", "A", "D", "2", ">", "3", "B", "C", "%", "R", "T", "Y", "O", "P",
                  "G", "4", "5", "F", "C", "X", "Z", "6", "J", "M", "N", "7", "$", "#", " ", "Q", "W"]
    random.shuffle(origin_key)
    for i in range(len(origin_key)):
        new_key += origin_key[i]
    for elem in input_str:
        index = ALPHABET.find(elem)
        result_str += new_key[index]
    print("KEY -> ", new_key)
    return result_str


if __name__ == "__main__":
    input_text = input("Input text -> ")
    print("RESULT -> ", coder(input_text))
