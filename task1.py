from random import shuffle


def generate_notepad() -> dict:
    alphabet = "йцукенгшщзхъфывапролджэячсмитьбю" + "йцукенгшщзхъфывапролджэячсмитьбю".upper()
    alphabet_cpy = shuffle_string(alphabet)
    return {c1: c2 for c1,c2 in zip(alphabet, alphabet_cpy) }


def shuffle_string(txt: str) -> str:
    txt_lst = list(txt)
    shuffle(txt_lst)
    return ''.join(txt_lst)


def encrypt(text: str, notepad: dict = None) -> str:
    if notepad is None:
        notepad = generate_notepad()
        print('Notepad is: ', notepad, sep='\n')

    return ''.join([notepad.get(c, c) for c in text])


if __name__ == "__main__":
    with open("task1_text") as file:
        s = file.read()
    #print(encrypt(s))
    #print(s)
    file_write = open("task1_encrypt.txt", "w")
    file_write.write(encrypt(s))
    file_write.close()


