RUSSIAN_ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
BY_FREQUENCY_ALPHABET = ' ОИЕАНТСРВМЛДЯКПЗЫЬУЧЖГХФЙЮБЦШЩЭЪ'

def read_file(filename: str) -> str:
    """
        function to read data from a file
    """
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        return file.read().upper()

def write_in_file(filename: str, data: str) -> None:
    """
        function to write data to file
    """
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        file.write(data)

def text_encoding_сaesars_cipher() -> str:
    """
        function of text encoding by simple permutation codes using a special Caesar cipher.
        :encryption_step: - encryption step (how much we shift the position of the letter in the alphabet).
        :read_text: - the text read from the text.txt file.
        :result_ciphers: - the result of encryption of the original text.
    """
    encryption_step = 3
    read_text = read_file('text.txt')
    result_ciphers = ""
    for i in read_text:
        new_letter_id = RUSSIAN_ALPHABET.find(i) + encryption_step
        if i in RUSSIAN_ALPHABET:
            result_ciphers += RUSSIAN_ALPHABET[new_letter_id]
        else:
            result_ciphers += i
    return result_ciphers

def repetition_rate_generation(your_text: str):
    dictionary = dict()
    for i in your_text:
        dictionary[i] = your_text.count(i)
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    # print(dictionary)
    return dictionary

