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


def get_encryption_keys(dict1: dict, dict2: dict) -> dict:
    dictionary = dict()
    list_for1_keys = list(dict1.keys())
    list_for2_keys = list(dict2.keys())
    for i in range(len(list_for1_keys)):
        dictionary[list_for1_keys[i]] = list_for2_keys[i]
    return dictionary

if __name__ == "__main__":
# task 1
    initial_txt = read_file('text.txt')
    res = text_encoding_сaesars_cipher()
    write_in_file('encryption.txt', res)
    dictionary_for_initial_text, dictionary_for_encrypted_text = repetition_rate_generation(initial_txt, res)

    # derived frequency dictionaries
    print(dictionary_for_initial_text)
    print(dictionary_for_encrypted_text)

    # text transcription
    print(text_transcription(res, dictionary_for_initial_text, dictionary_for_encrypted_text))

    # encryption key dictionary
    keys_dict = get_encryption_keys(dictionary_for_initial_text, dictionary_for_encrypted_text)
    write_in_file('key.txt', "' ' : ' ',\n'О' : 'С',\n'Е' : 'З',\n'И' : 'Л',\n'Н' : 'Р',\n'А' : 'Г',\n'Т' : 'Х',\n'Р' : 'У',\n'С' : 'Ф',\n'П' : 'Т',\n'Д' : 'Ж',\n'Ы' : 'Ю',\n'Л' : 'О',\n'В' : 'Е',\n'Я' : 'В',\n'М' : 'П',\n'К' : 'Н',\n'Г' : 'Ё',\n'Х' : 'Ш',\n'З' : 'К',\n',' : ',',\n'Б' : 'Д',\n'Ч' : 'Ъ',\n'Ь' : 'Я',\n'Й' : 'М',\n'У' : 'Ц',\n'Ю' : 'Б',\n'.' : '.',\n'Ф' : 'Ч',\n'Ц' : 'Щ',\n'Ш' : 'Ы',\n'Ж' : 'Й',\n'Э' : 'А',\n':' : ':',\n'-' : '-',\n'Щ' : 'Ь'")
# task 2
    text_ = read_file('cod4.txt')
    print(text_)
    dictionary_for_encrypted_text = get_dictionary(text_)
    dictionary_for_initial_text = get_dictionary(BY_FREQUENCY_ALPHABET)
    print(dictionary_for_encrypted_text)
    print(dictionary_for_initial_text)

    dict_keys = {}
    text_ = text_.replace('Ы', 'Ш')
    dict_keys['Ы'] = 'Ш'
    text_ = text_.replace(' ', 'Ы')
    dict_keys[' '] = 'Ы'
    text_ = text_.replace('М', ' ')
    dict_keys['М'] = ' '
    text_ = text_.replace('Х', 'Н')
    dict_keys['Х'] = 'Н'
    text_ = text_.replace('Ф', 'М')
    dict_keys['Ф'] = 'М'
    text_ = text_.replace('И', 'Ф')
    dict_keys['И'] = 'Ф'
    text_ = text_.replace('>', 'И')
    dict_keys['>'] = 'И'
    text_ = text_.replace('Р', 'З')
    dict_keys['Р'] = 'З'
    text_ = text_.replace('Д', 'Р')
    dict_keys['Д'] = 'Р'
    text_ = text_.replace('C', 'Д')
    dict_keys['C'] = 'Д'
    text_ = text_.replace('Е', 'С')
    dict_keys['Е'] = 'С'
    text_ = text_.replace('Е', 'Ы')
    dict_keys['Е'] = 'Ы'
    text_ = text_.replace('О', 'Е')
    dict_keys['О'] = 'Е'
    text_ = text_.replace('Л', 'Я')
    dict_keys['Л'] = 'Я'
    text_ = text_.replace('У', 'Л')
    dict_keys['У'] = 'Л'
    text_ = text_.replace('Т', 'У')
    dict_keys['Т'] = 'У'
    text_ = text_.replace('П', 'Ж')
    dict_keys['П'] = 'Ж'
    text_ = text_.replace('2', 'П')
    dict_keys['2'] = 'П'
    text_ = text_.replace('О', 'Й')
    dict_keys['2'] = 'П'
    text_ = text_.replace('1', 'О')
    dict_keys['1'] = 'О'
    text_ = text_.replace('Ь', 'Ц')
    dict_keys['Ь'] = 'Ц'
    text_ = text_.replace('А', 'Ь')
    dict_keys['А'] = 'Ь'
    text_ = text_.replace('A', 'В')
    dict_keys['A'] = 'В'
    text_ = text_.replace('4', 'А')
    dict_keys['4'] = 'А'
    text_ = text_.replace('B', 'Г')
    dict_keys['B'] = 'Г'
    text_ = text_.replace('R', 'Т')
    dict_keys['R'] = 'Т'
    text_ = text_.replace('Ц', 'Щ')
    dict_keys['Ц'] = 'Щ'
    text_ = text_.replace('Ч', 'Ц')
    dict_keys['Ч'] = 'Ц'
    text_ = text_.replace('<', 'Ч')
    dict_keys['<'] = 'Ч'
    text_ = text_.replace('Ю', 'К')
    dict_keys['Ю'] = 'К'
    text_ = text_.replace('К', 'Ю')
    dict_keys['К'] = 'Ю'
    text_ = text_.replace('8', 'К')
    dict_keys['8'] = 'К'
    text_ = text_.replace('Б', 'Э')
    dict_keys['Б'] = 'Э'
    text_ = text_.replace('Й', 'Х')
    dict_keys['Й'] = 'Х'
    text_ = text_.replace('7', 'Й')
    dict_keys['7'] = 'Й'
    text_ = text_.replace('T', 'У')
    dict_keys['T'] = 'У'
    text_ = text_.replace('5', 'Б')
    dict_keys['5'] = 'Б'
    with open('key_for_task2.txt', 'w') as file:
        for key,val in dict_keys.items():
            file.write('{} : {}\n'.format(key,val))
    write_in_file("decoding.txt", text_)