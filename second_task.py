if __name__ == '__main__':
    freq_letters = {}
    with open('frequency.txt', 'r', encoding = 'utf-8') as f:
        for i in range(33):
            row = f.readline()
            row = row.split('\n')
            row = row[0].split('=')
            freq_letters[row[0]] = [row[1]]