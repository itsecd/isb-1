from first_task import save_text

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

    freq_letters = list(freq_letters.items())
    text_freq = list(text_freq.items())

    decrypted_text = topic

    decrypted_text = decrypted_text.replace(text_freq[31][0], freq_letters[29][0])
    decrypted_text = decrypted_text.replace(text_freq[17][0], freq_letters[17][0])
    decrypted_text = decrypted_text.replace(text_freq[0][0], freq_letters[0][0])
    decrypted_text = decrypted_text.replace(text_freq[14][0], freq_letters[10][0])
    decrypted_text = decrypted_text.replace(text_freq[27][0], freq_letters[22][0])
    decrypted_text = decrypted_text.replace(text_freq[29][0], freq_letters[30][0])
    decrypted_text = decrypted_text.replace(text_freq[18][0], freq_letters[18][0])
    decrypted_text = decrypted_text.replace(text_freq[15][0], freq_letters[13][0])
    decrypted_text = decrypted_text.replace(text_freq[22][0], freq_letters[24][0])
    decrypted_text = decrypted_text.replace(text_freq[3][0], freq_letters[7][0])
    decrypted_text = decrypted_text.replace(text_freq[1][0], freq_letters[2][0])
    decrypted_text = decrypted_text.replace(text_freq[2][0], freq_letters[3][0])
    decrypted_text = decrypted_text.replace(text_freq[4][0], freq_letters[1][0])
    decrypted_text = decrypted_text.replace(text_freq[5][0], freq_letters[6][0])
    decrypted_text = decrypted_text.replace(text_freq[6][0], freq_letters[5][0])
    decrypted_text = decrypted_text.replace(text_freq[7][0], freq_letters[4][0])
    decrypted_text = decrypted_text.replace(text_freq[20][0], freq_letters[16][0])
    decrypted_text = decrypted_text.replace(text_freq[8][0], freq_letters[8][0])
    decrypted_text = decrypted_text.replace(text_freq[9][0], freq_letters[9][0])
    decrypted_text = decrypted_text.replace(text_freq[10][0], freq_letters[12][0])
    decrypted_text = decrypted_text.replace(text_freq[16][0], freq_letters[21][0])
    decrypted_text = decrypted_text.replace(text_freq[11][0], freq_letters[15][0])
    decrypted_text = decrypted_text.replace(text_freq[26][0], freq_letters[26][0])
    decrypted_text = decrypted_text.replace(text_freq[12][0], freq_letters[14][0])
    decrypted_text = decrypted_text.replace(text_freq[13][0], freq_letters[11][0])
    decrypted_text = decrypted_text.replace(text_freq[24][0], freq_letters[23][0])
    decrypted_text = decrypted_text.replace(text_freq[19][0], freq_letters[25][0])
    decrypted_text = decrypted_text.replace(text_freq[21][0], freq_letters[19][0])
    decrypted_text = decrypted_text.replace(text_freq[28][0], freq_letters[31][0])
    decrypted_text = decrypted_text.replace(text_freq[23][0], freq_letters[27][0])
    decrypted_text = decrypted_text.replace(text_freq[30][0], freq_letters[28][0])
    decrypted_text = decrypted_text.replace(text_freq[25][0], freq_letters[20][0])

    save_text(decrypted_text, 'decrypted_cod4')
