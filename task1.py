from random import shuffle


def generate_notepad() -> dict:
    alphabet = "йцукенгшщзхъфывапролджэячсмитьбю" + "йцукенгшщзхъфывапролджэячсмитьбю".upper()
    alphabet_cpy = shuffle_string(alphabet)
    return {c1: c2 for c1,c2 in zip(alphabet, alphabet_cpy) }


def shuffle_string(txt: str) -> str:
    txt_lst = list(txt)
    shuffle(txt_lst)
    return ''.join(txt_lst)
