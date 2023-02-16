from random import shuffle
def generate_notepad() -> dict:
    alphabet = "йцукенгшщзхъфывапролджэячсмитьбю" + "йцукенгшщзхъфывапролджэячсмитьбю".upper()
    alphabet_cpy = shuffle_string(alphabet)
