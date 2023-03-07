def main():
    print("start")
    text=input("Зашифрованный текст: ")
    length=len(text)
    set_text= set(text)
    A={}
    for i in set_text:
        counter=0
        for j in text:
            if j==i:
                counter+=1
        A[i]=counter/length
    
    sorted_tuple = sorted(A.items(), key=lambda x:x[1], reverse=True)
    for item in sorted_tuple:
        print("Частота ",item[0]," равна: ",item[1])        
    print("end")
    
if __name__ == "__main__":
    main()
    



