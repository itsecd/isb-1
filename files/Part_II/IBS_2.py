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
        print(*c, sep="\n")