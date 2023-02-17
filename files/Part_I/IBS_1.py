string = "" 
shift = int(input()) 
 
with open("files/Part_I/text", "r", encoding="utf-8") as f: 
    text = f.read().split() 
    for word in text: 
        for l in word: 
            if l.isupper() == True: 
                c_unicode = ord(l) 
                c_index = ord(l) - ord("A") 
 
                new_index = (shift + c_index)%26  
                new_unicode = new_index + ord("A") 
                new_char = chr(new_unicode) 
                string+=new_char 
            elif l.islower() == True: 
                c_unicode = ord(l) 
                c_index = ord(l) - ord("a") 
 
                new_index = (shift + c_index)%26  
                new_unicode = new_index + ord("a") 
                new_char = chr(new_unicode) 
                string+=new_char 
        string+=" " 
print(shift)         
print(text)         
print(string)     
 
with open("files/Part_I/text_encrypted", "w", encoding="utf-8") as f: 
    f.write(string) 
    f.write("\n") 
 
with open("files/Part_I/key", "w", encoding="utf-8") as f: 
    f.write(str(shift)) 
    f.write("\n")