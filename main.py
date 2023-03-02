symbols='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,- '

def read_file(file_name):
    with open(f'{file_name}.txt','r',encoding='utf-8') as file:
        return file.read()
    
def save_file(file_name, text):
    with open(f'{file_name}.txt', 'w',encoding='utf-8') as file:
        file.write(text)