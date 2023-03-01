def get_alp_freq(filename:str) -> dict:
    result = {}
    with open(f'{filename}.txt', 'r', encoding = 'utf-8') as f:
        for i in range(33):
            row = f.readline()
            row = row.split('\n')
            row = row[0].split('=')
            result[row[0]] = [row[1]]
    return result

def get_text_freq(text:str) -> dict:
    result = {}
    length = len(text)
    text_letters = []

    for letter in text:
        if text_letters.count(letter) == 0:
            text_letters.append(letter)

    for letter in text_letters:
        result[letter] = text.count(letter) / length

    result = sorted(result.items(), key = lambda x: x[1])
    result = dict(result[::-1])

    with open('text_freq.txt', 'w', encoding = 'utf-8') as f:
        let = list(result.keys())
        fre = list(result.values())
        for i in range(32):
            row = let[i] + '=' + str(fre[i]) + '\n'
            f.writelines(row)

    return result

if __name__ == '__main__':
    freq_letters = get_alp_freq('frequency')
    with open('encr_cod4.txt', 'r', encoding='utf-8') as f:
        topic = f.read()
    text_freq = get_text_freq(topic)
