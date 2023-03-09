ALPHABET = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
FREQUENCY = [
    (' ', 0.128675),
    ('О', 0.096456),
    ('И', 0.075312),
    ('Е', 0.072292),
    ('А', 0.064841),
    ('Н', 0.061820),
    ('Т', 0.061619),
    ('С', 0.051953),
    ('Р', 0.040677),
    ('В', 0.039267),
    ('М', 0.029803),
    ('Л', 0.029400),
    ('Д', 0.026983),
    ('Я', 0.026379),
    ('К', 0.025977),
    ('П', 0.024768),
    ('З', 0.015908),
    ('Ы', 0.015707),
    ('Ь', 0.015103),
    ('У', 0.013290),
    ('Ч', 0.011679),
    ('Ж', 0.010673),
    ('Г', 0.009867),
    ('Х', 0.008659),
    ('Ф', 0.007249),
    ('Й', 0.006847),
    ('Ю', 0.006847),
    ('Б', 0.006645),
    ('Ц', 0.005034),
    ('Ш', 0.004229),
    ('Щ', 0.003625),
    ('Э', 0.002416),
    ('Ъ', 0.000000)
]


def find_in_text_frequency(input: str, list_of_tuple: list) -> tuple:
    for elem in list_of_tuple:
        if elem[1] == input:
            return elem


def find_in_frequency(input: tuple) -> str:
    i = 0
    find = False
    while not find:
        elem = FREQUENCY[i]
        if float(input[0]) <= elem[1]:
            i += 1
        else:
            find = True
    elem = FREQUENCY[i]
    return elem[0]


def calc(input: str) -> list:
    input_len = len(input)
    result = []
    counter = 1
    j = 0
    while len(input) != 0:
        while j < len(input):
            if input[j] == input[0]:
                counter += 1
            j += 1
        if len(input):
            result.append((round(counter / input_len, 6), input[0]))
            input = input.replace(input[0], '')
            counter = 1
            j = 1
    result.sort(reverse=True)
    return result


if __name__ == "__main__":
    text = ""
    result_text = ""
    with open("code6.txt", "r", encoding="utf-8") as file:
        text = file.read()
    text = text.replace(' ', '+')
    result_list = calc(text.replace('\n', ''))
    i = 1
    for elem in result_list:
        print(f"{i} - {elem}")
        i += 1
    i = 1
    for elem in text:
        if elem == '\n':
            result_text += '\n'
        else:
            elem_tuple = find_in_text_frequency(elem, result_list)
            result_text += find_in_frequency(elem_tuple)
    with open("result.txt", 'w', encoding="utf-8") as file:
        file.write(result_text)
