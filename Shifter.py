class Shifter:
    """Give a shift and get a letter shifted by russian alphabet
    """
    def __init__(sefl, shift: int = 0):
        sefl.alphabet_lover = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        sefl.alphabet_upper = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
        
        if shift < 0 or shift > 33 : raise Exception("Range must be from 0 to 33 for russian alphabet.")
        
        sefl.shift = shift
    
    def get_shifted(self, letter: str)-> str:
        try:
            
            try:
                return self.alphabet_lover[self.alphabet_lover.index(letter) + self.shift]
            except:
                return self.alphabet_upper[self.alphabet_upper.index(letter) + self.shift]
        except:
            return letter
        
        