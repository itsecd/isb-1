alphabet_lover = list("абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя")
alphabet_upper = list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

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
        
    def shift_decode(self, letter: str):
        try:
            
            try:
                id = int(len(alphabet_lover)/2) + alphabet_lover.index(letter) - self.shift
                return alphabet_lover[id]
            except:
                id = int(len(alphabet_upper)/2) + alphabet_upper.index(letter) - self.shift
                return alphabet_upper[id]
        except:
            return letter
        
    
    def get_shift(a: str, b: str):
        return abs(ord(a) - ord(b))
        
        
        