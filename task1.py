from random import shuffle


def generate_notepad() -> dict:
    alphabet = "йцукенгшщзхъфывапролджэячсмитьбю" + "йцукенгшщзхъфывапролджэячсмитьбю".upper()
    alphabet_cpy = shuffle_string(alphabet)


def shuffle_string(txt: str) -> str:
    txt_lst = list(txt)
    shuffle(txt_lst)
    return ''.join(txt_lst)
