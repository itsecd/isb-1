alphabet_lover = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя")
alphabet_upper = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

class Shifter:
    """Give a shift and get a letter shifted by russian alphabet
    """
    def __init__(sefl, shift: int = 0):
        
        
        if shift < 0 or shift > 33 : raise Exception("Range must be from 0 to 33 for russian alphabet.")
        
        sefl.shift = shift
    
    def shift_encode(self, letter: str)-> str:
        try:
            
            try:
                return alphabet_lover[alphabet_lover.index(letter) + self.shift]
            except:
                return alphabet_upper[alphabet_upper.index(letter) + self.shift]
        except:
            return letter
        
    def shift_decode(self, letter: str)-> str:
        try:
            
            try:
                return alphabet_lover[alphabet_lover.index(letter) - self.shift + len(alphabet_lover)]
            except:
                return alphabet_upper[alphabet_upper.index(letter) - self.shift + len(alphabet_upper)]
        except:
            return letter
        
    
    def get_shift(a: str, b: str):
        return ord(a) - ord(b)
        
        
        