import re


def encryption(source: str = 'decrypted_text.txt', destination: str = 'encrypted_text.txt', key: str = 'key.txt') \
        -> None:
    with open(source, 'r', encoding='utf-8') as src:
        with open(destination, 'w', encoding='utf-8') as dest:
            with open(key, 'r', encoding='utf-8') as enc_key:
                alf1 = []
                alf2 = []
                for i in enc_key:
                    i = re.sub('\n', '', i)
                    x, y = re.split(' - ', i)
                    alf1.append(re.sub(r'"', '', x))
                    alf2.append(re.sub(r'"', '', y))
                for stroka in src:
                    enc_stroka = []
                    for i in stroka:
                        for j in range(len(alf1)):
                            if i.lower() == alf1[j]:
                                enc_stroka.append(alf2[j])
                    enc_stroka.append('\n')
                    dest.write(''.join(enc_stroka))


if __name__ == "__main__":
    encryption()
