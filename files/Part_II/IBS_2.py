total = 0 
 
with open("files/Part_II/text", "r", encoding="utf-8") as f: 
    string = f.read().split('\n') 
    text = "".join(string) 
    #print(text) 
    dict1 = {} 
    for l in text: 
        if l not in dict1: 
            dict1[l] = 1 
        else:  
            dict1[l]+=1  
        total+=1 
    dict_probability = {} 
    for key in dict1.keys(): 
        dict_probability[key] = dict1[key]/total 
    #print(len(dict_probability))     
    dict_probability = sorted(dict_probability.items(), key=lambda x: x[1], reverse=True) 
    for c in dict_probability: 
        print(*c)

    dict = {}
    
with open("files/Part_II/result", "w", encoding="utf-8") as f: 
    f.write(text.lower()) 
    f.write("\n") 

    text = text.replace(" ", "{")
    text = text.replace("Я", " ")
    dict["Я"] = " "

    text = text.replace("А", "&")
    text = text.replace("{", "A")
    dict["{"] = "А"

    text = text.replace("Е", "+")
    text = text.replace("Д", "Е")
    dict["Д"] = "Е"

    text = text.replace("Щ", "-")
    text = text.replace("Ч", "Щ")
    dict["Ч"] = "Щ"

    text = text.replace("К", "/")
    text = text.replace("Й", "К")
    dict["Й"] = "К"

    text = text.replace("О", "%")
    text = text.replace("4", "О")
    dict["4"] = "О"

    text = text.replace("Н", "№")
    text = text.replace("М", "Н")
    dict["M"] = "Н"

    print(text)
    f.write(text.lower()) 
    f.write("\n") 
    
    text = text.replace("И", "$")
    text = text.replace("t", "И")
    dict["t"] = "И"

    text = text.replace("Ч", "(")
    text = text.replace("Х", "Ч")
    dict["Х"] = "Ч"

    text = text.replace("Ь", ")")
    text = text.replace("Ъ", "Ь")
    dict["Ъ"] = "Ь"

    text = text.replace("З", ">")
    text = text.replace("r", "З")
    dict["r"] = "З"
    
    text = text.replace("Д", "<")
    text = text.replace("2", "Д")
    dict["2"] = "Д"

    text = text.replace("C", "*")
    text = text.replace("П", "С")
    dict["П"] = "С"

    text = text.replace("Ф", "Ё")
    text = text.replace("Т", "Ф")
    dict["T"] = "Ф"

    print(text)
    f.write(text.lower()) 
    f.write("\n") 
    

    text = text.replace("Р", "Т")
    dict["Р"] = "T"

    text = text.replace("Л", "[")
    text = text.replace("/", "Л")
    dict["К"] = "Л"

    text = text.replace("Г", "~")
    text = text.replace("1", "Г")
    dict["1"] = "Г"

    text = text.replace("[", "М")
    dict["Л"] = "М"

    text = text.replace("+", "Ж")
    dict["Е"] = "Ж"

    text = text.replace("X", "!")
    text = text.replace("У", "Х")
    dict["У"] = "Х"

    text = text.replace("%", "Р")
    dict["О"] = "Р"

    text = text.replace("5", "П")
    dict["5"] = "П"

    text = text.replace("$", "Й")
    dict["И"] = "Й"

    text = text.replace("B", "`")
    text = text.replace("Б", "В")
    dict["Б"] = "В"

    text = text.replace("Ы", "Ю")
    text = text.replace("-", "Ы")
    dict["Ы"] = "Ю"
    dict["Щ"] = "Ы"

    print(text)
    f.write(text.lower()) 
    f.write("\n")  
    

    text = text.replace(">", "У")
    dict["З"] = "У"

    text = text.replace(")", "Я")
    dict["Ь"] = "Я"

    text = text.replace("&", "Б")
    dict["А"] = "Б"

    text = text.replace("w", "Э")
    dict["w"] = "Э"
    text = text.replace("Ё", "Ц")
    dict["Ф"] = "Ц"

    text = text.replace("?", ".")
    dict["?"] = "."

    print(text)
    f.write(text.lower()) 
    f.write("\n") 


with open("files\Part_II\key", "w", encoding="utf-8") as f: 
    f.write(str(dict))
    f.write("\n") 
