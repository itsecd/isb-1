

def decryption(source: str = 'cod1.txt', destination: str = 'cod_freq.txt') -> None:
    with open(source, 'r', encoding='utf-8') as src:
        with open(destination, 'w', encoding='utf-8') as dest:
            stroka = src.read()
            size = len(stroka)
            d = {}
            for i in stroka:
                if i not in d.keys():
                    d[i] = 1
                else:
                    d[i] += 1
            tmp = sorted(d, key=d.get)
            tmp = tmp[::-1]
            for i in d.keys():
                d[i] /= size
            print(tmp)
            for i in tmp:
                dest.write(f'{i} - {round(d[i], 6)} \n')


if __name__ == "__main__":
    decryption()
