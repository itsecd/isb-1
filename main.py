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

def get_dictionary(text: str) -> dict:
    """
        function to get a sorted in descending order dictionary
    """
    dictionary = dict()
    for i in text:
        dictionary[i] = text.count(i)
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return dictionary

def repetition_rate_generation(initial_text: str, encrypted_text: str):
    """
        dictionary generation function for the initial text and the encrypted
        text (using frequency analysis for decryption)
    """
    dictionary_for_initial_text = get_dictionary(initial_text)
    dictionary_for_encrypted_text = get_dictionary(encrypted_text)
    return dictionary_for_initial_text, dictionary_for_encrypted_text

def text_transcription(text: str, dict1: dict, dict2: dict):
    """
        text interpretation function
    """
    result = ""
    list_for1_keys = list(dict1.keys())
    list_for2_keys = list(dict2.keys())
    for item in text:
        id = list_for2_keys.index(item)
        result += list_for1_keys[id]
    return result

initial_txt = read_file('text.txt')
res = text_encoding_сaesars_cipher()
dictionary_for_initial_text, dictionary_for_encrypted_text=repetition_rate_generation(initial_txt,res)
print(dictionary_for_initial_text)
print(dictionary_for_encrypted_text)
print(text_transcription(res, dictionary_for_initial_text, dictionary_for_encrypted_text))