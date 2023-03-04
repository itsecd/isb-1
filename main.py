def encode():
    alf1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    alf2 = " абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    text = "Парень, который придумал колесо. В двадцать пятом веке, наконец, разыскали, воскресили и стали чествовать того, кто изобрел колесо. А он ходил, печальный, с одного молочного банкета на другой, и каждый раз, захмелев от парного, бил себя в грудь: - Братцы, что вы меня хвалите, я-то что? Колесо, ведь оно, как луна, как солнце, опять же круги по воде идут, если камень бросишь... Не много ума надо, чтоб до колеса допереть... А вот кто ось придумал - это да! Хороший был этот парень, который придумал колесо."
    encoded_text = ""
    text = text.lower()
    for symbol in text:
        flag = False
        for j in range(len(alf1)):
            if symbol == alf1[j]:
                encoded_text += alf2[j]
                flag = True
        if not flag:
            encoded_text += symbol
    print(encoded_text)


def bubble(list_nums, dop_list):
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for i in range(len(list_nums) - 1):
            if list_nums[i] < list_nums[i + 1]:
                list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
                dop_list[i], dop_list[i + 1] = dop_list[i + 1], dop_list[i]
                swap_bool = True


def decode():
    text = "7ОУ8cr8ЛБ8ЧХОДХЛМtcbЛrАc<МАcРcМАЕc<ХЛД8cХcБАc5МА1cБКХ<Хr8cКД8cr8cБК87ЛМОРДb8МЛbcАБМХЕОД4r ЕcОД>АКХМЕАЕcЛУОМХb?cБАЛ2АД42tcАrcr8cХЛБАД4Фt8МcrХ2О2А1cХrИАКЕОЧХХcАcЛУХЕО8ЕАЕcМ82ЛМ8?c<МАП cБАrbМ4c2О2cБКАХЛЙА7ХМcЛУОМХ8cХЛБАД4ФtaЬ88cФrОrХbcАcМ82ЛМ8cР8Кr8ЕЛbc2cБАrbМХbЕc5rМКАБХХcХcХrИАКЕОМХРrАЛМХcМ82ЛМОccЛРbФ4cЕ8У7tcР8КАbМrАЛМbЕХcХc2А7ОЕХcХФt<О8МЛbcРcОД>8ПКОХ<8Л2А1cМ8АКХХc2А7ХКАРОrХbcАЛrАРrА1cМ8АКХ81c2АМАКА1cbРДb8МЛbcrХ2МАcХrА1c2О2c2ДА7c5ДРt7cЫ8rrАrc8>АcМ8АК8Е c2А7ХКАРОrХbcХЛМА<rХ2ОcХЛБАД4ФtaМЛbcА<8r4cО2МХРrАcХcФ78Л4"
    alf1 = ""
    decoded_text = ""
    for symbol in text:
        flag = True
        for alf_sym in alf1:
            if symbol == alf_sym:
                flag = False
        if flag:
            alf1 += symbol
    text_indexes = [0] * len(alf1)
    for symbol in text:
        for i in range(len(alf1)):
            if symbol == alf1[i]:
                text_indexes[i] += 1
    for i in range(len(text_indexes)):
        text_indexes[i] = text_indexes[i]/len(text)
    alf_list = list()
    for sym in alf1:
        alf_list.append(sym)
    bubble(text_indexes, alf_list)
    for i in range(len(alf_list)):
        print(f"{alf_list[i]} = {text_indexes[i]}")
    alf2 = " оиетнсакярмлпвдьучйзжэыгц,фбюхщш"
    str = ""
    for i in range(len(alf_list)):
        str += alf_list[i]
    print(str)
    for symbol in text:
        flag = False
        for j in range(len(str)):
            if symbol == str[j]:
                decoded_text += alf2[j]
                flag = True
        if not flag:
            decoded_text += symbol
    print(decoded_text)
    for i in range(len(alf1)):
        print(f"{alf1[i]} -> {alf2[i]}")


if __name__ == "__main__":
    encode()
    decode()
